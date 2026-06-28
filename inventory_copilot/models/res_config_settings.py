from odoo import models, fields

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    inventory_copilot_openai_api_key = fields.Char(
        string='OpenAI API Key',
        config_parameter='inventory_copilot.openai_api_key'
    )
