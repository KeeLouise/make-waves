from flask import Flask
from app.routes import register_routes
from app.extensions import db, bcrypt, login_manager
from flask_wtf import CSRFProtect
csrf = CSRFProtect()

def create_app():
    app = Flask(__name__,
                static_folder='static',
                template_folder='templates')

    app.config['SECRET_KEY'] = 'MWAVES_2025'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://makewaves_user:MWaves2025***@localhost:5432/makewaves_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    csrf.init_app(app)

    # Initialize extensions
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    register_routes(app)

    return app