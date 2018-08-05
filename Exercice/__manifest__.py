# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'exercice',
    'version' : '1.1',
    'summary': 'testrajaa',
    'sequence': 30,
    'description': """
Core mechanisms for the accounting modules. To display the menuitems, install the module account_invoicing.
    """,
    'category': 'test',
    'website': '',
    'images' : [],
    'depends' : ['base','sale','event'],
    'data': [
        "views/sale_view.xml",
        "report/views/sale_report_templates.xml",
        "views/organisateur.xml",
        "views/event_view.xml",
        "views/materiel.xml"
        ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': False,
    'auto_install': False,
}
