from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

app.run(host='192.168.1.73', port=81)