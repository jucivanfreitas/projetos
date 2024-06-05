# app/__init__.py
from flask import Flask
from . import auth
from .routes import main_bp
from config import Config

def create_app(version='1.0'):
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config['VERSION'] = version

    app.register_blueprint(auth.bp)
    app.register_blueprint(main_bp)

    @app.context_processor
    def inject_version():
        return dict(version=version)

    return app
