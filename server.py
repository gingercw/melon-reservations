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

@app.route('/booking', methods=["POST"])
def get_times():
    form_day = request.form.get("day")
    form_start = request.form.get("start")
    form_end = request.form.get("end")

    raw_start = datetime.strptime(form_day + " " + form_start, '%Y-%m-%d %H:%M')

    start = raw_start + (datetime.min - raw_start) % timedelta(minutes=30)

    end = datetime.strptime(form_day + " " + form_end, '%Y-%m-%d %H:%M')

    timeslots = []

    while start < end:
        time = start.strftime('%m-%d-%Y %I:%M %p')
        check_time = crud.get_appointment_by_time(time)
        if check_time:
          pass
        else:
          timeslots.append(time)
        start += timedelta(minutes=30)

    return render_template("booking.html", form_day = form_day, timeslots = timeslots)

@app.route('/reserve', methods=["POST"])
def reserve():
  """adds appointment to database"""
  user_id = session.get("user_id")
  form_dt = request.form.get("timeslot")
  time = datetime.strptime(form_dt, '%m-%d-%Y %I:%M %p')
  user = crud.get_user_by_id(user_id)
  new_appt = crud.create_appointment(time, user)
  db.session.add(new_appt)
  db.session.commit()
  flash("Thanks for making a reservation!")

  return redirect(f'/appointments/{ user_id }')


@app.route('/appointments/<user_id>')
def show_user_reservations(user_id):
    """show user's appointments'"""
    user_id = session.get("user_id")
    raw_appts = crud.get_appointments_by_user(user_id)
    today = datetime.today()
    past_appts = []
    appts = []
    for appt in raw_appts:
      if appt.time > today:
        formatted_time = appt.time.strftime('%m-%d-%Y %I:%M %p')
        appts.append(formatted_time)
      else:
        formatted_time = appt.time.strftime('%m-%d-%Y %I:%M %p')
        past_appts.append(formatted_time)


    return render_template("appointments.html", user_id = user_id, appts = appts, past_appts = past_appts)



if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)