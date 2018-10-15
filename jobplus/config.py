class BaseConfig():
    
    SECRET_KEY = 'to keep it secret'

class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'mysql://root@localhost:3306/jobplus?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(BaseConfig):
    pass

class TestingConfig(BaseConfig):
    pass


configs = {
    'development':DevelopmentConfig,
    'production':ProductionConfig,
    'testing':TestingConfig
}
