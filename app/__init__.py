from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('../config.py')
# I imagine I could also declare a SQL db w/o an ORM here
db = SQLAlchemy(app)

from app import views, models