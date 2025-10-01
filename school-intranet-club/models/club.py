from odoo import models, fields

class SchoolClub(models.Model):
    _name = 'school.club'
    _description = 'Club scolaire'

    name = fields.Char(required=True)
    ville = fields.Selection([
        ('safi', 'Safi'),
        ('rabat', 'Rabat'),
        ('casa', 'Casablanca'),
        ('marrakech', 'Marrakech')
    ], required=True)
    niveau = fields.Selection([
        ('college', 'Collège'),
        ('lycee', 'Lycée')
    ], required=True)
    responsable_id = fields.Many2one('res.users', string='Responsable')
    student_ids = fields.One2many('school.student', 'club_id', string='Élèves')
    project_ids = fields.One2many('school.project', 'club_id', string='Projets')
    content_ids = fields.One2many('school.elearning', 'club_id', string='Contenus pédagogiques')
