from flask import Blueprint

teacher_mod = Blueprint('mclub_teacher', __name__, url_prefix='/teacher')

import app.mclub.teacher.views