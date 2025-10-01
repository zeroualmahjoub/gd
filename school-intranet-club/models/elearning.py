from odoo import models, fields

class SchoolElearning(models.Model):
    _name = 'school.elearning'
    _description = "Contenu eLearning"

    name = fields.Char(required=True)
    description = fields.Text()
    file = fields.Binary(string='Fichier')
    file_name = fields.Char()
    club_id = fields.Many2one('school.club', string='Club')
