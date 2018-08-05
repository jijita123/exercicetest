# -*- coding: utf-8 -*-
from odoo import  models, fields, api
class events(models.Model):
    _inherit = 'event.event'
    theme = fields.Char(string="thème de évent")
    organisateur_id = fields.Many2one('organisateur',string="organisateur")
    materiel_id = fields.Many2many('materiel','materielevent','event_id','materiel_id',string="events name")
