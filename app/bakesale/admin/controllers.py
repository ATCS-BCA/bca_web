from app.db import DB, insert, insertmany, query_one, query, delete, update

from app.bakesale.admin.models import Bakesale

from .util import datetime_from_string, us_format

from datetime import datetime

# Get all current elective sections for a tri/year
def get_requested_bakesales():
    result = query(DB.BAKESALE,
                "SELECT bakesale_id, group_name, group_size, teacher_id, requested_day, items_desc, date, status_code, DATE_FORMAT(date, '%M %D') as formatted_date FROM bakesale WHERE status_code = 'R'")
    return result

# Temporary solution for getting the corresponding times for a section
def get_current_date():
    d = datetime.datetime.today()
    return d


# Temporary solution for getting the corresponding times for a section
def get_next_bakesales():
    result = query(DB.BAKESALE, "SELECT bakesale_id, group_name, group_size, teacher_id, requested_day, items_desc, date, status_code, DATE_FORMAT(date, '%M %D') as formatted_date FROM bakesale WHERE date >= " + get_current_date() + " ORDER BY date LIMIT 5")
    return result

