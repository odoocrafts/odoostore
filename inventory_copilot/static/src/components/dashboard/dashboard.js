/** @odoo-module **/

import { Component, onWillStart } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";

export class InventoryCopilotDashboard extends Component {
    setup() {
        this.orm = useService("orm");
        this.action = useService("action");
        this.state = {
            healthData: {},
        };

        onWillStart(async () => {
            await this.loadData();
        });
    }

    async loadData() {
        this.state.healthData = await this.orm.call(
            "inventory.health",
            "get_dashboard_data",
            []
        );
    }

    openRecommendations() {
        this.action.doAction("inventory_copilot.action_inventory_recommendation");
    }
}

InventoryCopilotDashboard.template = "inventory_copilot.Dashboard";

registry.category("actions").add("inventory_copilot.dashboard", InventoryCopilotDashboard);
