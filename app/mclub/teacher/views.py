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


@teacher_mod.route('/add', methods=['GET', 'POST'])
def add_club():
    if request.method == 'POST':
        # is there a difference between request.form['field'] and request.form.get('field', None')
        club_name = request.form['club_name']
        club_max_nbr = request.form['club_max_nbr']
        club_day = request.form['club_day']  # this might be a misnomer b/c it's more like meeting time than day
        club_room_nbr = request.form['club_room_nbr']
        club_desc = request.form['club_desc']

        if club_name and club_max_nbr and club_day and club_room_nbr and club_desc:
            add_club(club_name, club_max_nbr, club_day, club_room_nbr, club_desc, g.user.get_id())

        return url_for('mclub_teacher.index')

    return render_template("mclub/teacher/add.html")


@teacher_mod.route('/rosters/<int:id>', methods=['GET', 'POST'])
def rosters(id):
    return render_template("mclub/teacher/rosters.html")


@teacher_mod.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    club = get_club(id)

    # actually making changes
    if club:
        if request.method == 'POST':
            name = request.form.get('club_name', None)
            room_nbr = request.form.get('club_room_nbr', None)
            max_nbr = request.form.get('club_max_nbr', None)
            day = request.form.get('club_day', None)
            description = request.form.get('club_desc', None)

            if name or room_nbr or max_nbr or day or description:
                edit_club(id, name, day, room_nbr, description, max_nbr)

            # send back to the index page after making changes
            return render_template("mclub/teacher/index.html", clubs=get_clubs(g.user.get_id()),
                                   proposals=get_proposals())

        else:
            # if simply trying to see the edit page, not submitting changes
            return render_template("mclub/teacher/edit.html", club=club)

    else:  # error w/ the club
        redirect(url_for('mclub_teacher.index'))
