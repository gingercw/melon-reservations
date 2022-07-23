"""CRUD operations."""

from model import db, User, Appointment, connect_to_db

# Functions start here!

def create_user(name):
    """Create and return a new user."""

    user = User(name = name)

    return user

def create_appointment(time, user):
    """Create and return a new appointment."""

    appointment = Appointment(time = time, user = user)

    return appointment

if __name__ == '__main__':
    from server import app
    connect_to_db(app)