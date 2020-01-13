from app.elective import elective_mod

from app.shared.controllers import requires_token

from flask import g, redirect, url_for


@elective_mod.before_request
@requires_token
def check_auth():
    print("checking token....")

@elective_mod.route('/')
def index():
    type_code = g.user.get_role('ELEN')

    if type_code == 'STD':
        return redirect(url_for('bakesale_student.index'))
    elif type_code == 'TCH':
        return redirect(url_for('bakesale_teacher.index'))
    elif type_code == 'ADM':
        return redirect(url_for('bakesale_admin.index'))
    else:
        return redirect('/')
