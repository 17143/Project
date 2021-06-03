from flask import Flask, render_template
import sqlite3
from config import Config

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def home():
    return"hello world"

@app.route("/help")
def help():
    return "Help desk."

@app.route("/projects")
def models():
    return "Projects"


@app.route("/Project/<string:project_name>")
def Project(project_name):
    connection = sqlite3.connect('portfolio.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Project where name = ? ", (project_name,))
    project = cursor.fetchone()
    connection.close()
    return "<h1>{}</h1><p>{}</p>".format(project[1], project[3])

    
if __name__ == "__main__":
    app.run(debug=True)