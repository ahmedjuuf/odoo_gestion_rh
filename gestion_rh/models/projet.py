from odoo import fields,models

class Projet(models.Model):
    _name = 'gestion.rh.projet'
    _description = 'Informations sur les projets'

    nom = fields.Char(string="Nom du projet", required=True)
    description = fields.Text(string="Description")
    date_debut = fields.Date(string="Date de début")
    date_fin = fields.Date(string="Date de fin")
    budget = fields.Float(string="Budget")
    statut = fields.Selection([
        ('en_cours', 'En cours'),
        ('termine', 'Terminé'),
        ('en_attente', 'En attente'),
    ], string="Statut")

    # Les cardinalites
    # responsable_id = fields.Many2one('gestion.rh.employe', string="Responsable du Projet")
