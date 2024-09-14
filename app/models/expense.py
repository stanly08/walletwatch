from app import db  # Import db from app/__init__.py
from datetime import datetime

class Expense(db.Model):
    __tablename__ = 'expense'  # Ensure the table name matches the one defined in your migration

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(10), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'<Expense {self.id} - {self.description}>'


