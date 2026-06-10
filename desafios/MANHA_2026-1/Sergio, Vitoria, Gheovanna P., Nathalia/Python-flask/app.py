from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Home</h1>
    <p>Bem-vindo ao site!</p>
    """

@app.route("/produtos")
def produtos():
    return """
    <h1>Produtos:</h1>
    <p>Alface</p>
    """

@app.route("/clientes")
def clientes():
    return """
    <h1>Clientes:</h1>
    <p>João</p>
    """

@app.route("/contato")
def contato():
    return """
    <h1>Contato:</h1>
    <p>Email: contato@empresa.com</p>
    """

@app.route("/sobre")
def sobre():
    return """
    <h1>Sobre:</h1>
    <p>Empresa exemplo em Flask</p>
    """

if __name__ == "__main__":
    app.run(debug=True)