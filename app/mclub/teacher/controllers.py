from app.db import DB, insert, insertmany, query_one, query, delete, update
from app.mclub.teacher.models import Club, Proposal


def get_clubs(usr_id):
    clubs = query(DB.CLUBS, "SELECT club_id, name, advisor_id, day, room_nbr, description, max_nbr, enrollment_count"
                                        " FROM club "
                            " WHERE advisor_id = %s"
                            " order by club_id", [usr_id])
    # THIS QUERY IS QUESTIONABLE AT BEST. I WILL PROBABLY (MOST LIKELY) (LIKE DEFINITELY) HAVE TO FIX IT IN THE FUTURE
    # probably have to get the id of the student who proposed the club

    all_clubs = []

    for club in clubs:

        club_id = club[0]
        club_name = club[1]
        club_advisor_id = club[2] # need to see if usr_id matches advisor_id
        club_day = club[3]
        club_room_nbr = club[4]
        club_description = club[5]
        club_max_nbr = club[6]
        club_enrollment_count = club[7]

        c = Club(club_name, club_day, club_id, club_description, club_max_nbr, club_room_nbr, club_enrollment_count, club_advisor_id)

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
    info = query(DB.CLUBS, "SELECT club_id, name, advisor_id, day, room_nbr, description, max_nbr, enrollment_count"
                           " FROM club" 
                           " WHERE club_id = %s ", [club_id])

    if info:
        c = info[0]
        club = Club(c[1], c[3], c[0], c[5], c[6], c[4], c[7], c[2])
        # ^this is weirdly ordered but i'm. 2 lazy to make it better
        return club  # i also probs could've done this in like one line but i have 2 brain cells

    return None


# removed advisor_id & enrollment_count from the parameters/query bc teacher can't change those
def edit_club(club_id, name, day, room_nbr, description, max_nbr):
    query = "UPDATE club SET name = %s, day = %s, room_nbr = %s, description = %s, max_nbr = %s WHERE club_id = %s"
    params = [name, day, room_nbr, description, max_nbr, club_id]
    update(DB.CLUBS, query, params)

    return False




