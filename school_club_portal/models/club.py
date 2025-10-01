from odoo import models, fields

class SchoolClub(models.Model):
    _name = 'school.club'
    _description = 'School Club'

    name = fields.Char(string="Club Name", required=True)
    description = fields.Text()
    responsible_id = fields.Many2one('res.users', string="Responsible Teacher", required=True)
    member_ids = fields.Many2many('res.users', string="Students")
    project_ids = fields.One2many('school.club.project', 'club_id', string="Projects")
    content_ids = fields.One2many('school.elearning.content', 'club_id', string="E-Learning Content")