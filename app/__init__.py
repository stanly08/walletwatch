import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from config import Config
from flask_wtf import CSRFProtect

db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()
csrf = CSRFProtect()  # Initialize CSRFProtect

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    # Set up logging
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    try:
        # Initialize extensions
        db.init_app(app)
        migrate.init_app(app, db)
        login_manager.init_app(app)
        login_manager.login_view = 'main.login'
        csrf.init_app(app)  # Initialize CSRF protection after app creation

        # Register blueprints
        from app.routes import main
        app.register_blueprint(main)

        # Import models after app is initialized
        from app.models import User

        @login_manager.user_loader
        def load_user(user_id):
            return User.query.get(int(user_id))

        # Create all tables (optional, uncomment if needed)
        # with app.app_context():
        #     db.create_all()

        logger.info('Application initialized successfully.')

    except Exception as e:
        logger.error(f'Error during application initialization: {e}', exc_info=True)
        raise  # Re-raise the exception to ensure the app does not start if there is a critical error

    return app


