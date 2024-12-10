from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from app.config import DEV_DB, PROD_DB
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = PROD_DB

db = SQLAlchemy(app)

from app import routes
