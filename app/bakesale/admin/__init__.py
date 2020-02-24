from flask import Blueprint

admin_mod = Blueprint('bakesale_admin', __name__, url_prefix='/admin')

import app.bakesale.student.views