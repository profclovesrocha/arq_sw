from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import sqlite3

app = Flask(__name__)
app.secret_key = "123"

#CRIAR BANCO DE DADOS
def criar_banco():
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        email TEXT UNIQUE,
        senha TEXT,
        tipo TEXT
    )
    """)

    try:
        cursor.execute("ALTER TABLE usuarios ADD COLUMN pontos INTEGER DEFAULT 0")
    except:
        pass

    conn.commit()
    conn.close()

#CRIAÇÃO DE ROTAS

#ROTA PARA CADASTRO
@app.route("/", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        nome = request.form["nome"]
        data = request.form["data"]
        email = request.form["email"]
        senha = request.form["senha"]
        tipo = request.form["tipo"]

        conn = sqlite3.connect("usuarios.db")
        cursor = conn.cursor()

        try:
            cursor.execute(
                "INSERT INTO usuarios (nome, email, senha, tipo) VALUES (?, ?, ?, ?)",
                (nome, email, senha, tipo)
            )
            conn.commit()

        except:
            return render_template("cadastro.html", erro="Email já cadastrado!")

        conn.close()


        print(nome, data, email, senha, tipo)

        return redirect("/login")
    
    return render_template("cadastro.html")

#ROTA PARA LOGIN
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        email = request.form["email"]
        senha = request.form["senha"]
        tipo = request.form["tipo"]

        conn = sqlite3.connect("usuarios.db")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM usuarios WHERE email=? AND senha=? AND tipo=?",
            (email, senha, tipo)
        )

        usuario = cursor.fetchone()
        conn.close()

        if usuario:

            session["usuario_id"] = usuario[0]
            session["tipo"] = usuario[4]

            #REDIRECIONAMENTO
            if usuario[4] == "aluno":
                return redirect("/home_aluno")
            else:
                return redirect("/home_professor")

        else:
            return render_template("login.html", erro="Login inválido")

    return render_template("login.html")

#ROTA PARA A TELA DO ALUNO
@app.route("/home_aluno")
def home_aluno():

    if "usuario_id" not in session:
        return redirect("/login")

    usuario_id = session.get("usuario_id")

    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()

    cursor.execute("SELECT pontos FROM usuarios WHERE id=?", (usuario_id,))
    resultado = cursor.fetchone()

    conn.close()

    if resultado:
        pontos = resultado[0]
    else:
        pontos = 0

    return render_template("home_aluno.html", pontos=pontos)

#ROTA PARA ADICIONAR OS PONTOS DOS JOGOS
@app.route("/add_pontos", methods=["POST"])
def add_pontos():

    usuario_id = session.get("usuario_id")
    print("ID:", usuario_id)

    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE usuarios SET pontos = pontos + 1 WHERE id=?",
        (usuario_id,)
    )

    conn.commit()

    #VERIFICAR SE SALVOU
    cursor.execute("SELECT pontos FROM usuarios WHERE id=?", (usuario_id,))
    print("NOVOS PONTOS:", cursor.fetchone())

    conn.close()

    return "ok"

#ROTA PARA SALVAR OS DADOS DOS ALUNOS 
@app.route("/dados_alunos")
def dados_alunos():
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()

    cursor.execute("SELECT nome, pontos FROM usuarios WHERE tipo='aluno'")
    alunos = cursor.fetchall()

    conn.close()

    return jsonify(alunos)

#RORA PARA A TELA DO PROFESSOR
@app.route("/home_professor")
def home_professor():
    return render_template("home_professor.html")

#ROTA PARA OS JOGOS
@app.route("/jogo_frase")
def jogo_frase():
    if "usuario_id" not in session:
        return redirect("/login")
    return render_template("jogo_frase.html")


@app.route("/jogo_letras")
def jogo_letras():
    return render_template("jogo_letras.html")


@app.route("/jogo_imagem")
def jogo_imagem():
    return render_template("jogo_imagem.html")

#INICIALIZAÇÃO DA APLICAÇÃO
if __name__ == "__main__":
    criar_banco()
    app.run(debug=True)
