from odoo import fields,models

class NoteFrais(models.Model):
    _name = 'gestion.rh.notefrais'
    _description = 'Gestion des notes de frais'

    montant = fields.Float(string="Montant", required=True)
    date = fields.Date(string="Date", required=True)
    description = fields.Text(string="Description")
    statut = fields.Selection([
        ('soumis', 'Soumis'),
        ('approuve', 'Approuvé'),
        ('rembourse', 'Remboursé'),
    ], string="Statut")
    commentaire_approbateur = fields.Text(string="Commentaire de l'Approbateur")


    #Cardinalite
    # employe_id = fields.Many2one('gestion.rh.employe', string="Employé")