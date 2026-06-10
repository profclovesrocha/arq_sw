from flask import Flask
from .routes import app_routes

def create_app():
    app = Flask(__name__)
    app.secret_key = "chave_secreta"
    
    # Configuração do banco (exemplo SQLite)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meubanco.db'
    
    # Registrar rotas
    app.register_blueprint(app_routes)
    
    return app
