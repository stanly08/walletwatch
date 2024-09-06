from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_login import LoginManager

db = SQLAlchemy()

login_manager = LoginManager()
login_manager.init_app(app)

# Optionally set the login view
login_manager.login_view = 'main.login'


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app) 

    # Import and register blueprints/routes after db is initialized
    from app.routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
