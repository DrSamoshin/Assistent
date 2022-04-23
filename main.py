import config
from flask import Flask, render_template, url_for, redirect, flash
# from flask_login import LoginManager, UserMixin
from forms import CreateUserForm, CreateThingForm


app = Flask(__name__)
app.config.from_object(config)



# login_manager = LoginManager()
# login_manager.init_app(app)


@app.route('/')
def home():
    return render_template('index.html', title='start')

@app.route('/register_user', methods=['GET', 'POST'])
def register_user():
    create_user_form = CreateUserForm()
    if create_user_form.validate_on_submit():
        try:
            new_user = User(
                first_name=create_user_form.first_name.data,
                last_name=create_user_form.last_name.data,
                email=create_user_form.email.data,
                password=create_user_form.password.data,
            )
            db.session.add(new_user)
            db.session.commit()
            print('Good')
        except:
            print('Error')
        return redirect(url_for('home'))
    else:
        return render_template('register_user.html', form=create_user_form)

@app.route('/register_thing', methods=['GET', 'POST'])
def register_thing():
    create_thing_form = CreateThingForm()
    if create_thing_form.validate_on_submit():
        print(create_thing_form.started.data)
        try:
            new_thing = Thing(
                category=create_thing_form.category.data,
                title=create_thing_form.title.data,
                description=create_thing_form.description.data,
                dimension=create_thing_form.dimension.data,
                amount=create_thing_form.amount.data,
                started=create_thing_form.started.data
            )
            db.session.add(new_thing)
            db.session.commit()
            print('Good')
        except:
            print('Error')
        return redirect(url_for('home'))
    else:
        return render_template('register_thing.html', form=create_thing_form)

@app.route('/about')
def about():
    return render_template('about.html')

# with app.test_request_context(): # TEST REQUEST FROM SERVER
#     print(url_for('home'))

if __name__ == '__main__':
    app.debug = True
    app.run()
