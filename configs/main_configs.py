class Config:

    @staticmethod
    def init_app(self):
        pass


class DevelopmentConfig:
    DEBUG = True


class ProductionConfig:
    pass


main_configs = {'default': DevelopmentConfig,
                'development': DevelopmentConfig,
                'production': ProductionConfig,
                }
