from main import db

Project_Genre = db.Table('Project_Genre', db.Model.metadata,
                    db.Column('Project_id', db.Integer, db.ForeignKey('Project.id')),
                    db.Column('Genre_id', db.Integer, db.ForeignKey('Genre.id'))
                   )

class Project(db.Model):
    __tablename__ = 'Project'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    image = db.Column(db.String())
    description = db.Column(db.Text())
    category = db.Column(db.Integer)
    
    genre = db.relationship('Genre', secondary=Project_Genre, back_populates='project')

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())

class Genre(db.Model):
    __tablename__ = 'Genre'
    id = db.Column(db.integer, primary_key=True)
    name = db.Column(db.String())

    project = db.relationship('Project', secondary=Project_Genre, back_populates='genre')