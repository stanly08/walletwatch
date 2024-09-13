import os

class Config:
    # Secret key setup
    m_key = '0a619fb395d0f3b8b2975cf7fd54593b0316f86bf2dc0517'
    SECRET_KEY = os.environ.get('SECRET_KEY') or m_key

    # Define the base directory
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    # SQLite database URI pointing to instance/database.db
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(BASE_DIR, "../instance/database.db")}'
    
    # Disable modification tracking for performance
    SQLALCHEMY_TRACK_MODIFICATIONS = False

