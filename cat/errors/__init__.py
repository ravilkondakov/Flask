from flask import Blueprint

bp = Blueprint('errors', __name__)

from cat.errors import handlers