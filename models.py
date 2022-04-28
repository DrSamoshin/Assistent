from main import db
from sqlalchemy.orm import relationship
from flask_login import UserMixin
from datetime import datetime

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(500), nullable=True)

    things = relationship('Thing', backref='users')

    # def __repr__(self):
    #     return f'<user {self.id}>'

class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    title_category = db.Column(db.String(20), unique=True)

    things = relationship('Thing', backref='categories')

class Thing(db.Model):
    __tablename__ = 'things'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20))
    description = db.Column(db.String(20))
    dimension = db.Column(db.String(20), nullable=True)
    one_unit = db.Column(db.Float, nullable=True)
    amount = db.Column(db.Integer, nullable=True)

    user_id = db.Column(db.Integer, db.ForeignKey(User.id), comment='Owner of things')
    category_id = db.Column(db.Integer, db.ForeignKey(Category.id), comment='Category of things')

    add = relationship('AddThing', backref='things')
    remove = relationship('RemoveThing', backref='things')

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

class AddThing(db.Model):
    __tablename__ = 'add'
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float)
    amount = db.Column(db.Integer, nullable=True)
    put_date = db.Column(db.DateTime, default=datetime.utcnow)

    thing_id = db.Column(db.Integer, db.ForeignKey(Thing.id), comment='add thing')

class RemoveThing(db.Model):
    __tablename__ = 'remove'
    id = db.Column(db.Integer, primary_key=True)
    put_date = db.Column(db.DateTime, default=datetime.utcnow)

    thing_id = db.Column(db.Integer, db.ForeignKey(Thing.id), comment='remove thing')


