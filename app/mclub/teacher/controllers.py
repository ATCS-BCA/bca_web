from app.db import DB, insert, insertmany, query_one, query, delete, update

from app.mclub.teacher.models import Club

def get_clubs():
    clubs = query(DB.CLUBS, "SELECT club_id, name, advisor_id, day, room_nbr, description, max_nbr, enrollment_count"
                                        " FROM club, club_type"
                                        #"WHERE club_id = usr.id" ?? is there a usr_id here 
                                        " order by club_id")

    all_clubs =[]

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

