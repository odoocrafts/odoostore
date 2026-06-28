from odoo import api, fields, models, _

class InventoryRecommendation(models.Model):
    _name = 'inventory.recommendation'
    _description = 'AI Inventory Recommendation'
    _order = 'priority desc, id desc'

    name = fields.Char(string='Recommendation', required=True)
    product_id = fields.Many2one('product.product', string='Product')
    action_type = fields.Selection([
        ('purchase', 'Purchase'),
        ('delay', 'Delay Purchase'),
        ('transfer', 'Transfer Stock'),
        ('supplier', 'Investigate Supplier'),
        ('reduce', 'Reduce Inventory'),
    ], string='Action Type', required=True)
    priority = fields.Selection([
        ('0', 'Low'),
        ('1', 'Normal'),
        ('2', 'High'),
        ('3', 'Urgent'),
    ], string='Priority', default='1')
    explanation = fields.Text(string='AI Explanation')
    state = fields.Selection([
        ('draft', 'New'),
        ('done', 'Completed'),
        ('cancel', 'Ignored'),
    ], string='Status', default='draft')
    confidence_score = fields.Integer(string='Confidence Score (%)', default=90)

    @api.model
    def action_generate_recommendations(self):
        # MVP: Rule-based generation (dummy logic)
        self.search([('state', '=', 'draft')]).unlink()
        
        products = self.env['product.product'].search([('type', '=', 'consu')], limit=3) # Product may not be stored in demo data with storable
        if products:
            self.create({
                'name': f'Purchase {products[0].name}',
                'product_id': products[0].id,
                'action_type': 'purchase',
                'priority': '3',
                'explanation': f"Projected demand for {products[0].name} exceeds available inventory in 14 days. Supplier lead time has increased.",
                'confidence_score': 95,
            })
            
        if len(products) > 1:
            self.create({
                'name': f'Review Overstock for {products[1].name}',
                'product_id': products[1].id,
                'action_type': 'reduce',
                'priority': '2',
                'explanation': f"{products[1].name} has 6 months of supply tying up capital. Consider reducing future orders.",
                'confidence_score': 88,
            })
