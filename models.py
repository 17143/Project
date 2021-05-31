from main import db

class Project(db.model):
    __tablename__ = 'Project'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    image = db.Column(db.String())
    description = db.Column(db.Text())
    category = db.Column(db.Integer)

class Category(db.model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())