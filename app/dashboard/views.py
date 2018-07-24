from app.dashboard import board_mod
from app.dashboard.controllers import *
from app.shared.controllers import requires_token
from app.auth.controllers import create_token

from config import Config

from flask import render_template, redirect, request, url_for, g
from flask_breadcrumbs import register_breadcrumb

@board_mod.route('/')
@register_breadcrumb(board_mod, '.', 'Dashboard')
@requires_token
def index():
    return render_template("dashboard/dashboard.html")

@board_mod.route('/about')
@register_breadcrumb(board_mod, '.about', 'About')
@requires_token
def about():
    return render_template("dashboard/about.html")

@board_mod.route('/test', methods=['GET', 'POST'])
def test():
    if Config.DEBUG:
        if not request.cookies.get('bca_token'):
            if request.method == 'POST':

                usr_id_tch = request.form["usr_id_tch"]
                usr_id_adm = request.form["usr_id_adm"]
                usr_id_std = request.form["usr_id_std"]

                choice = request.form["choice"]

                if choice == 'Login ADM':
                    g.token =  create_token(usr_id_adm, request.remote_addr)
                elif choice == 'Login TCH':
                    g.token = create_token(usr_id_tch, request.remote_addr)
                    print("created token!")
                elif choice =='Login STD':
                    g.token = create_token(usr_id_std, request.remote_addr)
                else:
                    return redirect("dashboard/test.html", code=400)

            else:
                admins = get_admins()
                teachers = get_teachers()
                students = get_students()
                return render_template("dashboard/test.html", admins=admins, teachers=teachers, students=students)
    return redirect(url_for("dashboard.index"))