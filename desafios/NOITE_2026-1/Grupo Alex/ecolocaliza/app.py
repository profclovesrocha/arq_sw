from flask import Flask, redirect, url_for
from database import db  # <-- Alterado para importar do arquivo database.py
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Vincula o banco de dados a esta instância do Flask
    db.init_app(app)

    from controllers.auth_controller import auth_blueprint
    from controllers.geo_controller import geo_blueprint
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(geo_blueprint)

    # Cria as tabelas fisicamente no MySQL se não existirem
    with app.app_context():
        db.create_all()

    @app.route('/')
    def index():
        return redirect(url_for('auth.login'))

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)