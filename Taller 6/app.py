from flask import Flask
from flask_sqlalchemy import SQLAlchemy, SessionBase

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///databases/proyecto.db'

db = SQLAlchemy(app)

from controlador import *

if __name__ == '__main__':
    app.run(debug=True)