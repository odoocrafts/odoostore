# -*- coding: utf-8 -*-
{
    'name': 'SO Stock Balance Corrector',
    'version': '19.0.1.0.0',
    'category': 'Inventory/Delivery',
    'summary': 'Automatic "Phantom" Picking Generation on Quantities Decreases',
    'description': """
        When a Sales Order line has a confirmed delivery that has been generated or printed, 
        changing your mind and decreasing the order line quantity natively triggers a bug where 
        a phantom return is generated. This module cleanly adjusts the existing picking document 
        to reflect the correct allocations instead of inflating forecasting availability.
    """,
    'author': 'Odoocrafts Innovations',
    'website': 'https://odoocrafts.com',
    'license': 'OPL-1',
    'price': 60.0,
    'currency': 'EUR',
    'depends': ['sale_stock'],
    'data': [],
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': False,
    'auto_install': False,
}
