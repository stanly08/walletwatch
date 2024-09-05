from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    # Import models only after db is initialized
    from app.models import User, Expense
    # Import routes or blueprints here
    from app.routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
