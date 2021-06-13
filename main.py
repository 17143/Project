from os import name
from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy, model
import sqlite3
from config import Config


app = Flask(__name__)
app.config.from_object(Config)
db =  SQLAlchemy(app)

import models

@app.route('/')
def home():
    return render_template('home.html')

@app.route("/Help")
def help():
    return "Help desk."

@app.route("/projects")
def projects():
    projects = models.Project.query.all()
    return render_template('projects.html', projects=projects)

@app.route('/project/<int:id>')
def project(id):
  project = models.Pizza.query.filter_by(id=id).first_or_404()
  return render_template('pizza.html', project=project)

# @app.route("/Project/<string:project_name>")
# def Project(project_name):
#     connection = sqlite3.connect('portfolio.db')
#     cursor = connection.cursor()
#     cursor.execute("SELECT * FROM Project where name = ? ", (project_name,))
#     project = cursor.fetchone()
#     connection.close()
#     return "<h1>{}</h1><p>{}</p>".format(project[1], project[3])

    
if __name__ == "__main__":
    app.run(debug=True)