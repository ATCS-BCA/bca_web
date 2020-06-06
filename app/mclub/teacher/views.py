from app.mclub.teacher import teacher_mod

from app.shared.controllers import requires_token
from app.mclub.teacher.controllers import *

from flask import g, redirect, url_for, render_template, request, jsonify, make_response
from flask_breadcrumbs import register_breadcrumb

@teacher_mod.before_request
@requires_token
def check_teacher():
    pass
    #if g.user.get_role('CLUB') != 'ADM':
       # return redirect(url_for('mclub.index'))

@teacher_mod.route('/')
@register_breadcrumb(teacher_mod, ".", "Clubs")
def index():
    return render_template("mclub/teacher/index.html", clubs=get_clubs(g.user.get_id()))


@teacher_mod.route('/add', methods=['GET', 'POST'])
@register_breadcrumb(teacher_mod, ".add", "Add Club")
def add():
    if request.method == 'POST':
        # is there a difference between request.form['field'] and request.form.get('field', None')
        club_name = request.form['club_name']
        club_max_nbr = request.form['club_max_nbr']
        club_type_cde = request.form.get('club_type_cde')
        club_room_nbr = request.form['club_room_nbr']
        club_desc = request.form['club_desc']

        if club_name and club_max_nbr and club_type_cde and club_room_nbr and club_desc:
            add_club(club_name, club_max_nbr, club_type_cde, club_room_nbr, club_desc, g.user.get_id(),
                     get_type_name(club_type_cde))

        return render_template("mclub/teacher/index.html", clubs=get_clubs(g.user.get_id()))

    return render_template("mclub/teacher/add.html", days=get_club_days())


@teacher_mod.route('/rosters/<int:id>', methods=['GET', 'POST'])
@register_breadcrumb(teacher_mod, ".rosters", "Student Roster")
def rosters(id):
    return render_template("mclub/teacher/rosters.html", students=get_club_students(id))

# also have to take into account the security issue of "verify this user can make changes to this club"
@teacher_mod.route('/edit/<int:id>', methods=['GET', 'POST'])
@register_breadcrumb(teacher_mod, ".edit", "Edit Club")
def edit(id):
    club = get_club(id)

    # actually making changes
    if club:
        if request.method == 'POST':
            name = request.form.get('club_name', None)
            room_nbr = request.form.get('club_room_nbr', None)
            max_nbr = request.form.get('club_max_nbr', None)
            type_cde = request.form.get('club_day', None)
            description = request.form.get('club_desc', None)

            if name or room_nbr or max_nbr or type_cde or description:
                edit_club(id, name, get_type_name(type_cde), room_nbr, description, max_nbr, type_cde)

            # send back to the index page after making changes
            return render_template("mclub/teacher/index.html", clubs=get_clubs(g.user.get_id()))

        else:
            # if simply trying to see the edit page, not submitting changes
            return render_template("mclub/teacher/edit.html", club=club, days=get_club_days())

    else:  # error w/ the club
        redirect(url_for('mclub_teacher.index'))
