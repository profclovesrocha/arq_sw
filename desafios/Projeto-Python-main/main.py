from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Banco SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usuarios.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))


with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    nome = request.form['nome']


    novo = Usuario(nome=nome)
    db.session.add(novo)
    db.session.commit()

    return redirect('/listar')

@app.route('/listar')
def listar():
    usuarios = Usuario.query.all()
    return render_template('listar.html', usuarios=usuarios)

if __name__ == '__main__':
    app.run(debug=True)