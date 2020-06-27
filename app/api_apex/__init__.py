from flask import Blueprint

api_apex = Blueprint('api_apex', __name__)

from . import controllers
