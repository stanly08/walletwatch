from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app) 

    # Import and register blueprints/routes after db is initialized
    from app.routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
