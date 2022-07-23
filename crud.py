"""CRUD operations."""

from model import db, User, Appointment, connect_to_db

# Functions start here!

def create_user(name):
    """Create and return a new user."""

    user = User(name = name)

    return user

def get_user_by_id(user_id):
    """returns user's id"""
    return User.query.get(user_id)

def get_user_by_name(name):
    """returns user"""
    return User.query.filter(User.name == name).first()


def create_appointment(time, user):
    """Create and return a new appointment."""

    appointment = Appointment(time = time, user = user)

    return appointment

def get_appointments_by_user(user_id):
    """returns all appointments from a user"""
    return Appointment.query.filter_by(user_id = user_id).all()

def get_appointment_by_time(time):
    """return all appointment times"""
    
    return Appointment.query.filter(Appointment.time == time).first()

if __name__ == '__main__':
    from server import app
    connect_to_db(app)