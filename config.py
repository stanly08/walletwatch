import os

class Config:
    m_key = '0a619fb395d0f3b8b2975cf7fd54593b0316f86bf2dc0517'
    SECRET_KEY = os.environ.get('SECRET_KEY') or m_key
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
