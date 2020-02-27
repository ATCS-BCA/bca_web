from flask import Blueprint

student_mod = Blueprint('bakesale_teacher', __name__, url_prefix='/teacher')

import app.bakesale.teacher.views