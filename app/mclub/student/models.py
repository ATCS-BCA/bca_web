class Club(object):

    def __init__(self, name, day, id, desc, max_nbr, room_nbr, enrollment_count):
        self.name = name
        self.day = day
        self.id = id
        self.desc = desc
        self.max_nbr = max_nbr
        self.room_nbr = room_nbr
        self.enrollment_count = enrollment_count


class Proposal(object):
    def __init__(self, id, name, desc, date):
        self.id = id
        self.name = name
        self.description = desc
        self.date = date


