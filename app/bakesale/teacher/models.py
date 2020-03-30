class Bakesale(object):

    def __init__(self, id, teacher_id, group_name, group_size, items_desc, date, teacher_name):
        self.id = id
        self.teacher_id = teacher_id
        self.group_name = group_name
        self.group_size = group_size
        self.items_desc = items_desc
        self.date = date
        self.teacher_name = teacher_name

class Request(object):

    def _init_(self, group_name, group_size, items_desc, requested_day):
        self.group_name = group_name
        self.group_size = group_size
        self.items_desc = items_desc
        self.requested_day = requested_day

