import config
from flask import Flask, render_template, url_for, redirect, flash
# from flask_login import LoginManager, UserMixin
import function
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)

# login_manager = LoginManager()
# login_manager.init_app(app)

@app.route('/')
def home():
    return function.show_all()

@app.route('/register_user', methods=['GET', 'POST'])
def register_user():
    return function.register_user()

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
    return render_template('about.html')

# with app.test_request_context(): # TEST REQUEST FROM SERVER
#     print(url_for('home'))

if __name__ == '__main__':
    app.debug = True
    app.run()
