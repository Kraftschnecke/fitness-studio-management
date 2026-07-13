from flask import Flask, render_template, request, redirect, url_for
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


@app.route("/add_member", methods=["GET", "POST"])
def add_member():
    if request.method == "POST":
        firstname = request.form["firstname"]
        lastname = request.form["lastname"]
        email = request.form["email"]
        phone = request.form["phone"]
        trainerid = request.form["trainerid"]

        member.insert_member(
            firstname,
            lastname,
            email,
            phone,
            trainerid
        )
        return redirect(url_for("members"))
    return render_template("add_member.html")


if __name__ == "__main__":
    app.run(debug=True)
