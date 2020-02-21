from app.mclub.admin import admin_mod

from app.shared.controllers import requires_token

from flask import g, redirect, url_for, render_template, request, jsonify, make_response

@admin_mod.before_request
@requires_token
def check_teacher():
    pass
    # if g.user.get_role('CLUB') != 'ADM':
        # return redirect(url_for('mclub.index'))

@admin_mod.route('/')
def index():
    return render_template("./mclub/admin/index.html")

