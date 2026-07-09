from database import connection, cursor
import mysql.connector


def add_member():
    """Asks values for new member - calls insert_member"""
    member_first, member_last = input("Enter First and Last Name: ").split()
    member_mail = input("Enter Email: ")
    member_phone = input("Enter Phone Number: ")
    member_trainerid = int(input("Enter TrainerID: "))
    insert_member(member_first, member_last, member_mail, member_phone, member_trainerid)


def insert_member(member_first, member_last, member_mail, member_phone, member_trainerid):
    """Insert member into db"""
    try:
        cursor.execute("""
        INSERT INTO member (FirstName, LastName, Email, Phone, TrainerID)
        VALUES (%s, %s, %s, %s, %s)""", (member_first, member_last, member_mail, member_phone, member_trainerid))
        connection.commit()
        print("Member successfully added")
    except mysql.connector.Error as err:
        print(err)


def show_member_trainer():
    """shows member with their trainer"""
    try:
        cursor.execute("""
        SELECT
            member.FirstName,
            member.LastName,
            member.Phone,
            member.Email,
            trainer.FirstName,
            trainer.LastName,
            trainer.Speciality
        FROM member
        JOIN trainer
        ON member.TrainerID = trainer.TrainerID""")
        rows = cursor.fetchall()
        for tup in rows:
            print(f"Member: {tup[0]} {tup[1]}, Phone: {tup[2]}, Mail: {tup[3]}, has Trainer {tup[4]} {tup[5]} with speciality {tup[6]}")
    except mysql.connector.Error as err:
        print(err)


def change_trainer_of_member():
    """asks for memberid to get changed and new trainer id - call update_trainer of member"""
    member_id = int(input("Which memberID should get a new trainer? "))
    member_trainerid = int(input("Which TrainerID is the new one?"))
    update_trainer_of_member(member_id, member_trainerid)


def update_trainer_of_member(member_id, member_trainerid):
    """updates member in db"""
    try:
        cursor.execute("""
        UPDATE member
        SET member.TrainerID = %s
        WHERE member.MemberID = %s""", (member_trainerid, member_id))
        connection.commit()
        print("member successfully updated")
    except mysql.connector.Error as err:
        print(err)


def remove_member():
    """asks for memberid, that should be removed - calls delete_member"""
    member_id = input("Which memberID should be removed? ")
    answer = input(f"Are you sure u want to remove {member_id} (y/n)? ")
    if answer.lower() == "y":
        delete_member(member_id)


def delete_member(member_id):
    """removes member with member_id from db"""
    try:
        cursor.execute("""
        DELETE FROM member
        WHERE member.memberID = %s""", (member_id, ))
        connection.commit()
        print("memer successfully removed")
    except mysql.connector.Error as err:
        print(err)
