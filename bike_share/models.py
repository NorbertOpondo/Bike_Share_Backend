from bike_share import db
from datetime import datetime

class User(db.Model):
	student_id = db.Column(db.String(100), primary_key=True)
	first_name = db.Column(db.String(40), nullable=False)
	second_name = db.Column(db.String(40), nullable=False)
	email = db.Column(db.String(90), nullable=False)
	password = db.Column(db.String(90), nullable=False)
	date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	bike_status = db.Column(db.Boolean, default=False, nullable=False)
	bike = db.relationship('Rented_Bike',backref='owner',lazy=True)


class Bike(db.Model):
	bike_id = db.Column(db.Integer,primary_key=True)
	bike_type = db.Column(db.String(100), nullable=False)
	bike_status = db.Column(db.Boolean, default=False, nullable=False)


class Rented_Bike(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	student_id = db.Column(db.String(100),db.ForeignKey('user.student_id'),nullable=False)
	amount_paid = db.Column(db.String(100),nullable=False)
	date_acquired = db.Column(db.DateTime,nullable=False)
	return_date = db.Column(db.DateTime, nullable=False)
	accessories = db.Column(db.String, nullable=True)

class Overdue_Bike(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	student_id = db.Column(db.String(100),db.ForeignKey('user.student_id'),nullable=False)
	return_date = db.Column(db.DateTime, nullable=False)