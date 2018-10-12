class BaseConfig():
	SCRET_KEY ='makesure to set a very secret key'

class DevelopmentConfig(BaseConfig):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = 'mysql://root@localhost:3306/jobplus?charset=utf-8'

class ProductionConfig(BaseConfig):
	pass

class TestingConfig(BaseConfig):
	pass


configs = {
	'development':DevelopmentConfig,
	'production':ProductionConfig,
	'testing':TestingConfig
}
