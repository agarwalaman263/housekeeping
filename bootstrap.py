# -*- coding: utf-8 -*-
# Librarys
from flask import Flask, render_template
import pyrebase

config = {
  apiKey: "AIzaSyDMVYOXUhKKdu4wfegbdRAb1RsKUzZykS4",
  authDomain: "udaantest-62497.firebaseapp.com",
  databaseURL: "https://udaantest-62497.firebaseio.com",
  storageBucket: "udaantest-62497.appspot.com"
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()
# Variables
app = Flask(__name__)

# Views
@app.route('/add-asset', methods=["POST"])
def add-asset():
    return "aman"

@app.route('/add-task', methods=["POST"])
def add-task():
    return "aman"

@app.route('/add-worker', methods=["POST"])
def add-worker():
    return "aman"

@app.route('/assets/all', methods=["GET"])
def all():
    return "aman"

@app.route('/allocate-task', methods=["POST"])
def allocate-task():
    return "aman"

@app.route('/get-tasks-for-workers/<workerID>', methods=["GET"])
def allocate-task(workerID):
    return "aman"

# Run
if __name__ == '__main__':
    app.run()
