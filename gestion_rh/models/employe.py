from odoo import fields,models

class Employe(models.Model):
    _name = 'gestion.rh.employe'
    _description = 'Informations sur les employés'

    nom = fields.Char(string="Nom", required=True)
    prenom = fields.Char(string="Prénom", required=True)
    date_naissance = fields.Date(string="Date de Naissance")
    adresse = fields.Char(string="Adresse")
    email_professionnel = fields.Char(string="Email Professionnel")
    telephone = fields.Char(string="Téléphone")
    genre = fields.Selection([
        ('homme', 'Homme'),
        ('femme', 'Femme'),
    ], string="Genre")
    date_embauche = fields.Date(string="Date d'Embauche")

    # Cles etrangeres
    # notefrais_ids = fields.One2many('gestion.rh.notefrais', 'gestion.rh.employe', string="Notes de Frais")
    # departement_id = fields.Many2one('gestion.rh.departement', string="Département")
    # contrat_ids = fields.One2many('gestion.rh.contrat', 'gestion.rh.employe', string="Contrats")
    # conge_ids = fields.One2many('gestion.rh.conge', 'gestion.rh.employe', string="Congés")
    # projet_ids = fields.Many2many('gestion.rh.projet', string="Projets")
    # notefrais_ids = fields.One2many('gestion.rh.notefrais', 'gestion.rh.employe', string="Notes de Frais")
    # poste_id = fields.Many2one('gestion.rh.poste', string="Poste")
