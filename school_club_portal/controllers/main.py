from odoo import http
from odoo.http import request

class ClubPortal(http.Controller):

    @http.route('/my/clubs', auth='user', website=True)
    def portal_club_list(self, **kw):
        user = request.env.user
        clubs = request.env['school.club'].search([
            '|',
            ('responsible_id', '=', user.id),
            ('member_ids', 'in', [user.id])
        ])
        return request.render("school_club_portal.portal_club_list", {
            'clubs': clubs
        })

    @http.route('/club/<int:club_id>', auth='user', website=True)
    def portal_club_detail(self, club_id, **kw):
        club = request.env['school.club'].sudo().browse(club_id)
        if club.responsible_id != request.env.user and request.env.user not in club.member_ids:
            return request.not_found()
        return request.render("school_club_portal.portal_club_detail", {
            'club': club
        })

    @http.route('/club/<int:club_id>/join', auth='user', website=True)
    def join_club(self, club_id, **kw):
        club = request.env['school.club'].sudo().browse(club_id)
        if club.exists() and request.env.user not in club.member_ids:
            club.write({'member_ids': [(4, request.env.user.id)]})
        return request.redirect(f'/club/{club_id}')

    @http.route('/club/<int:club_id>/quiz', auth='user', website=True, methods=['GET', 'POST'])
    def take_quiz(self, club_id, **kw):
        club = request.env['school.club'].sudo().browse(club_id)
        if club.responsible_id != request.env.user and request.env.user not in club.member_ids:
            return request.not_found()

        quiz = request.env['school.quiz'].sudo().search([('club_id', '=', club_id)], limit=1)
        if not quiz:
            return request.render('school_club_portal.quiz_no_quiz', {'club': club})

        if request.httprequest.method == 'POST':
            answer = kw.get('answer')
            passed = (answer == quiz.correct_answer)
            request.env['school.quiz'].sudo().create({
                'name': f"Quiz by {request.env.user.name}",
                'club_id': club_id,
                'student_id': request.env.user.id,
                'is_passed': passed,
            })
            return request.render('school_club_portal.quiz_result', {
                'passed': passed,
                'club': club
            })

        return request.render('school_club_portal.quiz_form', {
            'quiz': quiz,
            'club': club
        })

    @http.route('/club/<int:club_id>/content', auth='user', website=True)
    def elearning_content(self, club_id, **kw):
        club = request.env['school.club'].sudo().browse(club_id)
        if club.responsible_id != request.env.user and request.env.user not in club.member_ids:
            return request.not_found()
        contents = request.env['school.elearning.content'].sudo().search([('club_id', '=', club_id)])
        return request.render('school_club_portal.elearning_content_list', {
            'club': club,
            'contents': contents
        })

    @http.route('/club/<int:club_id>/projects', auth='user', website=True)
    def club_projects(self, club_id, **kw):
        club = request.env['school.club'].sudo().browse(club_id)
        if club.responsible_id != request.env.user and request.env.user not in club.member_ids:
            return request.not_found()
        projects = request.env['school.club.project'].sudo().search([('club_id', '=', club_id)])
        return request.render('school_club_portal.project_list', {
            'club': club,
            'projects': projects
        })