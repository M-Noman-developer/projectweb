from flask import Flask, escape, request, render_template
from flask_sqlalchemy import SQLAlchemy
print(__file__)

import os
project_dir = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)
print(project_dir)

from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "databasefile.db"))

app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
class login(db.Model):

    username = db.Column(db.String(40),unique=True, nullable=False, primary_key = True)
    email = db.Column(db.String(40),unique=False, nullable=False)
    number = db.Column(db.String(40), unique=False, nullable=False)
    password = db.Column(db.String(40), unique=False, nullable=False)

app = Flask(__name__)
@app.route('/')
def choice():
    return render_template('choice.html')
@app.route('/adminpge.html')
def adminpg():
    return render_template('adminpge.html')
@app.route('/teacher-role.html')
def teacherpg():
    return render_template('teacher-role.html')
@app.route('/student-role.html')
def studentpg():
    return render_template('student-role.html')

@app.route('/admin.html', methods=['POST','GET'])
def admin():
    if request.method == "POST":
        user1 = login()
        user1.name = request.form['username']
        user1.email = request.form['email']
        user1.password = request.form['pass']
        user1.number = request.form['number']

        db.session.add(user1)
        db.session.commit()
    return render_template('admin.html')
@app.route('/student.html', methods=['POST','GET'])
def student():
    if request.method == "POST":
        user1 = login()
        user1.name = request.form['username']
        user1.email = request.form['email']
        user1.password = request.form['pass']
        user1.number = request.form['number']

        db.session.add(user1)
        db.session.commit()
    return render_template('student.html')
@app.route('/teacher.html', methods=['POST','GET'])
def teacher():
    if request.method == "POST":
        user1 = login()
        user1.name = request.form['username']
        user1.email = request.form['email']
        user1.password = request.form['pass']
        user1.number = request.form['number']

        db.session.add(user1)
        db.session.commit()
    return render_template('teacher.html')
app.run(debug=True)