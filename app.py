# _*_ coding: utf_8 _*_
# Librarys
from flask import Flask, render_template, request, Response, jsonify
import json
import mysql.connector
from flask_cors import CORS, cross_origin
import datetime

# Variables

app = Flask(__name__)
app.config['DEBUG'] = True
cors = CORS(app)
#functions 
def verify(string,table):
	mydb = mysql.connector.connect(host="remotemysql.com", user="6TvJRryz6j", passwd="Th1UfQOONG",  database="6TvJRryz6j") 
	mycursor = mydb.cursor()
	columnName=table.lower()+"ID";
	sql="SELECT * FROM "+table +" WHERE "+columnName+" = \""+string+"\";"
	mycursor.execute(sql)
	myresult = mycursor.fetchall()
	if(len(myresult)==1):
		return True
	return False
# Views
@app.route('/', methods=["GET"])
def home():
	return "aman"
@app.route('/add_asset', methods=["POST"])
def add_asset():
	try:
		assetID=request.form.get("assetID")
		if(len(assetID)>0):
			mydb = mysql.connector.connect(host="remotemysql.com", user="6TvJRryz6j", passwd="Th1UfQOONG",  database="6TvJRryz6j") 
			mycursor = mydb.cursor()
			try:
				sql = "INSERT INTO asset VALUES ('"+assetID+"');"
				mycursor.execute(sql)
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
		taskID=request.form.get("taskID")
		frequency=request.form.get("frequency")
		if(len(taskID)>0 and len(frequency)>0 ):
			mydb = mysql.connector.connect(host="remotemysql.com", user="6TvJRryz6j", passwd="Th1UfQOONG",  database="6TvJRryz6j") 
			mycursor = mydb.cursor()
			try:
				sql = "INSERT INTO Task VALUES (%s, %s)"
				val = (taskID,frequency)
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
		workerID=request.form.get("workerID")

		if(len(workerID)>0):
			mydb = mysql.connector.connect(host="remotemysql.com", user="6TvJRryz6j", passwd="Th1UfQOONG",  database="6TvJRryz6j") 
			mycursor = mydb.cursor()
			try:
				sql = "INSERT INTO worker (workerID, status,taskID,timeOfAllocation,taskTobePerformedBy) VALUES (%s, %s,%s,%s,%s)"
				val = (workerID, "available","NULL",datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
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
		final=[]
		for x in myresult:
			print(x)
			final.append(x[0])
		return jsonify(ListOfAllAssests=final)
	except:
		return Response("Incorrect way fo accessing the API. Choose the correct format. Make sure you pass through the formData or the Database in down for maintainence",400,mimetype="application/json")

@app.route('/get_tasks_for_workers/<workerID>', methods=["GET"])
def get_allocate_task_for_worker(workerID):
	mydb = mysql.connector.connect(host="remotemysql.com", user="6TvJRryz6j", passwd="Th1UfQOONG",  database="6TvJRryz6j") 
	mycursor = mydb.cursor()
	sql="SELECT * FROM worker WHERE workerID=\""+workerID+"\""; 
	mycursor.execute(sql)
	myresult = mycursor.fetchall()
	final={}
	if(len(myresult)==1):
		final["workerID"]=myresult[0][0]
		final["taskID"]=myresult[0][1]
		final["status"]=myresult[0][2]
		final["timeOfAllocation"]=myresult[0][3]
		final["taskTobePerformedBy"]=myresult[0][4]
		return jsonify(answer=final)
	return Response("No such worker exists",status=400,mimetype="application/json")

@app.route('/allocate_task', methods=["POST"])
def allocate_task():
	try:
		workerID=request.form.get("workerID")
		assetID=request.form.get("assetID")
		taskID=request.form.get("taskID")
		timeOfAllocation=request.form.get("timeOfAllocation")
		taskTobePerformedBy=request.form.get("taskTobePerformedBy")
		datetime.datetime.strptime(timeOfAllocation,'%Y-%m-%d %H:%M:%S')
		datetime.datetime.strptime(taskTobePerformedBy,'%Y-%m-%d %H:%M:%S')

		if(len(assetID)>0 and len(taskID)>0 and len(workerID)>0): 
			if(verify(assetID,"asset")):
				if(verify(taskID,"Task")):
					if(verify(workerID,"worker")):
						mydb = mysql.connector.connect(host="remotemysql.com", user="6TvJRryz6j", passwd="Th1UfQOONG",  database="6TvJRryz6j") 
						mycursor = mydb.cursor()
						sql="SELECT * FROM worker WHERE workerID= \""+workerID+"\";"
						print(sql)
						mycursor.execute(sql)
						myresult1 = mycursor.fetchall()
						if(myresult1[0][2]=="available"):
							mydb = mysql.connector.connect(host="remotemysql.com", user="6TvJRryz6j", passwd="Th1UfQOONG",  database="6TvJRryz6j") 
							mycursor = mydb.cursor()
							sql="UPDATE `worker` SET `workerID`=\""+workerID+"\",`taskID`=\""+taskID+"\",`status`=\"occupied\",`timeOfAllocation`=\""+timeOfAllocation+"\",`taskTobePerformedBy`=\""+taskTobePerformedBy+"\" WHERE `workerID`=\""+workerID+"\"";
							mycursor.execute(sql)
							mydb.commit()
							return "Successfuly alloted the task"
						else:
							ts1 = myresult1[0][4]
							ts2= timeOfAllocation
							f = '%Y-%m-%d %H:%M:%S'
							stored=datetime.datetime.strptime(ts1, f)
							new=datetime.datetime.strptime(ts2, f)
							if(new>stored):
								mydb1 = mysql.connector.connect(host="remotemysql.com", user="6TvJRryz6j", passwd="Th1UfQOONG",  database="6TvJRryz6j") 
								mycursor1 = mydb1.cursor()
								sql="UPDATE `worker` SET `workerID`=\""+workerID+"\",`taskID`=\""+taskID+"\",`status`=\"occupied\",`timeOfAllocation`=\""+timeOfAllocation+"\",`taskTobePerformedBy`=\""+taskTobePerformedBy+"\" WHERE `workerID`=\""+workerID+"\"";
								mycursor1.execute(sql)
								mydb1.commit()
								return "Successfuly alloted the task"
							else:	
								return Response("The worker is Busy",status=400,mimetype="application/json")
					else:
						return Response("WorkerID not registered",status=400,mimetype="application/json")
				else:
					return Response("taskID not registered",status=400,mimetype="application/json")
			else:
				return Response("assetID not registered",status=400,mimetype="application/json")
		else:
			return Response("Missing parameters",status=400,mimetype="application/json")
	except:
		return Response("Incorrect way fo accessing the API. Choose the correct format. Make sure you pass through the formData or the Database in down for maintainence",400,mimetype="application/json")		

# Run
if __name__ == '__main__':
    app.run(debug=True)
