from os import name
from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy, model
import sqlite3
from config import Config


app = Flask(__name__)
app.config.from_object(Config)
db =  SQLAlchemy(app)

import models

#Home route
@app.route('/')
def home():
    return render_template('home.html')

#Route to Help desk
@app.route("/Help")
def help():
    return "Help desk."

#List's all Projects
@app.route("/projects")
def projects():
    projects = models.Project.query.all()
    return render_template('all_models.html', projects=projects)
  
#List's individual games
@app.route('/game/<int:id>')
def game(id):
  game = models.Project.query.filter_by(id=id).first_or_404()
  print(game)
  return render_template('game.html', game=game)


#route for individul projects
@app.route('/blender/<int:id>')
def blender(id):
  blender = models.Project.query.filter_by(id=id).first_or_404()
  print(blender)
  return render_template('blender.html', blender=blender)


#route for projects in different category's
@app.route('/category/<string:category_name>')
def category(category_name):
  if category_name == "games":
     data = models.Project.query.filter_by(category=1).all()
     
  if category_name == "blendermodels":
      data = models.Project.query.filter_by(category=3).all()
      
  if category_name == "animations":
    data = models.Project.query.filter_by(category=2).all()

  return render_template('projects.html', data=data)

#test
@app.route('/blendermodelss')
def blendermodelss():
  blendermodelss = models.Project.query.filter_by(category=3).all()
  print(blendermodelss)
  return render_template('blendermodelss.html', blendermodelss=blendermodelss)

#Basic SQL query without the use of SQALchemy
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