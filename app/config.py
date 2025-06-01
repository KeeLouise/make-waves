import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'MWAVES_2025')

    # Use DATABASE_URL from Render, fallback to local DB - KR 01/06/2025
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL',
        'postgresql://makewaves_user:MWaves2025***@localhost:5432/makewaves_db'
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # profile image uploads - KR 01/06/2025
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    UPLOAD_FOLDER = os.path.join(basedir, 'static', 'uploads')