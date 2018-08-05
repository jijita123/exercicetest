# -*- coding: utf-8 -*-
from odoo import  models, fields, api
class sales(models.Model):
    _inherit = 'sale.order'
    Exercice = fields.Char(string="Exercice",translate=True)
