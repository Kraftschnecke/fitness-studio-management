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
    return "<h1>trainers page</h1>"


@app.route("/courses")
def courses():
    return "<h1>courses page</h1>"


@app.route("/rooms")
def rooms():
    return "<h1>rooms page</h1>"


if __name__ == "__main__":
    app.run(debug=True)
