from flask import Flask
from app.routes import register_routes
from app.extensions import db, bcrypt, login_manager, migrate
from app.errors import register_error_handlers
from flask_wtf import CSRFProtect
from app.config import Config
import cloudinary

csrf = CSRFProtect()

def create_app():
    app = Flask(__name__, static_folder='static', template_folder='templates')
    
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    csrf.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.account'

    cloudinary.config(
        cloud_name=app.config['CLOUDINARY_CLOUD_NAME'],
        api_key=app.config['CLOUDINARY_API_KEY'],
        api_secret=app.config['CLOUDINARY_API_SECRET']
    )

    register_routes(app)
    register_error_handlers(app)  # Register custom errors - KR 07/06/2025

    return app