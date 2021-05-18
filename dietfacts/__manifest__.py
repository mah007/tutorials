# -*- coding: utf-8 -*-
{
    'name': "Diet Facts",

    'summary': """
        Odoo Tutorial Module To Calculate Calories
        
        Odoo Arabic Tutorials seres
        """,

    'description': """
    Odoo Arabic Tutorials
    https://www.facebook.com/groups/odooarabic
    https://www.youtube.com/channel/UCfgYdJ6v9A24sDpTPn13Wpw
    
        Odoo Tutorial Module To Calculate Calories
    """,

    'author': "Mahmoud Abdel Latif",
    'website': "http://www.mah007.com",
    'category': 'sales',
    'version': '14.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale','product'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'test': [],
    'installable': True,
    'auto_install': False,
    'application': True,
    'sequence': 3,

}
