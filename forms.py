from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, SelectField, IntegerField
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
    dimension = SelectField('Dimension:', choices=['litres', 'kilograms', 'units'])
    amount = IntegerField('Amount:', validators=[NumberRange(min=0, max=100)])
    started = BooleanField('Started:', default=False)
    submit = SubmitField('Submit form')

class CreateCategoryForm(FlaskForm):
    title_category = StringField('Title:', validators=[DataRequired()])
    submit = SubmitField('Submit form')