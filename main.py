from flask import Flask

from config import Config

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def home():
    return"hello world"

@app.route("/help")
def help():
    return "Help desk."

@app.route("/Project/<string:project_name>")
def Project(project_name):
    return "Here is a {} Project".format(project_name)

if __name__ == "__main__":
    app.run(debug=True)