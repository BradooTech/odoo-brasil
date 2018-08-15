# -*- coding: utf-8 -*-
{
    'name': "Extensão Localização",
    'description': """
        Long description of module's purpose
    """,

    'author': "Bradoo",
    'website': "https://bradootech.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Localization',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'br_account', 'br_nfe'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/account_fiscal_position.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'auto_install': True
}