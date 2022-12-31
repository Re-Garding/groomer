"""Crud Operands"""

from model import db, Owner, Pet, Appointment, Employee


def create_owner(fname, lname, email, phone, vet_name, vet_phone, password):
"""add owner"""
    owner = Owner(fname=fname, lname=lanme, email=email, phone=phone, vet_name=vet_name, vet_phone=vet_phone, password=password)
    db.session.add(new_owner)
    db.session.commit()

    return owner

def create_pet(owner_id, name, species, breed):
    """add pet"""
    pet = Pet(owner_id=owner_id, name=name, species=species, breed=breed, last_apt=None)
    db.session.add(pet)
    db.session.commit()

    return pet

def create_apt(owner_id, pet_id, date, time, groom_type, groomer):
    """add appointment"""
    apt = Appointment(owner_id=owner_id, pet_id=pet_id, date=date, time=time, groom_type=groom_type, groomer=groomer)
    db.session.add(apt)
    db.session.commit()

    return apt

def add_employee(fname, lname, password):
    """add employee"""
    emp = Employee(fname, lname)
    db.session.add(emp)
    db.session.commit()
    return emp

def update_emp_password(emp_id, old_pass, new_pass):
    emp = Employee.query.get(emp_id)
    if emp.password == old_pass:
        emp.password = new_pass
        db.session.commit()
        return "Password change successful"
    else:
        return "Password change failed"

def cancel_apt(apt_id):
    Appointment.query.filter(Appointment.apt_id==apt_id).delete()
    db.session.commit()
    return "Cancelled"

def schedule_apt(owner_id, pet_id, date, time, groom_type, groomer):
    apt = Appointment(owner_id=owner_id, pet_id=pet_id, date=date, time=time, groom_type=groom_type, groomer=groomer)

    return apt