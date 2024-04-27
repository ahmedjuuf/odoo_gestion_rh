from odoo import fields,models

class Contrat(models.Model):
    _name = 'gestion.rh.contrat'
    _description = 'Informations sur les contrats'

    nom = fields.Char(string="Référence du Contrat", required=True)
    type_contrat = fields.Selection([
        ('cdi', 'CDI'),
        ('cdd', 'CDD'),
        ('stage', 'Stage'),
        # Ajoutez d'autres types de contrats selon vos besoins
    ], string="Type de contrat", required=True)
    date_debut = fields.Date(string="Date de début", required=True)
    date_fin = fields.Date(string="Date de fin")
    salaire = fields.Float(string="Salaire")

    #Cles etrangeres
    # employe_id = fields.Many2one('gestion.rh.employe', string="Employé", required=True)