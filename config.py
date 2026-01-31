import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://notes_user:123@localhost:5432/flask_notes'

    SQLALCHEMY_TRACK_MODIFICATIONS = False