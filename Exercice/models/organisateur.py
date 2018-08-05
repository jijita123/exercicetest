# -*- coding: utf-8 -*-
from odoo import  models, fields, api

class organisateur(models.Model):
    _name='organisateur'
    
    nom = fields.Char(string="nom", required=True)
    prenom = fields.Char(string="prénom")
    tel = fields.Char(string="Numéro de téléphone")
    mail = fields.Char(string="Adresse email")
    status = fields.Selection([('homme', 'Mr'), ('femme', 'Madame')])
    test = fields.Char(default="a value")
    value = fields.Integer()
    tax = fields.Integer()
    total = fields.Integer(string="total",readonly=True)
    
    
    rate = fields.Float(string='Rate (%)',default=100.0)
    amount = fields.Float()
    quantity = fields.Float( default=1.0)
    totale = fields.Float(compute='_compute_total', string='Total', store=True)

    @api.depends('quantity', 'amount', 'rate')
    def _compute_total(self):
        for line in self:
            line.totale = float(line.quantity) * line.amount * line.rate / 100
    
    
    @api.onchange('value', 'tax')
    def onchange_method(self):
        self.total = self.tax + self.value 
    @api.model
    def create(self, vals):                
        res={}
        print('vals',vals)
        if 'mail' not in vals:
            mail= ''
        else :
            mail =vals.get('mail') 
        
        if 'status' not in  vals:
            status= ''
        else :
            status =vals.get('status') 
       
        if 'tel' not in  vals:
            tel= ''
        else :
            tel =vals.get('tel') 
    
            res=super(organisateur, self).create(vals)
            print('res',res)
        print('valsnoom',vals['nom'])
        partner = self.env['res.partner'].create({
            'name': vals['nom'],
            'mail': mail,
            'is_company': status,
            'organizer_id':res.id,
           # 'status': vals.get('status'),
            
            'phone':tel,
            #'website': vals.get('status'),
            })
        print('parrtnrett',partner)
        return res
    
    @api.multi
    def write(self, vals):
        print('valswritevals',vals)
        print('oranisteur_id',self)
        pargtner_id=self.env['res.partner'].search([('organizer_id','=',self.id)])
        pargtner_id.write({
        'name': vals['nom'],
             })
        return super(organisateur, self).write(vals)

    @api.multi
    def unlink(self):
        for x in self:
           
            partner_id=self.env['res.partner'].search([('organizer_id','=',x.id)])
            partner_id.unlink()
        return super(organisateur, self).unlink()