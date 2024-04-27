from odoo import fields,models

class Conge(models.Model):
    _name = 'gestion.rh.conge'
    _description = 'Informations sur les congés'

    type_conge = fields.Selection([
        ('paye', 'Congé payé'),
        ('maladie', 'Congé maladie'),
        ('maternite','Conge de maternite')
    ], string="Type de congé", required=True)
    
    description = fields.Text(string="Description")
    statut_conge = fields.Selection([
        ('soumis', 'Soumis'),
        ('approuve', 'Approuvé'),
        ('refuse', 'Refusé'),
    ], string="Statut du Congé")
    est_paye = fields.Boolean(string="Est Payé")
    justificatif = fields.Binary(string="Justificatif")
    date_debut = fields.Date(string="Date de début", required=True)
    date_fin = fields.Date(string="Date de fin", required=True)
