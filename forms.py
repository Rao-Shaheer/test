from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField
from wtforms.validators import DataRequired, Length, Email, Regexp

class UserForm(FlaskForm):
    name = StringField('Name', validators=[
        DataRequired(),
        Length(min=2, max=100),
        Regexp(r'^[A-Za-z ]+$', message="Letters and spaces only")
    ])
    email = EmailField('Email', validators=[DataRequired(), Email(), Length(max=120)])

class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[
        DataRequired(),
        Length(min=2, max=100),
        Regexp(r'^[A-Za-z ]+$', message="Letters and spaces only")
    ])
    email = EmailField('Email', validators=[DataRequired(), Email(), Length(max=120)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])

class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Email(), Length(max=120)])
    password = PasswordField('Password', validators=[DataRequired()])
