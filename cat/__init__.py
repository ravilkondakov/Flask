from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
import os

app = Flask(__name__)
# app.config.from_object(Config)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:1q2w3e!@#@localhost:5432/megatutorial'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from cat import routes, models

