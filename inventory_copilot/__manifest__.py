{
    'name': 'Inventory Copilot',
    'version': '19.0.1.0.0',
    'category': 'Inventory/Inventory',
    'summary': 'AI-powered inventory decision support for Odoo',
    'description': """
Inventory Copilot transforms Odoo's inventory module from a reporting system into an intelligent decision-making assistant.
    """,
    'author': 'Odoocrafts Innovations',
    'website': 'https://odoocrafts.com',
    'depends': ['stock', 'purchase'],
    'data': [
        'security/ir.model.access.csv',
        'data/ir_cron_data.xml',
        'views/inventory_recommendation_views.xml',
        'views/res_config_settings_views.xml',
        'views/menu_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'inventory_copilot/static/src/components/dashboard/**/*.js',
            'inventory_copilot/static/src/components/dashboard/**/*.xml',
            'inventory_copilot/static/src/components/dashboard/**/*.scss',
            'inventory_copilot/static/src/components/dashboard/**/*.css',
        ],
    },
    'price': 199.0,
    'currency': 'EUR',
    'license': 'OPL-1',
    'installable': True,
    'application': True,
    'images': ['static/description/banner.png'],
}
