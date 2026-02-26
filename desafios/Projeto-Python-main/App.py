from main import app    

if __name__ == "__main__":
    app.run(debug=True)

@app.route("/")
def home():
    return "Seja bem-vindo ao meu primeiro projeto em Flask com Python professor Cloves!"

@app.route("/lista")
def lista():
    return "Aqui é a minha lista"

