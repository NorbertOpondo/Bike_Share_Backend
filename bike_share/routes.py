import json
import datetime
from flask import jsonify, request
from bike_share import app, db, bcrypt
from datetime import date
from bike_share.models import User,Bike,Rented_Bike,Overdue_Bike

#######  This route implements user registration ########
@app.route("/", methods=["GET","POST"])
@app.route("/userRegistration", methods=["GET","POST"])
def userRegistration():
	if request.method == "POST":
		
		first_name = request.form["firstName"]
		second_name = request.form["secondName"]
		school_id = request.form["schoolId"]
		email = request.form["email"]
		hashed_password = bcrypt.generate_password_hash(request.form["password"]).decode('utf-8') 
		
		try:
			user = User(first_name=first_name,second_name=second_name,student_id=school_id,email=email,password=hashed_password)
			db.session.add(user)
			db.session.commit()
			success = 1
		except Exception as e:
			raise e
			success = 0

	return jsonify({"status":success})


######## This route implements user Login ########
@app.route("/userLogin", methods=["GET","POST"])
def userLogin():

	student_id = request.form['schoolId']
	password = request.form['password']

	if request.method == "POST":
		user = User.query.filter_by(student_id=student_id).first()
		if user and bcrypt.check_password_hash(user.password,password):
			status = "1"
		else:
			status = "0"

	return jsonify({"status":status})

