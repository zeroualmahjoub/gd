from odoo import models, fields, api

class SchoolQuiz(models.Model):
    _name = 'school.quiz'
    _description = 'Simple Quiz'

    name = fields.Char(required=True)
    club_id = fields.Many2one('school.club', required=True)
    question = fields.Text(required=True)
    option_a = fields.Char("Option A", required=True)
    option_b = fields.Char("Option B", required=True)
    option_c = fields.Char("Option C")
    option_d = fields.Char("Option D")
    correct_answer = fields.Selection([
        ('a', 'A'), ('b', 'B'), ('c', 'C'), ('d', 'D')
    ], required=True)
    student_id = fields.Many2one('res.users', string="Student")
    is_passed = fields.Boolean("Passed")

    @api.model
    def create(self, vals):
        record = super(SchoolQuiz, self).create(vals)
        if record.is_passed and record.student_id and record.club_id:
            badge_name = f"Badge - {record.name}"
            self.env['school.badge'].create({
                'name': badge_name,
                'student_id': record.student_id.id,
                'club_id': record.club_id.id,
                'description': f"Successfully passed the quiz: {record.name}",
            })
        return record