from odoo import models, fields

class SchoolProject(models.Model):
    _name = 'school.project'
    _description = "Projet de club"

    name = fields.Char(required=True)
    description = fields.Text()
    club_id = fields.Many2one('school.club', string='Club')
    start_date = fields.Date(string="Date de début")
    end_date = fields.Date(string="Date de fin")
    status = fields.Selection([
        ('draft', 'Brouillon'),
        ('ongoing', 'En cours'),
        ('done', 'Terminé')
    ], default='draft')
