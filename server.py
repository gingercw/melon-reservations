from flask import (Flask, render_template, request, flash, session, redirect, jsonify, Markup)

from model import connect_to_db, db

from datetime import datetime


import crud 

from jinja2 import StrictUndefined

import os



app = Flask(__name__)
app.secret_key = "APIKEY"
app.jinja_env.undefined = StrictUndefined

if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0")