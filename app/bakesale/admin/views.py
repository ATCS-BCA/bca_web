from app.bakesale.admin import admin_mod

from app.shared.controllers import requires_token
from app.bakesale.admin.controllers import *

from flask import g, redirect, url_for, render_template, request, jsonify

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
@admin_mod.before_request
@requires_token
def check_admin():
    if g.user.get_role('BAKE') != 'ADM':
        return redirect(url_for('bakesale'))

# pages

# A route for the student_mod app
@admin_mod.route('/')
def index():
    return render_template("bakesale/admin/index.html", bakesales=get_requested_bakesales())

@admin_mod.route('/confirm', methods=["GET", "POST"])
def confirm():
    data = request.get_json(force=True, silent=True)
    bakesale_id = data["bakesale_id"]
    if data["confirmed"]:
        status_code = "A"
    else:
        status_code = "D"
    query(DB.BAKESALE, "update bakesale set status_code = '" + status_code + "' where bakesale_id = " + bakesale_id)

@admin_mod.route('/set_date', methods=["GET", "POST"])
def set_date():
    data = request.get_json(force=True, silent=True)
    bakesale_id = data["bakesale_id"]
    date = data["date"]

    query(DB.BAKESALE, "update bakesale set date = " + date + " where bakesale_id = " + bakesale_id)
