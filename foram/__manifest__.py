# -*- coding: utf-8 -*-
{
    'name': "Foram",

    'summary': """
       This app about courses for those who want to learn new skill""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Chekc https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '14.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'course_detail.xml',
        #     # 'views/views.xml',
        #     # 'views/templates.xml',
        #     'views/course_detail.xml',
        #     # 'views/sale_order_view_up.xml'
    ],
    # only loaded in demonstration mode

    'installable': True,
    # 'application': True,
    'auto_install': False
}
