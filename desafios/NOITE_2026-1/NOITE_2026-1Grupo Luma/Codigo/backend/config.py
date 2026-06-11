from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_restx import Api
from dotenv import load_dotenv
import os
from flask_jwt_extended import JWTManager

load_dotenv()

app = Flask(__name__)

ALFABE_DB = os.getenv('ALFABE_DATABASE_URL')
JWT_KEY = os.getenv('JWT_SECRET_KEY')

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recepcao.db'
app.config['SQLALCHEMY_DATABASE_URI'] = ALFABE_DB
app.config['JWT_SECRET_KEY'] = JWT_KEY
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
CORS(app)

jwt = JWTManager(app)

authorizations = {
    'Bearer': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization',
        'description': 'Digite: Bearer <seu_token>'
    }
}

api = Api(
    app,
    version='1.0',
    title='Alfabe API',
    description='API dos sistemas da Alfabe',
    authorizations=authorizations,
    security='Bearer'  
)