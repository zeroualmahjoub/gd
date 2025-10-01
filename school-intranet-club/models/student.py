from odoo import models, fields

class SchoolStudent(models.Model):
    _name = 'school.student'
    _description = "Élève"

    name = fields.Char(required=True)
    email = fields.Char()
    user_id = fields.Many2one('res.users', string="Compte utilisateur")
    club_id = fields.Many2one('school.club', string='Club')
