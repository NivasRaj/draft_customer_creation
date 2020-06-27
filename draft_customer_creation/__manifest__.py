#-*- coding:utf-8 -*-
{
    'name': 'Sale -  Customer creation with Approval process',
    'category': 'CRM',
    'version': '13.0.1',
    'sequence': 1,
    'author': 'Nivas M',
    'summary': 'Create a draft customer and approve to become Customer.',
    'description': """"
            1) Customer Creation for 'create and edit' option in partner_id field in SO form."
            2) Customer record will move to 'Draft Customer' menu.
            3) Administrator can approve the newly created customer.
            4) Finally you can see your customer record in existing 'Customer' menu.
        """,
    'website': '',
    'price': 5,
    'currency': 'EUR',
    'license': 'OPL-1',
    'depends': ['base','sale','sale_management'],
    'data': [
        'views/inherited_sale_views.xml',
        'views/res_partner_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}