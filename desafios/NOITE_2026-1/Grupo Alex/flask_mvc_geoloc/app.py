from flask import Flask, redirect, url_for
from config import Config
from controllers.auth_controller import auth_blueprint
from controllers.geo_controller import geo_blueprint

app = Flask(__name__)
app.config.from_object(Config)

# Registrando as rotas (Controllers)
app.register_blueprint(auth_blueprint)
app.register_blueprint(geo_blueprint)

# Rota raiz redireciona direto para o login
@app.route('/')
def index():
    return redirect(url_for('auth.login'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)