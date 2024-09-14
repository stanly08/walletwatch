from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from app.models import User, Expense
from app.forms import LoginForm, RegistrationForm, ExpenseForm, DeleteForm
from flask import Blueprint

# Define the main blueprint
main = Blueprint('main', __name__)

# Route for the home page
@main.route('/')
def home():
    print("Accessed Home Page")
    return render_template('index.html')

# Route for the dashboard
@main.route('/dashboard')
@login_required
def dashboard():
    print(f"User {current_user.username} accessed Dashboard")

    # Fetch expenses for the current user
    expenses = Expense.query.filter_by(user_id=current_user.id).all()

    # Calculate total expenses
    total_expenses = sum(expense.amount for expense in expenses if expense.category != 'income')

    form = DeleteForm()  # Create an instance of the form
    return render_template(
        'dashboard.html',
        expenses=expenses,
        form=form,
        username=current_user.username,
        total_expenses=total_expenses
    )

# Route for adding an expense
@main.route('/add-expense', methods=['GET', 'POST'])
@login_required
def add_expense():
    form = ExpenseForm()
    if form.validate_on_submit():
        new_expense = Expense(
            date=form.date.data,
            description=form.description.data,
            amount=form.amount.data,
            category=form.category.data,
            user_id=current_user.id
        )
        db.session.add(new_expense)
        db.session.commit()
        flash('Expense added successfully.', 'success')
        print(f"User {current_user.username} added an expense.")
        return redirect(url_for('main.dashboard'))
    return render_template('add_expense.html', form=form)

# Route for user signup
@main.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegistrationForm()
    if request.method == 'POST':
        print("Form data submitted:", request.form)
        if form.validate():
            print("Form validation successful!")
            existing_user = User.query.filter((User.username == form.username.data) | (User.email == form.email.data)).first()
            if existing_user:
                flash('Username or email already exists. Please choose a different one.', 'warning')
                print("User exists, redirecting to signup.")
                return redirect(url_for('main.signup'))
            hashed_password = generate_password_hash(form.password.data, method='pbkdf2:sha256')
            new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
            try:
                db.session.add(new_user)
                db.session.commit()
                flash('Signup successful! You can now log in.', 'success')
                print("User added successfully, redirecting to login.")
                return redirect(url_for('main.login'))
            except Exception as e:
                db.session.rollback()
                flash('Error during signup. Please try again.', 'danger')
                print(f"Error during database transaction: {e}")
        else:
            print("Form validation failed.", form.errors)
    return render_template('signup.html', form=form)

@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        # Fetch the user from the database
        user = User.query.filter_by(email=form.email.data).first()

        # Log the form data and user existence
        print(f"Form submitted: {request.form}")
        print(f"User found: {user}")

        if user:
            # Check if the password matches
            if check_password_hash(user.password, form.password.data):
                login_user(user)
                flash('Logged in successfully.', 'success')
                print(f"User {user.username} logged in successfully.")
                
                # Check the login status
                print(f"User is_authenticated: {current_user.is_authenticated}")

                # Redirect to the dashboard if login is successful
                return redirect(url_for('main.dashboard'))
            else:
                flash('Invalid password. Please try again.', 'danger')
                print("Invalid password for user:", user.email)
        else:
            flash('No account found with this email.', 'danger')
            print("No user found with email:", form.email.data)
    else:
        # Log the form validation failure
        print("Form validation failed.")
        print("Form errors:", form.errors)

    # If the form doesn't validate, or if there's a problem, render the login page
    return render_template('login.html', form=form)

@main.route('/logout', methods=['POST'])
@login_required
def logout():
    print(f"User {current_user.username} logged out.")
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('main.signup'))  # Redirect to the signup page

# Route for editing an expense
@main.route('/edit-expense/<int:expense_id>', methods=['GET', 'POST'])
@login_required
def edit_expense(expense_id):
    expense = Expense.query.get_or_404(expense_id)
    form = ExpenseForm(obj=expense)
    if form.validate_on_submit():
        expense.date = form.date.data
        expense.description = form.description.data
        expense.amount = form.amount.data
        expense.category = form.category.data
        db.session.commit()
        flash('Expense updated successfully.', 'success')
        print(f"User {current_user.username} updated expense {expense_id}.")
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
    print(f"User {current_user.username} deleted expense {expense_id}.")
    return redirect(url_for('main.dashboard'))




