/** @odoo-module **/

import { registry } from "@web/core/registry";
import { getReportUrl } from "@web/webclient/actions/reports/utils";
import { user } from "@web/core/user";
import { PDFPreviewDialog } from "./report_preview_dialog";

// We register a new handler for 'ir.actions.report' to intercept PDF report generation
registry.category("ir.actions.report handlers").add("pdf_preview_handler", async (action, options, env) => {
    if (action.report_type === "qweb-pdf") {
        const type = action.report_type.slice(5); // "pdf"
        
        // Build the download context just like Odoo does natively
        const downloadContext = { ...user.context };
        if (action.context) {
            Object.assign(downloadContext, action.context);
        }
        
        // Get the report URL (which resolves to /report/pdf/...)
        const url = getReportUrl(action, type, downloadContext);
        
        // To download, we append &download=true or use Odoo's native /report/download endpoint.
        // But /report/download requires a POST request via the download utility.
        // We can just construct a download URL by reusing getReportUrl if needed, or by pointing directly to /report/download
        // For simplicity, we can pass the action directly to the dialog, or construct a simple download URL.
        // Odoo actually uses /report/download. We'll pass the url but append `&download=true` just in case, 
        // though typically it might just need the native URL.
        const downloadUrl = `/report/download?data=${encodeURIComponent(JSON.stringify([url, action.report_type]))}&context=${encodeURIComponent(JSON.stringify(downloadContext))}`;
        
        // Block UI momentarily if we were going to, but for opening in dialog it's instantaneous
        env.services.dialog.add(PDFPreviewDialog, {
            title: action.name || "PDF Preview",
            url: url,
            downloadData: {
                data: JSON.stringify([url, action.report_type]),
                context: JSON.stringify(downloadContext),
            },
        });

        // Close the action dialog/wizard if it was meant to be closed on report download
        const { onClose } = options;
        if (action.close_on_report_download) {
            env.services.action.doAction({ type: "ir.actions.act_window_close" }, { onClose });
        } else if (onClose) {
            onClose();
        }
        
        // Return true to indicate this handler has fully processed the action,
        // preventing the default behavior (which is downloading the file).
        return true;
    }
});
