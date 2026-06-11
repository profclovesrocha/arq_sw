from flask import Flask, redirect, url_for
from extensions import db, bcrypt, login_manager, migrate


def create_app(config_name="development"):
    app = Flask(__name__)
    app.config.from_object(f"config.{config_name.capitalize()}Config")

    # Inicializa extensões
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    login_manager.login_view = "auth.login"
    login_manager.login_message = "Faca login para continuar."
    login_manager.login_message_category = "warning"

    with app.app_context():
        # Importar models aqui garante que @user_loader seja registrado
        import models  # noqa

        from blueprints.auth import auth_bp
        from blueprints.pedagogico import pedagogico_bp
        from blueprints.ia import ia_bp
        from blueprints.relatorios import relatorios_bp
        from blueprints.acolhimento import acolhimento_bp

        app.register_blueprint(auth_bp)
        app.register_blueprint(pedagogico_bp)
        app.register_blueprint(ia_bp)
        app.register_blueprint(relatorios_bp)
        app.register_blueprint(acolhimento_bp)

        db.create_all()

    @app.route("/")
    def index():
        return redirect(url_for("auth.login"))

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
