from flask import Flask

app = Flask(_name_)

@app.route('/')
def index( ):
    return 'Olá, sou o projeto Call Fast'

app.run ( host= '192.168.1.15', port=81)