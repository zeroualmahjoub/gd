from odoo import models, fields

class SchoolBadge(models.Model):
    _name = 'school.badge'
    _description = 'Achievement Badge'

    name = fields.Char(required=True)
    description = fields.Text()
    image = fields.Binary("Badge Image")
    student_id = fields.Many2one('res.users', string="Student")
    club_id = fields.Many2one('school.club', string="Club")