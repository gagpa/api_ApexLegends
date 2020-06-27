import os


class Config:

    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    # SERVER_NAME = os.environ.get('HOST')

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    pass


main_configs = {'default': DevelopmentConfig,
                'development': DevelopmentConfig,
                'production': ProductionConfig,
                }
