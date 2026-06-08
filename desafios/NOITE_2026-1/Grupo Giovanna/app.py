import os
from flask import Flask, render_template
from database import db, bcrypt
from blueprints.auth import auth_bp
from blueprints.feed import feed_bp

app = Flask(__name__)

# ----------------- A MÁGICA PARA RESOLVER O ERRO -----------------
# Pega o caminho absoluto de onde está o seu arquivo app.py
basedir = os.path.abspath(os.path.dirname(__file__))

# Configura o SQLAlchemy para criar o banco EXATAMENTE nessa pasta
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "banco.db")
# -----------------------------------------------------------------

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# 🧩 Inicialização Modular das Extensões
db.init_app(app)
bcrypt.init_app(app)

# 🏗️ Registro dos Blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(feed_bp)

# 🌐 Rota Raiz
@app.route("/")
def home():
    return render_template("index.html")

# 🚀 Inicialização do Servidor
if __name__ == "__main__":
    with app.app_context():
        # Cria as tabelas fisicamente no banco de dados
        db.create_all() 
    app.run(debug=True)