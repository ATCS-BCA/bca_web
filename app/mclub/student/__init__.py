from flask import Blueprint

student_mod = Blueprint('mclub_student', __name__, url_prefix='/student')

import app.mclub.student.views