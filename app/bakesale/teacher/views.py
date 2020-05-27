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
@register_breadcrumb(teacher_mod, ".", "Bakesales")
def index():
    return render_template("bakesale/teacher/index.html", bakesales=get_all_bakesales(), teacher_bakesales=get_teacher_bakesales(g.user.get_id()))

@teacher_mod.route('/create', methods=['GET', 'POST'])
@register_breadcrumb(teacher_mod, ".create", "Request Bakesale")
def create():
    if request.method == 'POST':
        group_name = request.form['group_name']
        group_size = request.form['group_size']
        requested_day = request.form['requested_day']
        items_desc = request.form.get('items_desc', None)

        if group_name and group_size and requested_day and items_desc:
            create_bakesale(group_name, group_size, items_desc, requested_day, g.user.get_id())

            return redirect(url_for('bakesale_teacher.index'))

    return render_template("bakesale/teacher/create.html", teacher_bakesales=get_teacher_bakesales(g.user.get_id()))

@teacher_mod.route('/edit/<int:bakesale_id>', methods=['GET', 'POST'])
@register_breadcrumb(teacher_mod, ".edit", "Edit Bakesale")
def edit(bakesale_id):
    # bakesale_id = request.form['bakesale_id']
    bakesale = get_bakesale(bakesale_id)

    if request.method == 'POST':
        group_name = request.form['group_name']
        group_size = request.form['group_size']
        requested_day = request.form['requested_day']
        items_desc = request.form.get('items_desc', None)

        if group_name and group_size and requested_day and items_desc:
            edit_bakesale(bakesale_id, group_name, group_size, items_desc, requested_day)
            return redirect(url_for('bakesale_teacher.index'))

    return render_template("bakesale/teacher/edit.html", bakesale=bakesale)
