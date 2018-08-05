from odoo import fields, models

class materiel(models.Model):
    _name = 'materiel'

    nom = fields.Char(string='nom')
    type = fields.Char(string="type")
    descreption = fields.Text(string="descreption du materiel")
    event_id = fields.Many2many('event.event','matrielevent','materiel_id','event_id', string="matriel affected")
    