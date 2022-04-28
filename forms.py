from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SubmitField, PasswordField, BooleanField, SelectField, IntegerField
from wtforms.validators import DataRequired, URL, Email, NumberRange

#WTForm
class CreateUserForm(FlaskForm):
    first_name = StringField('First name:', validators=[DataRequired(message='Error')])
    last_name = StringField('Last name:', validators=[DataRequired()])
    email = StringField('Email:', validators=[Email()])
    password = PasswordField('Password:', validators=[DataRequired()])
    submit = SubmitField('Submit form')

class LogInForm(FlaskForm):
    email = StringField('Email:', validators=[Email()])
    password = PasswordField('Password:', validators=[DataRequired()])
    submit = SubmitField('Submit form')

class CreateThingForm(FlaskForm):
    category_id = SelectField('Category:', coerce=int)
    title = StringField('Title:', validators=[DataRequired()])
    description = StringField('Description:', validators=[DataRequired()])
    dimension = SelectField('Dimension:', choices=['litre', 'kilogram', 'metre', 'unit'])
    one_unit = DecimalField('One Unit:', places=2, validators=[NumberRange(min=0)])
    submit = SubmitField('Submit form')

class CreateCategoryForm(FlaskForm):
    title_category = StringField('Title:', validators=[DataRequired()])
    submit = SubmitField('Submit form')

class AddThingForm(FlaskForm):
    price = DecimalField('Price:', places=2, validators=[NumberRange(min=0)])
    amount = IntegerField('Amount:', validators=[NumberRange(min=1, max=100)])
    submit = SubmitField('Submit form')

class RemoveThingForm(FlaskForm):
    remove = BooleanField('Remove:')
    submit = SubmitField('Submit form')

