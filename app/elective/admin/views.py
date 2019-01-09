from app.elective.admin import admin_mod

from app.shared.controllers import requires_token
from app.elective.teacher.controllers import get_electives

from flask import g, redirect, url_for, render_template

@admin_mod.before_request
@requires_token
def check_teacher():
    if g.user.get_type_code() != 'ADM':
        return redirect(url_for('elective'))

# TODO: Make admin route a way to update trimester/elective enroll opening/closings
# Admins should be able to look up 
@admin_mod.route('/')
def index():
    return render_template("./elective/admin/index.html", electives=get_electives())