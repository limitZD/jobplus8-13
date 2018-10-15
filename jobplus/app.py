from flask import Flask 
from .models import db,User
from .config import configs
from flask_login import LoginManage
from flask_migrate import Migrate

def register_extension(app):
    db.init_app(app)
    Migrate(db,app)
    login_manage = LoginManage()
    login_manage.init_app(app)

    @login_manage.user_loader
    def user_loader(id):
        return User.query.get(id)

    login_manage.login_view = 'front.login'

def register_blueprints(app):
    from .handlers import front
    app.register_blueprint(front)

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(configs.get(config))
    register_extension(app)
    register_blueprints(app)
    return app


