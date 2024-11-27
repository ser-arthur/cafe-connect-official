import os

class Config:
    # Secret key for CSRF protection and session management
    SECRET_KEY = os.environ['SECRET_KEY']
    API_KEY = os.environ['API_KEY']

    # Database URI for SQLAlchemy (environment variable provided by Render for PostgreSQL)
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']  # 'DATABASE_URL' is automatically set by Render.

    SQLALCHEMY_TRACK_MODIFICATIONS = False