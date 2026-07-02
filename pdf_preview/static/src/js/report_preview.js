/** @odoo-module **/

import { registry } from "@web/core/registry";
import { getReportUrl } from "@web/webclient/actions/reports/utils";
import { user } from "@web/core/user";

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
        
        // Block UI momentarily if we were going to, but for opening in new tab it's instantaneous
        // We open the native PDF route in a new tab. Browsers will automatically preview application/pdf.
        window.open(url, "_blank");

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
