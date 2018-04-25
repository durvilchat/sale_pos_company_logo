# -*- coding: utf-8 -*-

{
    'name': 'change the logo on your point of sale',
    'category': 'Sales',
    'summary': 'This plugin allows you to replace the odoo logo of the point of sale with the logo of your company',
    'author': "Kywana dev solution",
    'version': '1.0',
    'price': 5,
    'currency': 'EUR',
    'license': 'AGPL-3',
    'installable': True,
    'application': False,
    'images': ['images/demo.jpg', 'images/demo2.jpg'],
    'depends': ['point_of_sale'],
    'data': [
        'views/templates.xml',
    ]
}
