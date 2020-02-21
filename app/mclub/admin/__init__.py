from flask import Blueprint

admin_mod = Blueprint('mclub_admin', __name__, url_prefix='/admin')

import app.mclub.admin.views