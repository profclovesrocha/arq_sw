import os
from flask import Flask, render_template
from database import db, bcrypt

# 1. IMPORTANDO OS 4 BLUEPRINTS DO DIAGRAMA
from blueprints.auth import auth_bp
from blueprints.feed import feed_bp 
from blueprints.mapa import mapa_bp           
from blueprints.catalogo import catalogo_bp   

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "banco.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
bcrypt.init_app(app)

# 2. REGISTRANDO OS 4 BLUEPRINTS NO SISTEMA
app.register_blueprint(auth_bp)
app.register_blueprint(feed_bp)     
app.register_blueprint(mapa_bp)       
app.register_blueprint(catalogo_bp)  

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    with app.app_context():
        db.create_all() 
    app.run(debug=True)
