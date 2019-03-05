# _*_ coding: utf_8 _*_
# Librarys
from flask import Flask, render_template, request, Response, jsonify
import json
import mysql.connector
from flask_cors import CORS, cross_origin

# Variables

app = Flask(__name__)
app.config['DEBUG'] = True
cors = CORS(app)

# Views
@app.route('/', methods=["GET"])
def home():
	return "aman"
@app.route('/add_asset', methods=["POST"])
def add_asset():
	try:
		if(len(request.form.get("assetID"))>0):
			mydb = mysql.connector.connect(host="remotemysql.com", user="6TvJRryz6j", passwd="Th1UfQOONG",  database="6TvJRryz6j") 
			mycursor = mydb.cursor()
			try:
				sql = "INSERT INTO asset (assetID, workerID) VALUES (%s, %s)"
				val = (request.form.get("assetID"), "")
				mycursor.execute(sql, val)
				mydb.commit()
				return Response("The asset is sucessfuly added",200,mimetype="application/json")
			except:
				return Response("The assetID already exists",400,mimetype="application/json")
		else:
			return Response("ID too short",400,mimetype="application/json")	
	except:
		return Response("Incorrect way fo accessing the API. Choose the correct format. Make sure you pass through the formData or the Database in down for maintainence",400,mimetype="application/json")
	
@app.route('/add_task', methods=["POST"])
def add_task():
	try:
		if(len(request.form.get("taskID"))>0 and len(request.form.get("frequency"))>0 ):
			mydb = mysql.connector.connect(host="remotemysql.com", user="6TvJRryz6j", passwd="Th1UfQOONG",  database="6TvJRryz6j") 
			mycursor = mydb.cursor()
			try:
				sql = "INSERT INTO Task (taskID, frequency,assetID) VALUES (%s, %s,%s)"
				val = (request.form.get("taskID"), request.form.get("frequency"), "")
				mycursor.execute(sql, val)
				mydb.commit()
				return Response("The task is sucessfuly added",200,mimetype="application/json")
			except:
				return Response("The taskID already exists",400,mimetype="application/json")
		else:
			return Response("Empty string won't be accepted",400,mimetype="application/json")	
	except:
		return Response("Incorrect way fo accessing the API. Choose the correct format. Make sure you pass through the formData or the Database in down for maintainence",400,mimetype="application/json")

@app.route('/add_worker', methods=["POST"])
def add_worker():
	try:
		if(len(request.form.get("workerID"))>0):
			mydb = mysql.connector.connect(host="remotemysql.com", user="6TvJRryz6j", passwd="Th1UfQOONG",  database="6TvJRryz6j") 
			mycursor = mydb.cursor()
			try:
				sql = "INSERT INTO worker (workerID, taskID,status) VALUES (%s, %s,%s)"
				val = (request.form.get("workerID"), "", "available")
				mycursor.execute(sql, val)
				mydb.commit()
				return Response("The worker is sucessfuly added",200,mimetype="application/json")
			except:
				return Response("The workerID already exists",400,mimetype="application/json")
		else:
			return Response("Empty string won't be accepted",400,mimetype="application/json")	
	except:
		return Response("Incorrect way fo accessing the API. Choose the correct format. Make sure you pass through the formData or the Database in down for maintainence",400,mimetype="application/json")

@app.route('/assets/all', methods=["GET"])
def all():
	try:
		mydb = mysql.connector.connect(host="remotemysql.com", user="6TvJRryz6j", passwd="Th1UfQOONG",  database="6TvJRryz6j") 
		mycursor = mydb.cursor()
		mycursor.execute("SELECT * FROM asset")
		myresult = mycursor.fetchall()
		return jsonify(answer=myresult)
	except:
		return Response("Incorrect way fo accessing the API. Choose the correct format. Make sure you pass through the formData or the Database in down for maintainence",400,mimetype="application/json")

# @app.route('/allocate_task', methods=["POST"])
# def allocate_task():
#     return "aman"

@app.route('/get_tasks_for_workers/<workerID>', methods=["GET"])
def get_allocate_task_for_worker(workerID):
	# try:
	mydb = mysql.connector.connect(host="remotemysql.com", user="6TvJRryz6j", passwd="Th1UfQOONG",  database="6TvJRryz6j") 
	mycursor = mydb.cursor()
	sql="SELECT * FROM worker" 
	mycursor.execute(sql)
	myresult = mycursor.fetchall()
	for x in myresult:
		if(x[0]==workerID):
			return jsonify(answer=x)
	return Response("No such worker exists",status=400,mimetype="application/json")
	
	# except:
	# 	return Response("Incorrect way fo accessing the API. Choose the correct format. Make sure you pass through the formData or the Database in down for maintainence",400,mimetype="application/json")

# Run
if __name__ == '__main__':
    app.run(debug=True)
