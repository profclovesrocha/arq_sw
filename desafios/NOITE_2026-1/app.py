from flask import Flask
from blueprints.webui import webui_bp

app = Flask(__name__)
app.register_blueprint(webui_bp)

if __name__ == "__main__":
    app.run(debug=True)