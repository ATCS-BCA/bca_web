from app.mclub import mclub_mod

from app.shared.controllers import requires_token

from flask import g, redirect, url_for

@mclub_mod.before_request
@requires_token
def check_auth():
    print("checking token....")

@mclub_mod.route('/')
def index():
    type_code = g.user.get_role('CLUB')

    if type_code == 'STD':
        return redirect(url_for('mclub_student.index'))
    elif type_code == 'TCH':
        return redirect(url_for('mclub_teacher.index'))
    elif type_code == 'ADM':
        return redirect(url_for('mclub_admin.index'))
    else:
        return redirect(url_for('/'))

