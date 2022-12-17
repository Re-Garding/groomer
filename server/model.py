"""models for grooming app"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Owner(db.model):
    """a pet owner and client"""

    __tablename____ = 'owners'

    owner_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fname = db.Column(db.String(20), nullable=False)
    lname = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(12), nullable=False)
    vet_name = db.Column(db.String(20), nullable=False)
    vet_phone = db.Column(db.String(12), nullable=False)
    
    __repr__(self):
        return f'<Owner ownder_id: {self.owner_id} - name: {self.lname}, {self.fname}>'




class Pet(db.model):
    """a pet"""

    __tablename__ = 'pets'

    pet_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    owner_id = db.Column(db.String(20), db.ForeignKey('owners.owner_id'), nullable=False)
    name = db.Column(db.String(20), nullable=False)
    species = db.Column(db.String(20), nullable=False)
    breed = db.Column(db.String(20), nullable=False)
    last_apt = db.Column(db.DateTime(timezone=False))

    __repr__(self):
        return f'<Pet name: {self.name} owner id: {self.ownder_id}>'
    

class Appointment(db.model):
    """an appointment"""

    __tablename__ = 'appointments'

    appt_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    owner_id = db.Column(db.String(20), db.ForeignKey('owners.owner_id'), nullable=False)
    pet_id = db.Column(db.String(20), db.ForeignKey('pets.pet_id'), nullable=False)
    date = db.Column(db.DateTime(timezone=False))
    time = db.Column(db.DateTime(timezone=False))
    groom_type = db.Column(db.String(20), nullable=False)
    groomer = db.Column(db.String(20), db.ForeignKey('employees.emp_id'), nullable=False)

    __repr__(self):
        return f'<Appt date: {self.date} time: {self.time} pet: {self.pet_id}>'

class Employee(db.model):
    """Employees"""

    __tablename__ = 'employees'

    emp_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fname = db.Column(db.String(20), nullable=False)
    lname = db.Column(db.String(20), nullable=False)

    __repr__(self):
        return f'<Pet name: {self.name} owner id: {self.ownder_id}>'




def connect_to_db(flask_app, db_uri="postgresql:///groom", echo=True):
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