from app.mclub.admin import admin_mod

from app.shared.controllers import requires_token
from app.mclub.student.controllers import get_wed_clubs, get_mrng_clubs
from app.mclub.admin.controllers import get_signup_dates, update_enroll_date

from flask import g, redirect, url_for, render_template, request, jsonify, make_response
from flask_breadcrumbs import register_breadcrumb


@admin_mod.before_request
@requires_token
def check_teacher():
    # if g.user.get_role('CLUB') != 'ADM':
    #   return redirect(url_for('mclub'))
    pass

@admin_mod.route('/')
@register_breadcrumb(admin_mod, ".", "Clubs")
def index():
    wednesday_clubs = get_wed_clubs()
    morning_clubs = get_mrng_clubs()

    return render_template("./mclub/admin/index.html", wednesday_clubs=wednesday_clubs, morning_clubs=morning_clubs)

@admin_mod.route('/signup_dates')
@register_breadcrumb(admin_mod, ".signup_dates", "Signup Dates")
def signup_dates():
    return render_template("./mclub/admin/signup_dates.html", dates=get_signup_dates())


@admin_mod.route('/signup_dates', methods=['GET','POST'])
@register_breadcrumb(admin_mod, ".signup_Dates", "Signup Dates")
def update_dates():
    data = request.get_json(force=True, silent=True)

    if request.method == 'POST':
        grades = data['grades']

        if len(grades) > 0:

            for grade in grades:

                grade_lvl = grade
                tri_nbr = grades[grade]['tri_nbr']
                course_year = grades[grade]['course_year']
                start = grades[grade]['start']
                end = grades[grade]['end']

                update_enroll_date(grade_lvl, tri_nbr, course_year, start, end)

    return redirect(url_for('mclub_admin.index'))

