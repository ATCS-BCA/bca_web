from app.elective.teacher import teacher_mod
from app.elective.teacher.controllers import *

from app.shared.controllers import requires_token

from flask_breadcrumbs import register_breadcrumb

from flask import g, redirect, render_template, request, url_for, jsonify

import collections

@teacher_mod.before_request
@requires_token
def check_teacher():
    if g.user.get_type_code() != 'TCH':
        return redirect('elective')

# pages

@teacher_mod.route('/')
@register_breadcrumb(teacher_mod, ".", "Elective Enroll")
def index():
    return render_template("elective/teacher/index.html", sections=get_sections(g.user.get_id()))

@teacher_mod.route('/create', methods=['GET', 'POST'])
@register_breadcrumb(teacher_mod, ".create", "Create Elective")
def create():
    if request.method == 'POST':
        elective_name = request.form['elective_name']
        elective_desc = request.form['elective_desc']

        sections = request.form.getlist('section_time')
        section_room_nbr = request.form.getlist('section_room_nbr')
        section_year = request.form.getlist('section_year')
        section_tri = request.form.getlist('section_tri')


        if elective_name and elective_desc and sections and section_room_nbr and section_year and section_tri:
            elective_id = create_elective(elective_name, elective_desc)

            if isinstance(sections, collections.Iterable):
                add_sections(elective_id, g.user.get_id(), sections, section_room_nbr, section_year, section_tri)
            else:
                add_section(elective_id, g.user.get_id(), sections, section_room_nbr, section_year, section_tri)

            return redirect(url_for('elective_teacher.index'))

    return render_template("elective/teacher/create.html", electives=get_sections(g.user.get_id()))

@teacher_mod.route('/edit/<int:id>/section/', methods=['GET', 'POST', 'DELETE'])
def section(id):
    data = request.get_json(force=True, silent=True)

    if request.method == 'POST':
        section_time = data['section_time']
        section_year = data['section_year']
        section_tri = data['section_tri']
        section_room_nbr = data['section_room_nbr']

        if section_time and section_year and section_tri and section_room_nbr:
            add_section(id, g.user.get_id(), section_time, section_room_nbr, section_year, section_tri)
            return jsonify({"Info": True})

        return jsonify({"Info": False})

    elif request.method == 'DELETE':

        section_id = data['section_id']

        if delete_section(g.user.get_id(), section_id):
            return jsonify({"Info": "Successfully deleted Section"}), 200

        return jsonify({"Info": "You don't have permission to delete this elective!"}), 403
    return jsonify({"error": "Invalid route"})

@teacher_mod.route('/edit/<int:elective_id>/section/<int:section_id>/students', methods=['GET', 'POST', 'DELETE'])
def edit_students(elective_id, section_id):
    if request.method == 'POST':
        data = request.form
        if 'usr_id' in data and 'action' in data:
            usr_id = data['usr_id']
            action = data['action']

            if action.lower() == 'add':
                add_student(section_id, usr_id)
            elif action.lower() == 'delete':
                remove_student(section_id, usr_id)

    section_students = get_section_students(section_id)
    ids = [x.id for x in section_students]

    return render_template("elective/teacher/students.html", elective_students=section_students, global_students=get_students(ids))

@teacher_mod.route('/electives', methods=['GET'])
def query_elective():
    return render_template("elective/teacher/electives.html", electives=get_electives())

@teacher_mod.route('/edit/<int:id>', methods=['GET', 'POST'])
@register_breadcrumb(teacher_mod, ".edit", "Edit Elective")
def edit(id):
    elective = get_elective(id)

    if elective:
        return render_template("elective/teacher/edit.html", elective=elective)
    else:
        return redirect(url_for('elective_teacher.index'))