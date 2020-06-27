from flask import Flask
import os


from configs import main_configs


def create_app(config_name):
    app = Flask(__name__)
    config = main_configs[config_name]
    app.config.from_object(config)

    from .api_apex import api_apex
    app.register_blueprint(api_apex, url_prefix='/api_apex/v1')

    return app


app = create_app(os.environ.get('APP_MODE'))
