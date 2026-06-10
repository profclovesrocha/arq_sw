# FALTA ADICIONAR MAIS ROTAS E USAR O docker -> https://docs.docker.com/desktop/setup/install/linux/
from flask import Blueprint, render_template

app_routes = Blueprint('app_routes', __name__)

@app_routes.route("/")
def home():
    return render_template("index.html")

@app_routes.route("/sobre")
def sobre():
    return render_template("sobre.html")
