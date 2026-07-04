/** @odoo-module **/

import { Component, useRef } from "@odoo/owl";
import { Dialog } from "@web/core/dialog/dialog";
import { download } from "@web/core/network/download";

export class PDFPreviewDialog extends Component {
    static template = "pdf_preview_oc.PDFPreviewDialog";
    static components = { Dialog };
    static props = {
        title: { type: String, optional: true },
        url: { type: String },
        downloadData: { type: Object },
        close: { type: Function },
    };

    setup() {
        this.iframeRef = useRef("iframeRef");
    }

    onPrint() {
        if (this.iframeRef.el && this.iframeRef.el.contentWindow) {
            this.iframeRef.el.contentWindow.print();
        }
    }

    onDownload() {
        download({
            url: "/report/download",
            data: this.props.downloadData,
        });
    }
}
