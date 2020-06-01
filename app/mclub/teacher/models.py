class Club(object):

    def __init__(self, name, day, type_cde, id, description, max_nbr, room_nbr, enrollment_count, advisor_id):
        self.name = name
        self.day = day
        self.type_cde = type_cde
        self.id = id
        self.description = description
        self.max_nbr = max_nbr
        self.room_nbr = room_nbr
        self.enrollment_count = enrollment_count
        self.advisor_id = advisor_id


class Day(object):

    def __init__(self, type_cde, type_name):
        self.type_cde = type_cde
        self.type_name = type_name


class Student(object):
    def __init__(self, usr_id, first_name, last_name, class_year, academy_cde):
        self.usr_id = usr_id
        self.first_name = first_name
        self.last_name = last_name
        self.class_year = class_year
        self.academy_cde = academy_cde


class Proposal(object):
    def __init__(self, id, name, desc, date):
        self.id = id
        self.name = name
        self.description = desc
        self.date = date




