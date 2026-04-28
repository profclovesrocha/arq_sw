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
    app.run(debug=True)