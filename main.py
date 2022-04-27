from flask import Flask
import config
from flask_login import LoginManager, UserMixin, login_required
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)
login_manager = LoginManager(app)

import function

from models import User
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
def home():
    return function.show_all()

@app.route('/register_user', methods=['GET', 'POST'])
def register_user():
    return function.register_user()

@app.route('/delete_user/<int:user_id>', methods=['GET'])
def delete_user(user_id):
    return function.delete_user(user_id)

@app.route('/login', methods=['GET', 'POST'])
def login():
    return function.login()

@app.route('/logout', methods=['GET'])
def logout():
    return function.logout()

@app.route('/register_thing', methods=['GET', 'POST'])
def register_thing():
    return function.register_thing()

@app.route('/delete_thing/<int:thing_id>', methods=['GET'])
def delete_thing(thing_id):
    return function.delete_thing(thing_id)

@app.route('/register_category', methods=['GET', 'POST'])
def register_category():
    return function.register_category()

@app.route('/delete_category/<int:category_id>', methods=['GET'])
def delete_category(category_id):
    return function.delete_category(category_id)

@app.route('/about')
def about():
    return function.about()

# with app.test_request_context(): # TEST REQUEST FROM SERVER
#     print(url_for('home'))

if __name__ == '__main__':
    app.debug = True
    app.run()
