from odoo import api, fields, models
from jinja2 import Environment

class ZebraLabelTemplate(models.Model):
    _name = 'zebra.label.template'
    _description = 'Zebra/TSC Label Template'

    name = fields.Char(string="Template Name", required=True)
    printer_type = fields.Selection([
        ('zpl', 'Zebra (ZPL)'),
        ('tspl', 'TSC (TSPL)')
    ], string="Printer Command Language", default='zpl', required=True)
    
    # Template body for raw ZPL/TSPL containing Jinja2 placeholders
    body_raw = fields.Text(string="Template Body", required=True, 
                           help="Write your raw ZPL/TSPL here. Use {{ record.field }} for dynamic data.")
    
    active = fields.Boolean(default=True)

    def render_template(self, records):
        """
        Renders the Jinja2 template using the given records.
        Returns a list of rendered strings (one per record).
        """
        env = Environment()
        template = env.from_string(self.body_raw)
        
        results = []
        for record in records:
            rendered = template.render(record=record, env=self.env)
            results.append(rendered)
            
        return results
