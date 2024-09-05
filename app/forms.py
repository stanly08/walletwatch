from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FloatField, SelectField, DateField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from app.models import User

class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=5, max=30)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    # Custom validation to check if the email is already in use
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Sorry! Looks like the email is already taken! Please try another one.')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("Sorry! Looks like the username is already taken! Please try another one.")

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

class ExpenseForm(FlaskForm):
    date = DateField('Date', validators=[DataRequired()], format='%Y-%m-%d')
    description = StringField('Description', validators=[DataRequired(), Length(max=200)])
    amount = FloatField('Amount', validators=[DataRequired()])
    category = SelectField('Category', choices=[('Food', 'Food'), ('Transport', 'Transport'), ('Shopping', 'Shopping'), ('Rent', 'Rent'), ('Other', 'Other')], validators=[DataRequired()])
    submit = SubmitField('Save Expense')

    # Custom validation for the expense amount
    def validate_amount(self, amount):
        if amount.data <= 0:
            raise ValidationError('The expense amount must be greater than zero.')

    # Custom validation for the expense date (e.g., cannot be in the future)
    def validate_date(self, date_field):
        if date_field.data > date.today():
            raise ValidationError('The date cannot be in the future.')

    # Custom validation for the description (e.g., can't be too generic)
    def validate_description(self, description):
        if 'miscellaneous' in description.data.lower():
            raise ValidationError('Please provide a more specific description.')



