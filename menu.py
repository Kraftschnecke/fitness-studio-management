import member
import trainer
import helper
import course
import room


def print_menu():
    print("""
            ==========================
            Fitnessstudio Verwaltung
            ==========================

            1. Add Member
            2. Show Member with their trainer
            3. Change trainer of a member
            4. Remove member
            11. Add Trainer
            12. Show Trainer
            13. Change Trainer Speciality
            14. Remove Trainer
            21. Add course
            22. Show courses and rooms
            23. Change room of course
            24. Remove course
            31. Add room
            32. Show rooms
            33. Change room size
            34. Remove room
            99. Exit
            """)


def run():
    while True:
        print_menu()
        try:
            auswahl = int(input("Auswahl: "))
        except ValueError:
            print("Please enter integer")
            continue
        match auswahl:
            case 1:
                member.add_member()
            case 2:
                members = member.get_member_trainer()
                for member_data in members:
                    print(f"Member: {member_data[0]} {member_data[1]}, Phone: {member_data[2]}, Mail: {member_data[3]}, has Trainer {member_data[4]} {member_data[5]} with speciality {member_data[6]}")
            case 3:
                member.change_trainer_of_member()
            case 4:
                member.remove_member()
            case 11:
                trainer.add_trainer()
            case 12:
                trainers = trainer.get_trainers()
                for tup in trainers:
                    print(f"ID: {tup[0]}, Name: {tup[1]} {tup[2]}, Speciality: {tup[3]}")
            case 13:
                trainer.change_trainer_spec()
            case 14:
                trainer.remove_trainer()
            case 21:
                course.add_course()
            case 22:
                courses = course.get_courses_room()
                for tup in courses:
                    print(f"{tup[0]} for {tup[1]} with max {tup[2]} participants in room {tup[3]} with size {tup[4]}")
            case 23:
                course.change_course_room()
            case 24:
                course.remove_course()
            case 31:
                room.add_room()
            case 32:
                rooms = room.get_rooms()
                for tup in rooms:
                    print(f"{tup[0]}, size {tup[1]}")
            case 33:
                room.change_room_size()
            case 34:
                room.remove_room()
            case 99:
                print("Goodbye!")
                helper.pause()
                return
            case _:
                print("Invalid input")
        helper.pause()
