from flask import render_template
from config import app, db, api
from routes.professores import ns_professores
from routes.alunos import ns_alunos
from routes.categorias import ns_categorias, ns_licoes

api.add_namespace(ns_professores, path='/professores')
api.add_namespace(ns_alunos, path='/alunos')
api.add_namespace(ns_categorias, path='/categorias')
api.add_namespace(ns_licoes, path='/licoes')


@app.route('/redoc')
def redoc():
    return render_template('redoc.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5001) 