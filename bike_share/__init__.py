from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)

app.secret_key = b'_5#y2L"chhjfg456878230002F4bdlaqyxQ8555342z\n\xec]/>?@$'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from bike_share import models

bcrypt = Bcrypt(app)

from bike_share import routes
