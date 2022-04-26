from main import db
from sqlalchemy.orm import relationship


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(500), nullable=True)

    things = relationship('Thing', backref='users')

    def __repr__(self):
        return f'<user {self.id}>'

class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    title_category = db.Column(db.String(20))

    things = relationship('Thing', backref='categories')

class Thing(db.Model):
    __tablename__ = 'things'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20))
    description = db.Column(db.String(20))
    dimension = db.Column(db.String(20), nullable=True)
    amount = db.Column(db.Integer, nullable=True)
    started = db.Column(db.Boolean, nullable=True)

    user_id = db.Column(db.Integer, db.ForeignKey(User.id), comment='Owner of things')
    category_id = db.Column(db.Integer, db.ForeignKey(Category.id), comment='Category of things')



