from flask import render_template
from flask_login import login_required
from blueprints.acolhimento import acolhimento_bp

MASCOTES = [
    {"nome": "Alfa",     "emoji": "🦋", "desc": "A borboletinha das letras",   "cor": "#7C3AED"},
    {"nome": "Letrinha", "emoji": "📚", "desc": "O livro magico falante",       "cor": "#0891B2"},
    {"nome": "Silabao",  "emoji": "🐸", "desc": "O sapo das silabas",           "cor": "#059669"},
]

@acolhimento_bp.route("/")
@login_required
def inicio():
    return render_template("acolhimento/inicio.html", mascotes=MASCOTES)
