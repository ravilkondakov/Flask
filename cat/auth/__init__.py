from flask import Blueprint

bp = Blueprint('auth', __name__)

from cat.auth import routes