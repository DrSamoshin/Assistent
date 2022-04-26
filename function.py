from flask import url_for, render_template, redirect
from forms import CreateUserForm, CreateThingForm, CreateCategoryForm
from main import db
from models import User, Thing, Category

def register_user():
    create_user_form = CreateUserForm()
    if create_user_form.validate_on_submit():
        try:
            new_user = User(
                first_name=create_user_form.first_name.data,
                last_name=create_user_form.last_name.data,
                email=create_user_form.email.data.lower(),
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

def register_thing():
    categories = Category.query.all()
    list_categories = [(item.id, item.title_category) for item in categories]
    create_thing_form = CreateThingForm()
    create_thing_form.category_id.choices = list_categories
    if create_thing_form.validate_on_submit():
        try:
            new_thing = Thing(
                category_id=create_thing_form.category_id.data,
                title=create_thing_form.title.data.lower(),
                description=create_thing_form.description.data.lower(),
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

def delete_category(category_id):
    category_to_delete = Category.query.get(category_id)
    db.session.delete(category_to_delete)
    db.session.commit()
    return redirect(url_for('register_category'))

def show_all():
    things = Thing.query.all()
    users = User.query.all()
    return render_template('index.html', title='start', things=things, users=users)