from app.bakesale.teacher import teacher_mod

from app.shared.controllers import requires_token
from app.bakesale.teacher.controllers import *

from flask import g, redirect, url_for, render_template, request, jsonify
from flask_breadcrumbs import register_breadcrumb

# Explanation:
# This file is a sub app for the elective enroll application
# It is specified for students
# Only students can view these pages
# The First Route Below makes sure that the requester of this app, student_mod, is a student
# If not, the user is redirected to the index page of the 'elective' app itself
# The name of this app is elective_student
# Every individual app on flask has its own name
# Its sub apps have the name '%PRIMARY_APP_NAME%_%SUB_APP_NAME%'
# These names are useful because they can be used to get urls of routes
# For example, url_for('elective.index') would return the route with the function named index

# Checks whether the requester
@teacher_mod.before_request
@requires_token
def check_teacher():
    if g.user.get_role('BAKE') != 'TCH':
        return redirect(url_for('bakesale'))

# pages

# A route for the teacher_mod app
@teacher_mod.route('/')
def index():
    return render_template("bakesale/teacher/index.html", bakesales=get_all_bakesales(), teacher_bakesales=get_teacher_bakesales(14))

@teacher_mod.route('/create', methods=['GET', 'POST'])
@register_breadcrumb(teacher_mod, ".create", "Create Bakesale")
def create():
    if request.method == 'POST':
        group_name = request.form['group_name']
        group_size = request.form['group_size']
        requested_day = request.form['requested_day']
        items_desc = request.form.get('items_desc', None)

        if group_name and group_size and requested_day and items_desc:
            elective_id = create_elective(elective_name, elective_desc, elective_course_id, elective_prereq)

            if isinstance(sections, collections.Iterable):
                add_sections(elective_id, g.user.get_id(), sections, section_room_nbr, section_year, section_tri)
            else:
                add_section(elective_id, g.user.get_id(), sections, section_room_nbr, section_year, section_tri)

            return redirect(url_for('elective_teacher.index'))

    return render_template("elective/teacher/create.html", electives=get_sections(g.user.get_id()))
