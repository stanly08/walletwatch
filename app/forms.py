from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FloatField, DateField, SelectField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError, Regexp
from models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=5, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8),Regexp(r'^(?=.*[a-zA-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$',
               message="Password must be at least 8 characters long, contain at least one letter, one number, and one special character.")
    ])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message="passwords don't match")])
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("Sorry! Looks like the email is already taken! Please try another one.")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("Sorry! Looks like the username is already taken! Please try another one.")

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
