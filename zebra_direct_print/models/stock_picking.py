from odoo import models, _
from odoo.exceptions import UserError

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    def action_direct_print_labels(self):
        """
        Gathers raw ZPL data and triggers a client action to send it via WebSocket.
        """
        self.ensure_one()
        
        template = self.picking_type_id.zebra_label_template_id
        if not template:
            raise UserError(_('No direct print template configured for this operation type.'))

        # Example: we print a label for each stock move line
        records_to_print = self.move_line_ids
        if not records_to_print:
            # Fallback to moves if no lines yet, or print one for picking
            records_to_print = self.move_ids if self.move_ids else self

        # Compile raw string array
        rendered_labels = template.render_template(records_to_print)
        
        # Combine labels or send as array
        raw_data = ''.join(rendered_labels)

        return {
            'type': 'ir.actions.client',
            'tag': 'zebra_direct_print.trigger_print',
            'params': {
                'raw_data': raw_data,
                'ws_url': self.picking_type_id.printer_websocket_url or 'ws://127.0.0.1:8181',
                'printer_type': template.printer_type,
            }
        }
