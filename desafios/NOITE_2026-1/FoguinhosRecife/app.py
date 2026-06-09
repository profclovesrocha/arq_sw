<<<<<<< HEAD:desafios/NOITE_2026-1/FoguinhosRecife/app.py
from flask import Flask, request, jsonify, render_template
from database import db
from models import User, Evento, Post

app = Flask(__name__)

# 🔌 Config do banco
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///banco.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

# 🏗️ Criar banco automaticamente
with app.app_context():
    db.create_all()

    # cria eventos iniciais (se não existir)
    if Evento.query.count() == 0:
        eventos_iniciais = [
            Evento(nome="Show no Marco Zero", local="Recife"),
            Evento(nome="Carnaval de Olinda", local="Olinda"),
            Evento(nome="Feira Cultural", local="Boa Viagem")
        ]
        db.session.add_all(eventos_iniciais)
        db.session.commit()


# 🌐 ROTA PRINCIPAL
@app.route("/")
def home():
    return render_template("index.html")


# 📝 CADASTRO
@app.route("/register", methods=["POST"])
def register():
    data = request.json

    if User.query.filter_by(email=data["email"]).first():
        return jsonify({"msg": "Usuário já existe"}), 400

    novo_user = User(
        email=data["email"],
        senha=data["senha"]
    )

    db.session.add(novo_user)
    db.session.commit()

    return jsonify({"msg": "Usuário criado"})


# 🔐 LOGIN
@app.route("/login", methods=["POST"])
def login():
    data = request.json

    user = User.query.filter_by(email=data["email"]).first()

    if user and user.senha == data["senha"]:
        return jsonify({"status": "ok", "user_id": user.id})

    return jsonify({"status": "erro"}), 401


# 📡 EVENTOS
@app.route("/eventos", methods=["GET"])
def eventos():
    eventos = Evento.query.all()

    return jsonify([
        {
            "id": e.id,
            "nome": e.nome,
            "local": e.local
        }
        for e in eventos
    ])


# 💬 CRIAR POST
@app.route("/posts", methods=["POST"])
def criar_post():
    data = request.json

    novo_post = Post(
        conteudo=data["conteudo"],
        user_id=data["user_id"]
    )

    db.session.add(novo_post)
    db.session.commit()

    return jsonify({"msg": "Post criado"})


# 📥 LISTAR POSTS
@app.route("/posts", methods=["GET"])
def listar_posts():
    posts = Post.query.all()

    return jsonify([
        {
            "id": p.id,
            "conteudo": p.conteudo,
            "user_id": p.user_id
        }
        for p in posts
    ])


# ▶️ RODAR SERVIDOR
if __name__ == "__main__":
=======
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
>>>>>>> 1b23910f8fbdb558822ef0643423323080a8cd90:desafios/NOITE_2026-1/Grupo Giovanna/app.py
    app.run(debug=True)