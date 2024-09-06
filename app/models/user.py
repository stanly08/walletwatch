from app import db  # Import db from app/__init__.py
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = 'user'  # Ensure the table name matches the one defined in your migration

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)

    # Define the relationship with the Expense model
    expenses = db.relationship('Expense', backref='user', lazy=True)

    def __repr__(self):
        return f'<User {self.username}>'
