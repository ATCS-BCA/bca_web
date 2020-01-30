from app.shared.models import NestableBlueprint

bakesale_mod = NestableBlueprint('bakesale', __name__, url_prefix='/bakesale_register')

import app.elective.views

from .admin import admin_mod
from .teacher import teacher_mod
from .student import student_mod

bakesale_mod.register_blueprint(admin_mod)
bakesale_mod.register_blueprint(teacher_mod)
bakesale_mod.register_blueprint(student_mod)
