from flask import (Flask, render_template, request, flash, session, redirect, jsonify, Markup)

from model import connect_to_db, db

from datetime import date, datetime, time, timedelta



import crud 

from jinja2 import StrictUndefined

import os



app = Flask(__name__)
app.secret_key = "APIKEY"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def index():
    """go to homepage if a user is not already logged in"""
    if "user_id" in session:
        user_id = session.get("user_id")
        return redirect(f"/search/{user_id}")
    else:
        return render_template("index.html")

@app.route('/signin', methods=["POST"])
def signin():
    """sign in existing user"""
    user_name = request.form.get("user_name")
    user = crud.get_user_by_name(user_name)

    if not user:
        flash(f"Sorry! That name isn't in our system. Check the name and try again.")
        return redirect("/")
    elif user_name == user.name:
        session["user_id"] = user.user_id
        return redirect(f"/search")

@app.route("/logout")
def logout():
    """log out user"""
    del session["user_id"]
    flash("You logged out.")
    return redirect("/")

@app.route('/search')
def show_search():
    """show date time search inputs"""
    today = date.today()
    return render_template("search.html", today = today)

@app.route('/gettimes', methods=["POST"])
def get_times():
    form_day = request.form.get("day")
    form_start = request.form.get("start")
    form_end = request.form.get("end")

    raw_start = datetime.strptime(form_day + " " + form_start, '%Y-%m-%d %H:%M')

    start = raw_start + (datetime.min - raw_start) % timedelta(minutes=30)

    end = datetime.strptime(form_day + " " + form_end, '%Y-%m-%d %H:%M')

    timeslots = []

    while start < end:
        timeslots.append(start)
        start += timedelta(minutes=30)

    return redirect("/booking")



@app.route('/booking')
def make_appointment():
    """show user profile page with created cards"""

    return render_template("booking.html")



@app.route('/appointments/<user_id>')
def get_user_reservations(user_id):
    """show user profile page with created cards"""
    user = crud.get_user_by_id(user_id)
    appointments = crud.get_appointments_by_user(user_id)
    return render_template("appointments.html", user = user, appointments = appointments)



if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)