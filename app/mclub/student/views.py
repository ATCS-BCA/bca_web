from app.mclub.student import student_mod

from app.shared.controllers import requires_token
from app.mclub.student.controllers import *

from flask import g, redirect, url_for, render_template, request, jsonify

# Checks whether the requester
@student_mod.before_request
@requires_token
def check_teacher():
    if g.user.get_role('CLUB') != 'STD':
        return redirect(url_for('mclub'))

# pages

# A route for the student_mod app
@student_mod.route('/')
def index():
    enroll_info = get_enrollment_time(g.user.get_grade_level())

    enrolled_clubs = []
    available_clubs = []

    if not enroll_info.start_time is None:
        all_clubs = get_clubs()
        enrolled_clubs = get_enrolled_clubs(g.user.get_id(), enroll_info.course_year, enroll_info.tri_nbr)

        for club in all_clubs:
            if club.id not in [i.id for i in enrolled_clubs]:
                available_clubs.append(club)

    return render_template("mclub/student/index.html", clubs=available_clubs, enroll_info=enroll_info, enrolled_clubs=enrolled_clubs)


@student_mod.route('/enroll/<int:club_id>', methods=['GET'])
def enroll(club_id):
    if enrollment_open(g.user.get_grade_level()):
        if not is_club_full(club_id):
            usr_id = g.user.get_id()
            enroll_user(usr_id, club_id)

    return redirect(url_for('mclub_student.index'))


@student_mod.route('/drop/<int:club_id>', methods=['GET'])
def drop(club_id):
    usr_id = g.user.get_id()
    drop_club(usr_id, club_id)

    return redirect(url_for('mclub_student.index'))

