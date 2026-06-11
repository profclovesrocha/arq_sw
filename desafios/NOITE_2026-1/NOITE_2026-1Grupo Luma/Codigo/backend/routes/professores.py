from datetime import timedelta
from flask import request
from sqlalchemy.exc import IntegrityError
from config import db, api
from models.alfabe_models import Professor, Aluno, ProgressoNivel, Licao, Categoria
from flask_restx import Resource, fields
from flask_jwt_extended import create_access_token, jwt_required

ns_professores = api.namespace('professores', description='Operações de professores')

# --- Modelos ---

professor_model = api.model('Professor', {
    'id': fields.Integer,
    'nome': fields.String,
    'matricula': fields.String,
})

professor_login_model = api.model('LoginProfessor', {
    'matricula': fields.String(required=True, description='Matrícula do professor'),
    'senha': fields.String(required=True, description='Senha do professor'),
})

professor_create_model = api.model('CreateProfessor', {
    'nome': fields.String(required=True),
    'matricula': fields.String(required=True),
    'senha': fields.String(required=True),
})

aluno_metricas_model = api.model('AlunoMetricas', {
    'id': fields.Integer,
    'nome': fields.String,
    'matricula': fields.String,
    'idade': fields.Integer,
    'estrelas': fields.Integer,
    'conquistas': fields.Integer,
    'niveis_completos': fields.Integer,
})


NOMES_NIVEL = {'1': 'Básico', '2': 'Reconhecimento', '3': 'Intermediário'}


# --- Endpoints ---

@ns_professores.route('/login')
class ProfessorLogin(Resource):
    @ns_professores.expect(professor_login_model)
    def post(self):
        """Login de professor por matrícula + senha."""
        data = request.get_json()
        matricula = data.get('matricula', '').strip()
        senha = data.get('senha', '').strip()

        if not matricula or not senha:
            return {'message': 'Matrícula e senha são obrigatórios'}, 400

        professor = Professor.query.filter_by(matricula=matricula).first()

        if not professor or not professor.verificar_senha(senha):
            return {'message': 'Credenciais inválidas'}, 401

        access_token = create_access_token(
            identity=str(professor.id),
            expires_delta=timedelta(hours=8)
        )

        return {
            'message': 'Login realizado com sucesso',
            'token': access_token,
            'professor': {
                'id': professor.id,
                'nome': professor.nome,
                'matricula': professor.matricula,
            }
        }, 200


@ns_professores.route('/create')
class ProfessorCreate(Resource):
    @ns_professores.expect(professor_create_model)
    def post(self):
        """Cria um novo professor."""
        data = request.get_json()

        nome = data.get('nome', '').strip()
        matricula = data.get('matricula', '').strip()
        senha = data.get('senha', '').strip()

        if not nome or not matricula or not senha:
            return {'message': 'Todos os campos são obrigatórios'}, 400

        if len(senha) < 6:
            return {'message': 'Senha deve ter pelo menos 6 caracteres'}, 400

        if Professor.query.filter_by(matricula=matricula).first():
            return {'message': 'Matrícula já existe'}, 409

        try:
            professor = Professor(nome=nome, matricula=matricula)
            professor.set_senha(senha)
            db.session.add(professor)
            db.session.commit()

            return {
                'message': 'Professor criado com sucesso',
                'professor': {
                    'id': professor.id,
                    'nome': professor.nome,
                    'matricula': professor.matricula,
                }
            }, 201
        except IntegrityError:
            db.session.rollback()
            return {'message': 'Erro ao criar professor'}, 500


@ns_professores.route('/alunos')
class ProfessorAlunos(Resource):
    @jwt_required()
    def get(self):
        """Lista todos os alunos com métricas de progresso (visão professor)."""
        alunos = Aluno.query.all()
        resultado = []

        for aluno in alunos:
            progressos = ProgressoNivel.query.filter_by(id_aluno=aluno.id).all()
            estrelas = sum(p.estrelas for p in progressos)
            conquistas = len(progressos)

            resultado.append({
                'id': aluno.id,
                'nome': aluno.nome,
                'matricula': aluno.matricula,
                'idade': aluno.idade,
                'estrelas': estrelas,
                'conquistas': conquistas,
                'niveis_completos': conquistas,
            })

        return resultado, 200
