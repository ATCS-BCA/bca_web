from app.shared.models import NestableBlueprint

mclub_mod = NestableBlueprint('mclub', __name__, url_prefix='/morning_clubs')

import app.mclub.views

from .admin import admin_mod
from .teacher import teacher_mod
# from .student import student_mod

mclub_mod.register_blueprint(admin_mod)
mclub_mod.register_blueprint(teacher_mod)
# mclub_mod.register_blueprint(student_mod)
