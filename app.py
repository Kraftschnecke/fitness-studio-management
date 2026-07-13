from flask import Flask, render_template
import member
import trainer
import helper
import course
import room

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/members")
def members():
    members = member.get_member_trainer()
    return render_template("members.html", members=members)


@app.route("/trainers")
def trainers():
    trainers = trainer.get_trainers()
    return render_template("trainers.html", trainers=trainers)


@app.route("/courses")
def courses():
    courses = course.get_courses_room()
    return render_template("courses.html", courses=courses)

@app.route("/rooms")
def rooms():
    rooms = room.get_rooms()
    return render_template("rooms.html", rooms=rooms)


if __name__ == "__main__":
    app.run(debug=True)
