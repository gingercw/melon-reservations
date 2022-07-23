from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """A user."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String, unique = True, nullable = False)
    
    def __repr__(self):
        return f'<User name={self.name}>'

class Appointment(db.Model):
    """An appointment."""

    __tablename__ = 'appointments'
    
    appointment_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    time = db.Column(db.DateTime, unique = True, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))

    user = db.relationship("User", backref="appointments")

    def __repr__(self):
        return f'<Appointment appointment_id={self.appointment_id}>'



def connect_to_db(flask_app, db_uri="postgresql:///reservations", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)