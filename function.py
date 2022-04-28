from flask import url_for, render_template, redirect, flash, request, jsonify
from functools import wraps
from forms import CreateUserForm, CreateThingForm, CreateCategoryForm, LogInForm, AddThingForm, RemoveThingForm
from main import db, login_manager
from models import User, Thing, Category, AddThing, RemoveThing
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, current_user, logout_user

def before_first_request():
    if not User.query.get(1):
        password_hash = generate_password_hash('KG85056710a', method='pbkdf2:sha256', salt_length=8)
        first_user = User(
            first_name='Sergey',
            last_name='Samoshin',
            email='s@s.s',
            password=password_hash
        )
        db.session.add(first_user)
        db.session.commit()
        login_user(first_user, remember=True)

# перехватчик запроса befor
def before_request():
    if current_user.is_anonymous:
        return login()

# decorator
def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.id != 1:
            return logout()
        return f(*args, **kwargs)
    return decorated_function

def register_user():
    create_user_form = CreateUserForm()
    if create_user_form.validate_on_submit():
        if User.query.filter_by(email=create_user_form.email.data.lower()).first():
            flash('this email used', 'error')
            return render_template('register_user.html', form=create_user_form)
        else:
            try:
                password_hash = generate_password_hash(create_user_form.password.data, method='pbkdf2:sha256', salt_length=8)
                new_user = User(
                    first_name=create_user_form.first_name.data,
                    last_name=create_user_form.last_name.data,
                    email=create_user_form.email.data.lower(),
                    password=password_hash
                )
                db.session.add(new_user)
                db.session.commit()
                login_user(new_user, remember=True)
            except:
                print('Error')
            return redirect(url_for('home'))
    else:
        return render_template('register_user.html', form=create_user_form)

@admin_only
def delete_user(user_id):
    if user_id == 1:
        return redirect(url_for('home'))
    else:
        user_to_delete = User.query.get(user_id)
        db.session.delete(user_to_delete)
        db.session.commit()
        return redirect(url_for('home'))

def login():
    login_form = LogInForm()
    if login_form.validate_on_submit():
        email = login_form.email.data.lower()
        password = login_form.password.data
        user = User.query.filter_by(email=email).first()
        if not user or not check_password_hash(user.password, password):
            flash("Email or password are incorrect")
            return redirect(url_for('login'))
        else:
            login_user(user, remember=True)
            return redirect(request.args.get('next') or url_for('home'))
    return render_template('login.html', form=login_form)

def logout():
    logout_user()
    return redirect(url_for('home'))

def register_thing():
    categories = Category.query.all()
    list_categories = [(item.id, item.title_category) for item in categories]
    create_thing_form = CreateThingForm(one_unit=0.5)
    create_thing_form.category_id.choices = list_categories
    if create_thing_form.validate_on_submit():
        try:
            new_thing = Thing(
                category_id=create_thing_form.category_id.data,
                title=create_thing_form.title.data.lower(),
                description=create_thing_form.description.data.lower(),
                dimension=create_thing_form.dimension.data,
                one_unit=create_thing_form.one_unit.data,
                amount=0,
                user_id=current_user.id
            )
            db.session.add(new_thing)
            db.session.commit()
            print('Good')
        except:
            print('Error')
        return redirect(url_for('home'))
    else:
        return render_template('register_thing.html', form=create_thing_form)

def show_thing(thing_id):
    thing_to_show = Thing.query.get(thing_id)
    category_of_thing = Category.query.get(thing_to_show.user_id)
    form_add = AddThingForm(price=0.0)
    form_remove = RemoveThingForm()
    return render_template('thing.html', thing=thing_to_show, category=category_of_thing, form_remove=form_remove, form_add=form_add)

def add_thing(thing_id):
    form_add = AddThingForm()
    thing = Thing.query.get(thing_id)
    if form_add.validate_on_submit():
        thing.amount += form_add.amount.data
        db.session.commit()
        new_add_thing = AddThing(
            price=form_add.price.data,
            amount=form_add.amount.data,
            thing_id=thing_id
        )
        db.session.add(new_add_thing)
        db.session.commit()
    return redirect(url_for('show_thing', thing_id=thing_id))

def remove_thing(thing_id):
    form_remove = RemoveThingForm()
    thing = Thing.query.get(thing_id)
    if form_remove.remove.data and thing.amount > 0:
        thing.amount -= 1
        db.session.commit()
        new_remove_thing = RemoveThing(thing_id=thing_id)
        db.session.add(new_remove_thing)
        db.session.commit()
    return redirect(url_for('show_thing', thing_id=thing_id))

def delete_thing(thing_id):
    thing_to_delete = Thing.query.get(thing_id)
    db.session.delete(thing_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

def register_category():
    create_category_form = CreateCategoryForm()
    categories = Category.query.all()
    if create_category_form.validate_on_submit():
        try:
            new_category = Category(
                title_category=create_category_form.title_category.data.lower()
            )
            db.session.add(new_category)
            db.session.commit()
            print('Good')
        except:
            print('Error')
        return redirect(url_for('register_category'))
    else:
        return render_template('register_category.html', form=create_category_form, categories=categories)

@admin_only
def delete_category(category_id):
    if category_id == 1:
        return redirect(url_for('home'))
    else:
        category_to_delete = Category.query.get(category_id)
        for i in category_to_delete.things:
            i.category_id = 1
            db.session.commit()
        db.session.delete(category_to_delete)
        db.session.commit()
        return redirect(url_for('register_category'))

def show_all():
    things = Thing.query.all()
    category = Category.query.all()
    return render_template('index.html', title='things', things=things, category=category)

@admin_only
def all_users():
    users = User.query.all()
    return render_template('all_users.html', title='users', users=users)

def things_to_json():
    things = Thing.query.all()
    return jsonify(all_things=[thing.to_dict() for thing in things])