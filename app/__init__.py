from flask import Flask
from app.routes import register_routes
from app.extensions import db, bcrypt, login_manager
from flask_wtf import CSRFProtect
from app.config import Config

csrf = CSRFProtect()

def create_app():
    app = Flask(__name__,
                static_folder='static',
                template_folder='templates')
    
    app.config.from_object(Config)

    csrf.init_app(app)
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.account'

    register_routes(app)

    return app