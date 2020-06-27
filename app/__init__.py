from flask import Flask
import os


from configs import main_configs


def create_app(config_name):
    app = Flask(__name__)
    config = main_configs[config_name]
    app.config.from_object(config)

    return app


app = create_app(os.environ.get('APP_MODE'))
