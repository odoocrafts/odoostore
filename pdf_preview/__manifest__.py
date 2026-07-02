# -*- coding: utf-8 -*-
{
    'name': 'PDF Preview',
    'version': '19.0.1.0.0',
    'category': 'Extra Tools',
    'summary': 'Preview PDF reports directly in the browser instead of automatically downloading them.',
    'description': """
PDF Preview for Odoo
====================
This module modifies the default behavior of Odoo when printing PDF reports (like invoices, quotations, etc.).
Instead of automatically downloading the PDF to your device, it opens the PDF inline in a new browser tab for a quick preview.
From there, users can choose to download or print using the browser's native PDF viewer.
    """,
    'author': 'Odoocrafts Innovations',
    'website': 'https://odoocrafts.com',
    'license': 'OPL-1',
    'price': 0.0,
    'currency': 'EUR',
    'depends': ['web'],
    'data': [],
    'assets': {
        'web.assets_backend': [
            'pdf_preview/static/src/js/report_preview.js',
        ],
    },
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': False,
    'auto_install': False,
}
