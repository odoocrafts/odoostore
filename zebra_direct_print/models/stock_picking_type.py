from odoo import fields, models

class StockPickingType(models.Model):
    _inherit = 'stock.picking.type'

    zebra_label_template_id = fields.Many2one(
        'zebra.label.template', 
        string="Direct Print Label Template",
        help="Select the ZPL/TSPL template to use for direct printing from this operation type."
    )
    printer_websocket_url = fields.Char(
        string="Printer WebSocket URL",
        default="ws://127.0.0.1:8181",
        help="WebSocket URL for the client's local printer bridge (e.g. QZ Tray)."
    )
