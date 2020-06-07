from app.db import DB, insert, insertmany, query_one, query, delete, update

from app.mclub.student.models import Club, EnrollmentTime

from config import Config
from .util import datetime_from_string, us_format

from datetime import datetime

# Make Query to DB to check whether enrollment is open for grade level
def get_enrollment_time(grade_level):
    result = query_one(DB.CLUBS, "SELECT grade_lvl, start, end, course_year, tri_nbr "
                                 "FROM signup_dates t "
                                 "WHERE t.grade_lvl = %s "
                                 "AND NOW() >= t.start "
                                 "AND NOW() < t.end", [grade_level])
    if result:

        start_time = result[1]
        end_time = result[2]

        return EnrollmentTime(result[0], start_time, end_time, result[3], result[4])
    else:
        return EnrollmentTime(grade_level, None, None, get_current_year(), '-1')

def enrollment_open(grade_level):
    result = query_one(DB.CLUBS, "SELECT * "
                                  "FROM signup_dates t "
                                  "WHERE t.grade_lvl = %s "
                                  "AND NOW() >= t.start "
                                  "AND NOW() <= t.end", [grade_level])

    return (not result is None)


# Enroll a user in a club
def enroll_user(usr_id, club_id):
    print(usr_id, club_id)
    insert(DB.CLUBS, 'INSERT INTO club_user_xref (club_id, usr_id) VALUES (%s, %s) '
                        'ON DUPLICATE KEY UPDATE club_id=club_id', [club_id, usr_id])

    enrollment_count = query_one(DB.CLUBS, "SELECT enrollment_count "
                                     "FROM club "
                                     "WHERE club_id = %s", club_id)

    query = "UPDATE club SET enrollment_count = %s WHERE club_id = %s"
    params = [enrollment_count[0] + 1, club_id]
    update(DB.CLUBS, query, params)



# Remove a user from a club
def drop_club(usr_id, club_id):
    delete(DB.CLUBS, 'DELETE FROM club_user_xref WHERE usr_id=%s AND club_id=%s', [usr_id, club_id])

    enrollment_count = query_one(DB.CLUBS, "SELECT enrollment_count "
                                           "FROM club "
                                           "WHERE club_id = %s", club_id)

    query = "UPDATE club SET enrollment_count = %s WHERE club_id = %s"
    params = [enrollment_count[0] - 1, club_id]
    update(DB.CLUBS, query, params)


# Returns whether a club is full
def is_club_full(club_id):
    club_info = query_one(DB.CLUBS, "SELECT enrollment_count, max_nbr "
                                     "FROM club "
                                     "WHERE club_id = %s", club_id)

    return club_info[0] >= club_info[1]


def get_wed_clubs():
    clubs = query(DB.CLUBS, "SELECT club_id, name, advisor_id, day, room_nbr, description, max_nbr, enrollment_count"
                                        " FROM club " 
                                        "WHERE club_type_cde = 3 " # Displaying only Wednesday Afternoon Clubs
                                        "order by club_id")

    all_clubs = []

    for club in clubs:

        club_id = club[0]
        club_name = club[1]
        club_advisor_id = club[2]
        club_day = club[3]
        club_room_nbr = club[4]
        club_desc = club[5]
        club_max_nbr = club[6]
        club_enrollment_count = club[7]

        c = Club(club_name, club_day, club_id, club_desc, club_max_nbr, club_room_nbr, club_enrollment_count)

        all_clubs.append(c)

    return all_clubs

def get_mrng_clubs():
    clubs = query(DB.CLUBS, "SELECT club_id, name, advisor_id, day, room_nbr, description, max_nbr, enrollment_count"
                                        " FROM club " 
                                        "WHERE club_type_cde <> 3" # Displaying morning clubs (Excluding Wednesday Clubs)
                                         " order by club_id")

    all_clubs = []

    for club in clubs:

        club_id = club[0]
        club_name = club[1]
        club_advisor_id = club[2]
        club_day = club[3]
        club_room_nbr = club[4]
        club_desc = club[5]
        club_max_nbr = club[6]
        club_enrollment_count = club[7]

        c = Club(club_name, club_day, club_id, club_desc, club_max_nbr, club_room_nbr, club_enrollment_count)

        all_clubs.append(c)

    return all_clubs

def get_enrolled_clubs(usr_id, year, tri_nbr):

    clubs = query(DB.CLUBS, "SELECT club_id, name, advisor_id, day, room_nbr, description, max_nbr, enrollment_count "
                    "FROM club " 
                    "WHERE course_year = %s "
                    "AND tri_nbr = %s "
                    "AND club_type_cde = 3 "
                    "AND club_id in (SELECT club_id FROM club_user_xref WHERE usr_id=%s) "
                    "ORDER BY club_id", [str(year), str(tri_nbr), str(usr_id)])

    # enrolled clubs
    e_clubs = []

    for club in clubs:

        club_id = club[0]
        club_name = club[1]
        club_advisor_id = club[2] # need to see if usr_id matches advisor_id
        club_day = club[3]
        club_room_nbr = club[4]
        club_desc = club[5]
        club_max_nbr = club[6]
        club_enrollment_count = club[7]

        c = Club(club_name, club_day, club_id, club_desc, club_max_nbr, club_room_nbr, club_enrollment_count)

        e_clubs.append(c)

    return e_clubs

def get_club_teacher(club_id):
    teacher_id = query(DB.CLUBS, "SELECT advisor_id "
                            "FROM club "
                            "WHERE club_id = %s ", [club_id])

    full_name = query(DB.SHARED, "SELECT usr_first_name, usr_last_name "
                            "FROM user "
                            "WHERE usr_id=%s ", [teacher_id])

    return full_name[0]

# Returns the current school year formatted in "YEAR-END_YEAR" form
def get_current_year():
    return '%d-%s' % (datetime.utcnow().year, str(datetime.utcnow().year + 1)[2:])

# Returns the current '%d-%d' year string and trimester
def get_current_info():
    current_year = get_current_year()

    formatted_year = str(current_year.split('-')[0])

    print(formatted_year)

    # ps_year format - Ex: 2018 = 28
    formatted_year = formatted_year[0] + formatted_year[-1]

    current_tri = query_one(DB.CLUBS, 'SELECT tri_nbr FROM atcsdevb_dev_shared.trimester ' +
                                         'WHERE NOW() <= end_dt ' +
                                         'AND NOW() >= start_dt ' +
    #                                    'AND ps_year = %s ' +
                                         'ORDER BY end_dt')[0]
    return [current_year, current_tri]


def get_amount_left(club_id):
    club_info = query_one(DB.CLUBS, "SELECT c.max_nbr - c.enrolled_count "
                                          "FROM club c"
                                          "WHERE club_id = %d", [club_id])[0]

    return club_info


"""

def get_proposals():
    proposals = query(DB.CLUBS, "SELECT proposal_id, club_name, description, date_proposed"
                                " FROM proposal "
                                "ORDER BY proposal_id")

    all_proposals = []

    for p in proposals:
        p_id = p[0]
        p_name = p[1]
        p_desc = p[2]
        p_date = p[3]

        prop = Proposal(p_id, p_name, p_desc, p_date)
        all_proposals.append(prop)

    return all_proposals


"""