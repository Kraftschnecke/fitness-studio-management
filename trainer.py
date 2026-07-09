from database import connection, cursor
import mysql.connector


def add_trainer():
    """asks for values - calls insert_trainer"""
    trainer_firstname, trainer_lastname = input("Enter full trainer name: ").split()
    trainer_speciality = input("Enter speciality of trainer: ")
    insert_trainer(trainer_firstname, trainer_lastname, trainer_speciality)


def insert_trainer(trainer_firstname, trainer_lastname, trainer_speciality):
    """inserts trainer into db list trainer"""
    try:
        cursor.execute("""
        INSERT INTO trainer (FirstName, LastName, Speciality)
        VALUES (%s, %s, %s)""",
        (trainer_firstname, trainer_lastname, trainer_speciality))
        connection.commit()
        print("Trainer added successfully")
    except mysql.connector.Error as err:
        print(err)


def show_trainer():
    """shows all trainers from trainer"""
    try:
        cursor.execute("""
        SELECT *
        FROM trainer""")
        rows = cursor.fetchall()
        for tup in rows:
            print(f"ID: {tup[0]}, Name: {tup[1]} {tup[2]}, Speciality: {tup[3]}")
    except mysql.connector.Error as err:
        print(err)


def change_trainer_spec():
    """ask for trainer to be changed and new speciality - calls update_trainer"""
    trainer_id = int(input("Which trainer ID should be updated? "))
    trainer_new_speciality = input("Enter new speciality: ")
    update_trainer_spec(trainer_id, trainer_new_speciality)


def update_trainer_spec(trainer_id, trainer_new_speciality):
    """update speciality from 1 trainer in db"""
    try:
        cursor.execute("""
        UPDATE trainer
        SET trainer.Speciality = %s
        WHERE trainer.TrainerID = %s""", (trainer_new_speciality, trainer_id))
        connection.commit()
        print("Change successful")
    except mysql.connector.Error as err:
        print(err)


def remove_trainer():
    """asks which trainer with ID should be removed - calls delete_trainer"""
    trainer_id = int(input("Which trainerID would you like to remove"))
    answer = input(f"Are u sure u want to remove trainer with ID {trainer_id} (y/n)")
    if answer.lower() == "y":
        delete_trainer(trainer_id)


def delete_trainer(trainer_id):
    """deletes the trainer from db"""
    try:
        cursor.execute("""
        DELETE FROM trainer
        WHERE trainer.TrainerID = %s""", (trainer_id, ))
        connection.commit()
        print("Trainer successfully removed.")
    except mysql.connector.Error as err:
        print(err)
