# Importa Flask
from flask import Flask

# Importa extensões
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS

# importar rota de teste para a AI
from app.routes.test_ai import test_ai_bp

# Instâncias globais
db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app():

    # Cria aplicação Flask
    app = Flask(__name__)

    # Carrega configurações
    app.config.from_object("app.config.Config")

    # Inicializa extensões
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    # Libera acesso do React
    CORS(app)

    # Importa rotas
    from app.routes.auth import auth_bp
    from app.routes.quizzes import quiz_bp

    # Registra rotas
    app.register_blueprint(auth_bp)
    app.register_blueprint(quiz_bp)
    app.register_blueprint(test_ai_bp)


    

    return app