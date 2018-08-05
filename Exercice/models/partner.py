from odoo import fields, models

class Partner(models.Model):
    _inherit = 'res.partner'

    organizer_id = fields.Many2one('organisateur', readonly=True)
