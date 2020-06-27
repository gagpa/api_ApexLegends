import os

from flask import Flask

from configs import main_configs
from .database import db
from flask_migrate import Migrate


def create_app(config_name):
    app = Flask(__name__)
    config = main_configs[config_name]
    app.config.from_object(config)
    config.init_app(app)
    db.init_app(app)

    from .api_apex import api_apex
    app.register_blueprint(api_apex, url_prefix='/api_apex/v1')

    return app


app = create_app(os.environ.get('APP_MODE') or 'default')
migrate = Migrate(app, db)
