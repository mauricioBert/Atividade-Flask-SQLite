from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Studant(db.Model):
    id =db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    lastName = db.Column(db.String(120))
    age =db.Column(db.Integer)
    room = db.Column(db.String(150))
    school = db.Column(db.String(150))

    def __int__(self, name, lastName, age, room, school):
        self.name = name
        self.lastName = lastName
        self.age = age
        self.room = room
        self.school = school
