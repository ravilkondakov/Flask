from flask import Blueprint

bp = Blueprint('main', __name__)

from cat.main import routes