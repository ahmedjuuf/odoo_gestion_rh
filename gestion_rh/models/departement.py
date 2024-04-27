from odoo import fields,models

class Departement(models.Model):
    _name = 'gestion.rh.departement'
    _description = 'Informations sur les départements'

    name = fields.Char(string="Nom du département", required=True)
    localisation = fields.Char(string="Localisation")
    budget_annuel = fields.Float(string="Budget Annuel")
    numero_telephone = fields.Char(string="Numéro de Téléphone")
    email_contact = fields.Char(string="Email de Contact")
    description = fields.Char(string="Description")

    #Cles etrangeres
    manager_id = fields.Many2one('gestion.rh.employe', string="Responsable")
    # employe_ids = fields.One2many('gestion.rh.employe', 'gestion.rh.departement', string="Employés")

