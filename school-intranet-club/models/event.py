from odoo import models, fields

class SchoolEvent(models.Model):
    _name = 'school.event'
    _description = "Événement / Séminaire"

    name = fields.Char(required=True)
    date = fields.Datetime(string="Date de l'événement")
    description = fields.Text()
    google_meet_link = fields.Char(string="Lien Google Meet")
    club_ids = fields.Many2many('school.club', string="Clubs invités")
