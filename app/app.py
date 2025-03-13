from flask import Flask
import os
from flask_login import LoginManager
from .models import User
from .account_service import collection
from datetime import timedelta

def create_app():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # find path to current directory
    TEMPLATE_DIR = os.path.join(BASE_DIR,'..','templates')  # set path to templates
    STATIC_DIR = os.path.join(BASE_DIR,'..','static')

    app = Flask(__name__, template_folder=TEMPLATE_DIR , static_folder=STATIC_DIR) 
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY') # set Secret Key
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=15)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    @login_manager.user_loader
    def load_user(user_id):
        user_data = collection.find_one({"_id": user_id})
        if user_data:
            return User(user_data["username"], user_data["password"], user_data["_id"])
        return None

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app

