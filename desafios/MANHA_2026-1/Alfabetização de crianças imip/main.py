from flask import Flask
from views import init_app
from model import init_db

app = Flask(__name__)
app.config["SECRET_KEY"] = "substitua_por_uma_chave_segura"

init_db()
init_app(app)

if __name__ == "__main__":
    app.run(debug=True)
