from .main_routes import main_bp
from .auth_routes import auth_bp

def register_routes(app):
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)