from app.mclub.teacher import teacher_mod

from app.shared.controllers import requires_token
from app.mclub.teacher.controllers import *

from flask import g, redirect, url_for, render_template, request, jsonify, make_response

@teacher_mod.before_request
@requires_token
def check_teacher():
    pass
    #if g.user.get_role('CLUB') != 'ADM':
       # return redirect(url_for('mclub.index'))

@teacher_mod.route('/')
def index():
    return render_template("mclub/teacher/index.html", clubs=get_clubs(), proposals=get_proposals())


@teacher_mod.route('/edit/<int:id>', methods=['GET', 'POST'])
# breadcrumbs?
def edit(id):
    club = get_club(id)

    if club:
        if request.method == 'POST':
            name = request.form.get('club_name', None)
            room_nbr = request.form.get('club_room_nbr', None)
            max_nbr = request.form.get('club_max_nbr', None)
            day = request.form.get('club_day', None)
            description = request.form.get('club_desc', None)

            if name or room_nbr or max_nbr or day or description:
                edit_club(id, name, day, room_nbr, description, max_nbr)

            # send back to the index page
            return render_template("mclub/teacher/index.html", clubs=get_clubs(), proposals=get_proposals())

        else:
            # if simply trying to see the edit page, not submitting changes
            return render_template("mclub/teacher/edit.html", club=club)

    else:  # error w/ the club
        redirect(url_for('mclub_teacher.index'))
