# -*- coding: utf-8 -*-
{
    'name': "MyModule",
    'version': '0.2',
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Productivity/MyModule',
    'description': """
        Long description of module's purpose
    """,
    'website': "http://www.yourcompany.com",
    'summary': """
    Short (1 phrase/line) summary of the module's purpose, used as
    subtitle on modules listing or apps.openerp.com""",
    # any module necessary for this one to work correctly
    'depends': ['base'],
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
    'installable': True,
    'application': True,
    'auto_install': False,
    'author': "My Company",










}
