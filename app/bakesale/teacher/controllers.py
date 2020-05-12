from app.db import DB, insert, insertmany, query_one, query, delete, update

from app.bakesale.teacher.models import Bakesale

from config import Config
from .util import datetime_from_string, us_format

from datetime import datetime

# Get all current bakesale within 5 days of the given day
def get_all_bakesales():

    bakesales = query(DB.BAKESALE, "SELECT bakesale_id, group_name, group_size, teacher_id, requested_day, items_desc, date, bakesale.status_code, description, CONCAT(t.usr_last_name, ', ', t.usr_first_name) as teacher_name "
                                        " FROM bakesale, status, user t "
                                        " where bakesale.status_code = status.status_code "
                                        " and bakesale.teacher_id = t.usr_id "
                                        " order by bakesale_id")

    e_bakesales = []

    for bakesale in bakesales:
        print(bakesale)

        bakesale_id = bakesale[0]
        group_name = bakesale[1]
        group_size = bakesale[2]
        teacher_id = bakesale[3]
        requested_day = bakesale[4]
        items_desc = bakesale[5]
        date = bakesale[6]
        status_code = bakesale[7]
        status_desc = bakesale[8]
        teacher_name = bakesale[9]

        bakesale = Bakesale(bakesale_id, teacher_id, group_name, group_size, items_desc, date, teacher_name)

        e_bakesales.append(bakesale)

    return e_bakesales

def get_teacher_bakesales(teacher_id):

    bakesales = query(DB.BAKESALE, "SELECT bakesale_id, group_name, group_size, teacher_id, requested_day, items_desc, date, bakesale.status_code, description, CONCAT(t.usr_last_name, ', ', t.usr_first_name) as teacher_name "
                                        " FROM bakesale, status, user t "
                                        " where bakesale.status_code = status.status_code "
                                        " and %s = bakesale.teacher_id "
                                        " and bakesale.teacher_id = t.usr_id "
                                        " order by bakesale_id", [teacher_id])

    e_bakesales = []

    for bakesale in bakesales:
        print(bakesale)

        bakesale_id = bakesale[0]
        group_name = bakesale[1]
        group_size = bakesale[2]
        teacher_id = bakesale[3]
        requested_day = bakesale[4]
        items_desc = bakesale[5]
        date = bakesale[6]
        status_code = bakesale[7]
        status_desc = bakesale[8]
        teacher_name = bakesale[9]

        bakesale = Bakesale(bakesale_id, teacher_id, group_name, group_size, items_desc, date, teacher_name)

        e_bakesales.append(bakesale)

    return e_bakesales

def create_bakesale(group_name, group_size, items_desc, requested_day, teacher_id):
    insert(DB.BAKESALE, "INSERT INTO bakesale (group_name, group_size, `items_desc`, requested_day, teacher_id, status_code) VALUES (%s, %s, %s, %s, %s, %s)", (group_name, group_size, items_desc, requested_day, teacher_id, 'R'))

    return query_one(DB.BAKESALE, "SELECT bakesale_id FROM bakesale WHERE group_name=%s AND `items_desc`=%s", [group_name, items_desc])[0]

