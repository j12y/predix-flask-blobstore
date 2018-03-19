
import os


class Config(object):
    """
    Base class for applicaiton configuration.
    """
    SECRET_KEY = os.environ.get('FLASK_SECRET_KEY')

    @staticmethod
    def init_app(app):
        pass


class DevConfig(Config):
    DEBUG = True


config = {
    'dev': DevConfig,
    'default': Config
}
