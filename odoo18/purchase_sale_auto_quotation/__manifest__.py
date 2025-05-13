# -*- coding: utf-8 -*-
{
    'name': "purchase sale auto quote",

    'summary': "Autotmatic sales quotation creation depends on related server purchase order",

    'description': """
Long description of module's purpose
    """,

    'author': "ITOS",
    'website': "https://www.itos-eg.com",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','web','website','sale_management','purchase'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        # 'views/templates.xml',
    ],
    'installable': True,
    'application': False,  
}

