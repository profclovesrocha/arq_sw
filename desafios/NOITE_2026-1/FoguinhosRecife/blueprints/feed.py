from flask import Blueprint, request, jsonify
from database import db
from models import Post

feed_bp = Blueprint('feed', __name__)

@feed_bp.route("/posts", methods=["POST"])
def criar_post():
    data = request.json
    novo_post = Post(conteudo=data["conteudo"], user_id=data["user_id"])
    db.session.add(novo_post)
    db.session.commit()
    return jsonify({"msg": "Post criado"})

@feed_bp.route("/posts", methods=["GET"])
def listar_posts():
    posts = Post.query.all()
    return jsonify([{
        "id": p.id,
        "conteudo": p.conteudo,
        "user_id": p.user_id
    } for p in posts])