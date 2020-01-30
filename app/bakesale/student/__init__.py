from flask import Blueprint

student_mod = Blueprint('bakesale_student', __name__, url_prefix='/student')

import app.bakesale.student.views