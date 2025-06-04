from flask import Flask
from app.routes import register_routes
from app.extensions import db, bcrypt, login_manager
from flask_wtf import CSRFProtect
from app.config import Config
import cloudinary

csrf = CSRFProtect()

def create_app():
    app = Flask(__name__,
                static_folder='static',
                template_folder='templates')
    
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

     #cloudinary setup - 04/06/2025
    cloudinary.config(
        cloud_name=app.config['CLOUDINARY_CLOUD_NAME'],
        api_key=app.config['CLOUDINARY_API_KEY'],
        api_secret=app.config['CLOUDINARY_API_SECRET']
    )

    csrf.init_app(app)
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.account'

    register_routes(app)

    return app