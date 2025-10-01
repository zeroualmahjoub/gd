from odoo import models, fields

class ClubProject(models.Model):
    _name = 'school.club.project'
    _description = 'Club Project'

    name = fields.Char(required=True)
    club_id = fields.Many2one('school.club', required=True, ondelete='cascade')
    description = fields.Text()
    start_date = fields.Date()
    end_date = fields.Date()
    task_ids = fields.One2many('school.club.task', 'project_id', string="Tasks")