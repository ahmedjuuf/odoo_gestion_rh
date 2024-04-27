from odoo import fields,models

class Poste(models.Model):
    _name = 'gestion.rh.poste'
    _description = 'Informations sur les postes'

    nom = fields.Char(string="Intitulé du poste", required=True)
    description = fields.Text(string="Description")
    statut = fields.Selection([
        ('ouvert', 'Ouvert'),
        ('ferme', 'Fermé'),
        ('attente', 'En attente')
    ], string="Statut")
    avantages = fields.Text(string="Avantages")
    competences_requises = fields.Text(string="Compétences Requises")
    experience_requise = fields.Integer(string="Expérience Requise")
    formation_requise = fields.Char(string="Formation")

    # employe_ids = fields.One2many('gestion.rh.employe', 'gestion.rh.poste', string="Employés")
