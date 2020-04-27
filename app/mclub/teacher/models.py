class Club(object):

    def __init__(self, name, day, id, description, max_nbr, room_nbr, enrollment_count, advisor_id):
        self.name = name
        self.day = day
        self.id = id
        self.description = description
        self.max_nbr = max_nbr
        self.room_nbr = room_nbr
        self.enrollment_count = enrollment_count
        self.advisor_id = advisor_id


class Proposal(object):
    def __init__(self, id, name, desc, date):
        self.id = id
        self.name = name
        self.description = desc
        self.date = date




