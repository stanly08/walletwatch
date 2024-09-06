from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app import db  # Import db from app/__init__.py
from app.models import User, Expense  # Import models from models/__init__.py
from app.forms import LoginForm, SignupForm, ExpenseForm
from flask import Blueprint

# Define the main blueprint
main = Blueprint('main', __name__)

# Route for the home page
@main.route('/')
def home():
    return render_template('index.html')

# Route for the dashboard
@main.route('/dashboard')
@login_required
def dashboard():
    # Fetch the expenses for the logged-in user
    expenses = Expense.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard.html', expenses=expenses)

# Route for user signup
@main.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        # Create a new user
        new_user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Account created successfully! You can now log in.', 'success')
        return redirect(url_for('main.login'))
    return render_template('signup.html', form=form)

# Route for user login
@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Check if the user exists and the password is correct
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            flash('Logged in successfully.', 'success')
            return redirect(url_for('main.dashboard'))
        else:
            flash('Login failed. Please check your email and password.', 'danger')
    return render_template('login.html', form=form)

# Route for user logout
@main.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('main.login'))

# Route for adding an expense
@main.route('/add-expense', methods=['GET', 'POST'])
@login_required
def add_expense():
    form = ExpenseForm()
    if form.validate_on_submit():
        # Create a new expense
        new_expense = Expense(date=form.date.data, description=form.description.data, 
                              amount=form.amount.data, category=form.category.data, 
                              user_id=current_user.id)
        db.session.add(new_expense)
        db.session.commit()
        flash('Expense added successfully.', 'success')
        return redirect(url_for('main.dashboard'))
    return render_template('add_expense.html', form=form)

# Route for editing an expense
@main.route('/edit-expense/<int:expense_id>', methods=['GET', 'POST'])
@login_required
def edit_expense(expense_id):
    expense = Expense.query.get_or_404(expense_id)
    form = ExpenseForm(obj=expense)
    if form.validate_on_submit():
        # Update the expense
        expense.date = form.date.data
        expense.description = form.description.data
        expense.amount = form.amount.data
        expense.category = form.category.data
        db.session.commit()
        flash('Expense updated successfully.', 'success')
        return redirect(url_for('main.dashboard'))
    return render_template('edit_expense.html', form=form, expense=expense)

# Route for deleting an expense
@main.route('/delete-expense/<int:expense_id>', methods=['POST'])
@login_required
def delete_expense(expense_id):
    expense = Expense.query.get_or_404(expense_id)
    db.session.delete(expense)
    db.session.commit()
    flash('Expense deleted successfully.', 'success')
    return redirect(url_for('main.dashboard'))
