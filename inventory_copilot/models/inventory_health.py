from odoo import api, fields, models, _

class InventoryHealth(models.Model):
    _name = 'inventory.health'
    _description = 'Inventory Health KPI'
    
    name = fields.Char(string='Name', required=True)
    score = fields.Integer(string='Health Score (%)')
    stockout_risk_count = fields.Integer(string='Stockout Risks')
    overstock_risk_count = fields.Integer(string='Overstock Risks')
    dead_stock_value = fields.Float(string='Dead Stock Value')
    inventory_turnover = fields.Float(string='Inventory Turnover')
    supplier_score = fields.Integer(string='Supplier Reliability Score')

    @api.model
    def action_generate_health_metrics(self):
        # MVP: Rule-based generation of a dummy health record
        self.search([]).unlink() # Keep one record for dashboard simplicity
        self.create({
            'name': 'Current Inventory Health',
            'score': 78,
            'stockout_risk_count': 12,
            'overstock_risk_count': 5,
            'dead_stock_value': 12500.0,
            'inventory_turnover': 4.2,
            'supplier_score': 85,
        })
        
    @api.model
    def get_dashboard_data(self):
        record = self.search([], limit=1)
        if not record:
            self.action_generate_health_metrics()
            record = self.search([], limit=1)
            
        return {
            'score': record.score,
            'stockout_risk_count': record.stockout_risk_count,
            'overstock_risk_count': record.overstock_risk_count,
            'dead_stock_value': record.dead_stock_value,
            'inventory_turnover': record.inventory_turnover,
            'supplier_score': record.supplier_score,
        }
