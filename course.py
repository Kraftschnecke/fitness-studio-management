from database import connection, cursor
import mysql.connector


def add_course():
    """asks values for new course - calls insert_course"""
    course_name = input("Name of course: ")
    course_duration = int(input("Duration of course: "))
    course_max_participants = int(input("Maximal Participants: "))
    course_roomid = int(input("Enter RoomID: "))
    insert_course(course_name, course_duration, course_max_participants, course_roomid)


def insert_course(course_name, course_duration, course_max_participants, course_roomid):
    """inserts course in db"""
    try:
        cursor.execute("""
        INSERT INTO course (Name, Duration, MaxParticipants, RoomID)
        VALUES (%s, %s, %s, %s)""", (course_name, course_duration, course_max_participants, course_roomid))
        connection.commit()
        print("course added")
    except mysql.connector.Error as err:
        print(err)


def get_courses_room():
    """shows courses with their rooms"""
    try:
        cursor.execute("""
        SELECT
            course.Name,
            course.Duration,
            course.MaxParticipants,
            room.RoomName,
            room.RoomSize
        FROM course
        JOIN room
        ON course.RoomID = room.RoomID""")
        return cursor.fetchall()
        for tup in rows:
            print(f"{tup[0]} for {tup[1]} with max {tup[2]} participants in room {tup[3]} with size {tup[4]}")
    except mysql.connector.Error as err:
        print(err)
        return []


def change_course_room():
    """ask for course and room changed to -  calls update_course_room"""
    course_id = int(input("courseID: "))
    course_roomid = int(input("new roomID: "))
    update_course_room(course_id, course_roomid)


def update_course_room(course_id, course_roomid):
    """updates course with id to new room in db"""
    try:
        cursor.execute("""
        UPDATE course
        SET course.RoomID = %s
        WHERE course.CourseID = %s""", (course_roomid, course_id))
        connection.commit()
        print("course changed successfully")
    except mysql.connector.Error as err:
        print(err)


def remove_course():
    """asks for course to be removed - calls delete_course"""
    course_id = int(input("Which courseID do u want to remove?: "))
    answer = input(f"Are you sure u want to remove {course_id}").lower()
    if answer == "y":
        delete_course(course_id)


def delete_course(course_id):
    try:
        cursor.execute("""
        DELETE FROM course
        WHERE course.CourseID = %s""", (course_id, ))
        connection.commit()
        print("course removed successfully")
    except mysql.connector.Error as err:
        print(err)
