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
                member.show_member_trainer()
            case 3:
                member.change_trainer_of_member()
            case 4:
                member.remove_member()
            case 11:
                trainer.add_trainer()
            case 12:
                trainer.show_trainer()
            case 13:
                trainer.change_trainer_spec()
            case 14:
                trainer.remove_trainer()
            case 21:
                course.add_course()
            case 22:
                course.show_course_room()
            case 23:
                course.change_course_room()
            case 24:
                course.remove_course()
            case 31:
                room.add_room()
            case 32:
                room.show_rooms()
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
