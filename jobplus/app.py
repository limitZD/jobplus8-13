from flask import Flask 
from .models import db,User
from .config import configs
from flask_login import LoginManager
from flask_migrate import Migrate

def register_extension(app):
    db.init_app(app)
    Migrate(db,app)
    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def user_loader(id):
        return User.query.get(id)

    login_manager.login_view = 'front.login'

def register_blueprints(app):
    from .handlers import front,job,company,admin,user
    app.register_blueprint(front)
    app.register_blueprint(job)
    app.register_blueprint(company)
    app.register_blueprint(user)
    app.register_blueprint(admin)

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(configs.get(config))
    register_extension(app)
    register_blueprints(app)
    return app


