class BaseConfig():

    SECRET_KEY ='makesure to set a very secret key'
    INDEX_PER_PAGE = 9
    ADMIN_PER_PAGE = 15

class DevelopmentConfig(BaseConfig):
   
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@118.24.33.253:3306/jobplus?charset=utf8'
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
