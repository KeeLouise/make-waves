import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = 'MWAVES_2025'
    SQLALCHEMY_DATABASE_URI = 'postgresql://makewaves_user:MWaves2025***@localhost:5432/makewaves_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # profile image upload - KR 25/05/2025
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    UPLOAD_FOLDER = os.path.join(basedir, 'static', 'uploads')