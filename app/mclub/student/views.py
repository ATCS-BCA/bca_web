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

