from flask import Blueprint

teacher_mod = Blueprint('bakesale_teacher', __name__, url_prefix='/teacher')

import app.bakesale.teacher.views