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

with open("user_data.json") as f:
    user_data = json.loads(f.read())

users_in_db = []

for user in user_data:
    name = user["username"]

    db_user = crud.create_user(name)
    model.db.session.add(db_user)




model.db.session.commit()
