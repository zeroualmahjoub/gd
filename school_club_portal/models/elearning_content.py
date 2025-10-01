from odoo import models, fields

class ElearningContent(models.Model):
    _name = 'school.elearning.content'
    _description = 'E-Learning Content'

    name = fields.Char(required=True)
    club_id = fields.Many2one('school.club', required=True, ondelete='cascade')
    content_type = fields.Selection([
        ('video', 'Video'),
        ('document', 'Document'),
        ('text', 'Text')
    ], required=True)
    url = fields.Char(string="URL or File Path")
    description = fields.Text()
    quiz_id = fields.Many2one('school.quiz', string="Associated Quiz")