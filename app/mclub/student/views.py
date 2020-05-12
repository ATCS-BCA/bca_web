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
        enrolled_clubs = get_enrolled_clubs(g.user.get_id(), enroll_info.course_year, enroll_info.tri_nbr)
        available_clubs = get_clubs()

    return render_template("mclub/student/index.html", clubs=available_clubs, enroll_info=enroll_info, enrolled_clubs=enrolled_clubs)


@student_mod.route('/enroll/<int:id>', methods=['PUT'])
def enroll(id):
    data = wrequest.get_json(force=True, silent=True)

    club_id = id
    usr_id = data['usr_id']
    will_enroll = data['enroll']

    if enrollment_open(g.user.get_grade_level()):
        if will_enroll:
            if not is_club_full(club_id):
                enroll_user(usr_id, club_id)

                return jsonify({"has_enrolled": True, "Error": None})

            else:
                return jsonify({"has_enrolled": False, "Error": "Club Full."})
        else:
            drop_club(usr_id, club_id)
            return jsonify({"has_enrolled": False, "Error": None})

    else:
        return jsonify({"has_enrolled": False, "Error": "Enrollment Not Open"})


@student_mod.route('/enroll/update', methods=['PUT'])
def ping():
    data = request.get_json(force=True, silent=True)

    club_ids = data['club_ids']

    if(club_ids):

        amount_left = {}

        for i in range(len(club_ids)):
            amount_left[club_ids[i]] = get_amount_left(club_ids[i])

        return jsonify(amount_left)

    else:
        return jsonify({"Error": "Invalid parameters"})