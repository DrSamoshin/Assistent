from main import app
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(500), nullable=True)

    def __repr__(self):
        return f'<user {self.id}>'

class Thing(db.Model):
    __tablename__ = 'things'
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(20))
    title = db.Column(db.String(20))
    description = db.Column(db.String(20))
    dimension = db.Column(db.String(20), nullable=True)
    amount = db.Column(db.Integer, nullable=True)
    started = db.Column(db.Boolean, nullable=True)