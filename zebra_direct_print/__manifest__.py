{
    'name': 'ZebraDirect: Raw Printer Engine Thermal Barcode Label PDF',
    'version': '19.0.1.0.0',
    'category': 'Inventory',
    'summary': 'Bypass PDF generation. Print ZPL/TSPL labels directly to thermal printers.',
    'description': """
ZebraDirect: Raw Printer Engine
===============================
This module completely bypasses standard Odoo PDF generation for labels.
It introduces a visual label designer that compiles layouts directly into raw printer
control languages (ZPL for Zebra, TSPL for TSC).

Features:
- Instantaneous printing without intermediate PDF rendering.
- Pixel-perfect sharp borders and zero browser margin shifts.
- Define raw ZPL/TSPL templates and render with Jinja.
- Direct raw socket printing via WebSocket to local hardware.
    """,
    'author': 'Odoocrafts Innovations',
    'website': 'https://odoocrafts.com',
    'license': 'OPL-1',
    'price': 76.0,
    'currency': 'EUR',
    'depends': ['stock', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'views/zebra_label_template_views.xml',
        'views/stock_picking_type_views.xml',
        'views/stock_picking_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'zebra_direct_print/static/src/js/direct_print_action.js',
        ],
    },
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': True,
}
