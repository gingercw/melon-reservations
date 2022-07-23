from flask import (Flask, render_template, request, flash, session, redirect, jsonify, Markup)

from model import connect_to_db, db

from datetime import datetime


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


@app.route('/search/<user_id>')
def find_available_times(user_id):
    """show user profile page with created cards"""
    user = crud.get_user_by_id(user_id)
    return render_template("search.html", user = user)

@app.route('/booking/<user_id>')
def make_appointment(user_id):
    """show user profile page with created cards"""
    user = crud.get_user_by_id(user_id)
    return render_template("search.html", user = user)

@app.route('/reservations/<user_id>')
def get_user_reservations(user_id):
    """show user profile page with created cards"""
    user = crud.get_user_by_id(user_id)
    appointments = crud.get_appointments_by_user(user_id)
    return render_template("reservations.html", user = user, appointments = appointments)



if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0")