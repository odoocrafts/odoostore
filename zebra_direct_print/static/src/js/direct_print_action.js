/** @odoo-module **/

import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";

/**
 * Handles the direct printing to local WebSockets
 * Used for ZPL/TSPL raw strings
 */
async function triggerDirectPrint(env, action) {
    const rawData = action.params.raw_data;
    const wsUrl = action.params.ws_url || "ws://127.0.0.1:8181";

    if (!rawData) {
        env.services.notification.add("No print data generated.", { type: "danger" });
        return;
    }

    try {
        const socket = new WebSocket(wsUrl);

        socket.onopen = () => {
            // Socket opened, send the raw ZPL/TSPL string
            socket.send(rawData);
            env.services.notification.add("Label sent to printer.", { type: "success" });
            
            // Close after sending (or QZ tray handles closing appropriately)
            setTimeout(() => {
                socket.close();
            }, 500);
        };

        socket.onerror = (error) => {
            console.error("WebSocket Error:", error);
            env.services.notification.add("Failed to connect to local print spooler at " + wsUrl, { type: "danger" });
        };

    } catch (err) {
        console.error("Direct Print Error:", err);
        env.services.notification.add("Error initiating print connection.", { type: "danger" });
    }
}

registry.category("actions").add("zebra_direct_print.trigger_print", triggerDirectPrint);
