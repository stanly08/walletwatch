from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, PasswordField, SubmitField, DateField, HiddenField
from wtforms.validators import DataRequired, Email, Length, NumberRange, EqualTo, ValidationError
from app.models import User
from datetime import date

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=5, max=30)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        if not User.is_email_available(email.data):
            raise ValidationError('Sorry! Looks like the email is already taken! Please try another one.')

    def validate_username(self, username):
        if not User.is_username_available(username.data):
            raise ValidationError("Sorry! Looks like the username is already taken! Please try another one.")

class ExpenseForm(FlaskForm):
    amount = DecimalField('Amount', validators=[DataRequired(), NumberRange(min=0.01)])
    category = StringField('Category', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired(), Length(max=200)])
    date = DateField('Date', validators=[DataRequired()], format='%Y-%m-%d')
    submit = SubmitField('Save Expense')

    def validate_amount(self, amount):
        if amount.data <= 0:
            raise ValidationError('The expense amount must be greater than zero.')

    def validate_date(self, date_field):
        if date_field.data > date.today():
            raise ValidationError('The date cannot be in the future.')

    def validate_description(self, description):
        if 'miscellaneous' in description.data.lower():
            raise ValidationError('Please provide a more specific description.')

class DeleteForm(FlaskForm):
    csrf_token = HiddenField()
