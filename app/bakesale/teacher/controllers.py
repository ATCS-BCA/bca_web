from config import DB
from app.db import insert, insertmany, query_one, query, delete, update

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
        if (date is None):
            formatted_date = "None";
        else:
            formatted_date = date.strftime("%m-%d")

        status_code = bakesale[7]
        description = bakesale[8]
        teacher_name = bakesale[9]

        bakesale = Bakesale(bakesale_id, teacher_id, group_name, group_size, items_desc, formatted_date, teacher_name, description, requested_day)

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
        if (date is None):
            formatted_date = "None";
        else:
            formatted_date = date.strftime("%m-%d")

        status_code = bakesale[7]
        description = bakesale[8]
        teacher_name = bakesale[9]

        bakesale = Bakesale(bakesale_id, teacher_id, group_name, group_size, items_desc, formatted_date, teacher_name, description, requested_day)

        e_bakesales.append(bakesale)

    return e_bakesales

def create_bakesale(group_name, group_size, items_desc, requested_day, teacher_id):
    insert(DB.BAKESALE, "INSERT INTO bakesale (group_name, group_size, `items_desc`, requested_day, teacher_id, status_code) VALUES (%s, %s, %s, %s, %s, %s)", (group_name, group_size, items_desc, requested_day, teacher_id, 'R'))

    return query_one(DB.BAKESALE, "SELECT bakesale_id FROM bakesale WHERE group_name=%s AND `items_desc`=%s", [group_name, items_desc])[0]

def get_bakesale(bakesale_id):
    info = query(DB.BAKESALE, "SELECT bakesale_id, group_name, group_size, teacher_id, requested_day, items_desc, date, bakesale.status_code, description, CONCAT(t.usr_last_name, ', ', t.usr_first_name) as teacher_name "
                           " FROM bakesale, user t, status" 
                           " WHERE bakesale.status_code = status.status_code"
                           " AND bakesale_id = %s ", [bakesale_id])

    if info:
        b = info[0]
        bakesale = Bakesale(b[0], b[3], b[1], b[2], b[5], b[6], b[9], b[8], b[4])
        return bakesale

    return None

def edit_bakesale(bakesale_id, group_name, group_size, items_desc, requested_day):
    query = "UPDATE bakesale SET group_name = %s, group_size = %s, items_desc = %s, requested_day = %s WHERE bakesale_id = %s"
    params = [group_name, group_size, items_desc, requested_day, bakesale_id]
    update(DB.BAKESALE, query, params)

    return None

