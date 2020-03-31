from app.db import DB, insert, insertmany, query_one, query, delete, update
from app.mclub.student.models import Club, Proposal


def get_clubs():
    clubs = query(DB.CLUBS, "SELECT club_id, name, advisor_id, day, room_nbr, description, max_nbr, enrollment_count"
                                        " FROM club " 
                                        " order by club_id")
    # THIS QUERY IS QUESTIONABLE AT BEST. I WILL PROBABLY (MOST LIKELY) (LIKE DEFINITELY) HAVE TO FIX IT IN THE FUTURE

    all_clubs = []

    for club in clubs:

        club_id = club[0]
        club_name = club[1]
        club_advisor_id = club[2] # need to see if usr_id matches advisor_id
        club_day = club[3]
        club_room_nbr = club[4]
        club_desc = club[5]
        club_max_nbr = club[6]
        club_enrollment_count = club[7]

        c = Club(club_name, club_day, club_id, club_desc, club_max_nbr, club_room_nbr, club_enrollment_count)

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





