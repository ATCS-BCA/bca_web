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
    return render_template("mclub/teacher/index.html", clubs=get_clubs(g.user.get_id()), proposals=get_proposals())


@teacher_mod.route('/edit/<int:club_id>', methods=['GET', 'POST'])
def edit(club_id):
    club = get_club(club_id)

    # actually making changes
    if request.method == 'POST':
        name = request.form['club_name']
        room_nbr = request.form['club_room_nbr']
        max_nbr = request.form['club_max_nbr', None]
        day = request.form['club_day', None]
        description = request.form['club_desc', None]

        exit()
        edit_club(club_id, name, day, room_nbr, description, max_nbr)
        # return render_template("mclub/teacher/index.html", clubs=get_clubs(), proposals=get_proposals())
        return redirect(url_for('mclub_teacher.index'))

    return render_template("mclub/teacher/edit.html", club=club)
