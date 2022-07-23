"""Script to seed database."""

import os
import json
from datetime import datetime

import crud
import model
import server

os.system("dropdb cards")
os.system("createdb cards")

model.connect_to_db(server.app)
model.db.create_all()





model.db.session.commit()
