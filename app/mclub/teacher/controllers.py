from app.db import DB, insert, insertmany, query_one, query, delete, update
from app.mclub.teacher.models import *
from app.shared.models import User


def get_clubs(usr_id):
    clubs = query(DB.CLUBS,
                  "SELECT club_id, name, advisor_id, day, club_type_cde, room_nbr, description, max_nbr, enrollment_count"
                                        " FROM club "
                            " WHERE advisor_id = %s"
                            " order by club_id", [usr_id])
    # probably have to get the id of the student who proposed the club

    all_clubs = []

    for club in clubs:

        club_id = club[0]
        club_name = club[1]
        club_advisor_id = club[2]
        club_day = club[3]
        club_type_cde = club[4]
        club_room_nbr = club[5]
        club_description = club[6]
        club_max_nbr = club[7]
        club_enrollment_count = club[8]

        c = Club(club_name, club_day, club_type_cde, club_id, club_description, club_max_nbr, club_room_nbr,
                 club_enrollment_count, club_advisor_id)

        all_clubs.append(c)

    return all_clubs


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


def get_club(club_id):
    info = query(DB.CLUBS,
                 "SELECT club_id, name, advisor_id, day, club_type_cde, room_nbr, description, max_nbr, enrollment_count"
                           " FROM club" 
                           " WHERE club_id = %s ", [club_id])

    if info:
        c = info[0]
        club = Club(c[1], c[3], c[4], c[0], c[6], c[7], c[5], c[8], c[2])
        # ^ i don't know why i did it this way i'm sorry
        return club  # i also probs could've done this in like one line but i have 2 brain cells

    return None


# removed advisor_id & enrollment_count from the parameters/query bc teacher can't change those
def edit_club(club_id, name, day, room_nbr, description, max_nbr, type_cde):
    query = "UPDATE club SET name = %s, day = %s, room_nbr = %s, description = %s, max_nbr = %s, club_type_cde = %s WHERE club_id = %s"
    params = [name, day, room_nbr, description, max_nbr, type_cde, club_id]
    update(DB.CLUBS, query, params)

    return False


def add_club(name, max_nbr, type_cde, room_nbr, desc, advisor_id, day):
    insert(DB.CLUBS, "INSERT INTO club (name, max_nbr, club_type_cde, room_nbr, description, advisor_id, day ) "
                     "VALUES (%s, %s, %s, %s, %s, %s, %s)", (name, max_nbr, type_cde, room_nbr, desc, advisor_id, day))

    return False


# where club.club_type = club_type.club_type_cde (idk i just thought of this and i'll probably have to use it)
def get_club_days():
    types = query(DB.CLUBS, "select club_type_cde, club_type_name from club_type")

    club_types = []
    for i in types:
        club_types.append(Day(i[0], i[1]))

    return club_types


def get_type_name(type_cde):
    type_name = query_one(DB.CLUBS, "select club_type_name from club_type where club_type.club_type_cde = %s",
                          [type_cde])
    return type_name


# get the type information for a specific club
# i forgot the thing for if the parameter is null wait i'm thinking about dr racket Never mind
def get_club_day(club_id):
    info = query(DB.CLUBS, "select club_type_cde, day"
                           "from club "
                           "where club.club_id = %s ", [club_id])

    # i could've done this on one line but i wanna make sure i'm doing this right lol
    d = info[0]
    return Day(d[0], d[1])


def add_student(club_id, usr_id):
    insert(DB.CLUBS, "INSERT INTO club_user_xref (usr_id, club_id) "
                     "VALUES (%s, %s)", (usr_id, club_id))

    return False


def get_club_students(club_id):
    # get all the students enrolled in a club
    users = query(DB.CLUBS, "SELECT usr_id FROM club_user_xref WHERE club_id=%s", [club_id])

    # get all the information of those students
    students = []
    for user in users:
        info = query_one(DB.SHARED, "SELECT usr_id, usr_first_name, usr_last_name, usr_class_year, academy_cde "
                                    "FROM user "
                                    "WHERE usr_type_cde='STD' "
                                    "AND usr_id=%s", [user[0]])

        students.append(Student(info[0], info[1], info[2], info[3], info[4]))

    # return a list of all the students enrolled in a club + their information
    return students
