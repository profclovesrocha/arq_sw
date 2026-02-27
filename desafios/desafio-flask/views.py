from main import app
from flask import render_template

@app.route("/")
def homepage():
    return  render_template("homepage.html")

@app.route("/contatos")
def contatos():
    return 'Entre em contato conosco via:'

@app.route("/sobre")
def sobre():
    return 'Conheça quem somos e nossa história:'