from database import cursor, connection
import mysql.connector


def add_room():
    """asks value - calls insert_room"""
    room_name = input("Enter room name: ")
    room_size = int(input("Enter room size: "))
    insert_room(room_name, room_size)


def insert_room(room_name, room_size):
    """inserts new room in db"""
    try:
        cursor.execute("""
        INSERT INTO room (RoomName, RoomSize)
        VALUES (%s, %s)""", (room_name, room_size))
        connection.commit()
        print("room added succesfully")
    except mysql.connector.Error as err:
        print(err)


def show_rooms():
    """shows all rooms"""
    try:
        cursor.execute("""
        SELECT
            room.RoomName,
            room.RoomSize
        FROM room""")
        rows = cursor.fetchall()
        for tup in rows:
            print(f"{tup[0]}, size {tup[1]}")
    except mysql.connector.Error as err:
        print(err)


def change_room_size():
    """asks for room to be changed and new roomsize"""
    room_id = int(input("Enter roomID: "))
    room_size = int(input("Enter new room size: "))
    update_room_size(room_id, room_size)


def update_room_size(room_id, room_size):
    """changes room size for roomid"""
    try:
        cursor.execute("""
        UPDATE room
        SET room.RoomSize = %s
        WHERE room.RoomID = %s""", (room_size, room_id))
        connection.commit()
        print("Room successfully updated")
    except mysql.connector.Error as err:
        print(err)


def remove_room():
    """ask for roomid to be removed"""
    room_id = int(input("Enter roomID to remove: "))
    answer = input(f"Are you sure you want to remove room with id {room_id}")
    if answer.lower() == "y":
        delete_room(room_id)


def delete_room(room_id):
    """deletes room where room_id"""
    try:
        cursor.execute("""
        DELETE FROM room
        WHERE room.RoomID = %s""", (room_id, ))
        connection.commit()
        print("Room successfully removed")
    except mysql.connector.Error as err:
        print(err)
