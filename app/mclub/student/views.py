from app.mclub.student import student_mod

from app.shared.controllers import requires_token
from app.mclub.student.controllers import *

from flask import g, redirect, url_for, render_template, request, jsonify, make_response

@student_mod.before_request
@requires_token
def check_teacher():
    pass
    #if g.user.get_role('CLUB') != 'ADM':
    #  return redirect(url_for('mclub.index'))

@student_mod.route('/')
def index():
    return render_template("mclub/student/index.html", clubs=get_clubs())
# i changed get_clubs() so that it takes a parameter user_id (which is g.user.get_id() )
# so if you wanna get the student's id, use that method and if you wanna get their clubs, pass that into get_clubs()
