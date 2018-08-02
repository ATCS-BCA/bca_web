class Elective(object):

    def __init__(self, id, name, desc):
        self.name = name
        self.desc = desc
        self.id = id

        self.sections = []

    def __str__(self):
        return "<%s: %s, %s/>" % (self.id, self.name, self.desc)

class ElectiveTeacher(object):

    def __init__(self, teacher_id, teacher_name):
        self.teacher_id = teacher_id
        self.teacher_name = teacher_name


class ElectiveSection(object):

    def __init__(self, id, elective, section_nbr, tri, course_year, max, room_nbr):
        self.id = id

        self.elective = elective
        self.section_nbr = section_nbr

        self.tri = tri
        self.course_year = course_year

        self.max = max
        self.enrolled = 0

        self.room_nbr = room_nbr

        self.times = []

    def __str__(self):
        return "\n<%s: %s, %s, %s, %s, %s %s, %s, %s/>" % (self.id, self.elective, self.section_nbr, self.tri, self.course_year, self.max, self.enrolled, self.room_nbr, ', '.join([str(x) for x in self.times]))

    def getTimes(self):
        s = ' '

        for i in range(len(self.times)):
            s += self.times[i].__str__()

            if i < len(self.times)-1:
                s += ', '

        return s


class ElectiveTime(object):

    def __init__(self, id, day, desc):
        self.id = id
        self.day = day
        self.desc = desc

    def __str__(self):
        return self.desc