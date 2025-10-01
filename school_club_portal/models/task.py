from odoo import models, fields

class ClubTask(models.Model):
    _name = 'school.club.task'
    _description = 'Club Task'

    name = fields.Char(required=True)
    project_id = fields.Many2one('school.club.project', required=True, ondelete='cascade')
    assigned_to_ids = fields.Many2many('res.users', string="Assigned Students")
    state = fields.Selection([
        ('todo', 'To Do'),
        ('in_progress', 'In Progress'),
        ('done', 'Done')
    ], default='todo')
    description = fields.Text()