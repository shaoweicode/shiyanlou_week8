import os
basedir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig(object):
    SECRET_KEY = 'makesure to set a very secret key'

class DevelopmentConfig(BaseConfig):
    DEBUG=1
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+'/home/python/shiyanlou_week8/simpledu/data.sqlite'

class ProductionConfig(BaseConfig):
    pass

class TestingConfig(BaseConfig):
    pass

configs={
    'development':DevelopmentConfig,
    'proction':ProductionConfig,
    'testing':TestingConfig
}