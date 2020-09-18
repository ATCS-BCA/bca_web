from app import mysql
from config import Config

# Executes the statemet and then returns the result
# Statement - SQL Query
# Vars - List of variables in Query to prevent SQL Injection
def query(db, statement, vars="", dictResults=False):
    curtype = pymysql.cursors.DictCursor
    if (dictResults):
        curtype = mysql.get_db().DictCursor

    cur = mysql.get_db().cursor(curtype)

    cur = mysql.get_db().cursor()
    use_db(cur, db)

    if vars:
        cur.execute(statement, vars)
    else:
        cur.execute(statement)

    if Config.SHOW_QUERIES:
        log_print("QUERY", db, statement, vars)

    result = cur.fetchall()
    cur.connection.commit()
    return result


# only searches for one return option/value
def query_one(db, statement, vars=""):
    cur = mysql.get_db().cursor()
    use_db(cur, db)

    if vars:
        cur.execute(statement, vars)
    else:
        cur.execute(statement)

    if Config.SHOW_QUERIES:
        log_print("QUERY", db, statement, vars)
    return cur.fetchone()


def insert(db, statement, vars):
    cur = mysql.get_db().cursor()
    use_db(cur, db)

    cur.execute(statement, vars)

    cur.connection.commit()

    if Config.SHOW_QUERIES:
        log_print("INSERT", db, statement, vars)

def insertmany(db, statement, data):
    cur = mysql.get_db().cursor()
    use_db(cur, db)

    cur.executemany(statement, data)

    cur.connection.commit()

    if Config.SHOW_QUERIES:
        log_print("INSERT", db, statement, data)


def update(db, statement, vars="", display=False):
    cur = mysql.get_db().cursor()
    use_db(cur, db)

    if vars:
        cur.execute(statement, vars)
    else:
        cur.execute(statement)

    cur.connection.commit()

    if display:
        log_print("UPDATED", db, statement, vars)


def delete(db, statement, vars="", display=False):
    cur = mysql.get_db().cursor()
    use_db(cur, db)

    if vars:
        cur.execute(statement, vars)
    else:
        cur.execute(statement)

    cur.connection.commit()

    if display:
        log_print("DELETE", db, statement, vars)


def use_db(cur, db, display=False):
    if display:
        print("Using db, %s" % db)
    cur.execute('USE ' + str(db))

def log_print(operation, db, statement, values):
    print("%s @ %s: '%s', %s " % (operation, db, statement, values))