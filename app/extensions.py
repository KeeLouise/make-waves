"""
Initialise flask extensions without an app instance.
These will be tied to the app in create_app() - KR 22/05/2025
"""
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()