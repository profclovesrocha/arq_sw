from datetime import timedelta
from flask import request, jsonify,  render_template
from sqlalchemy.exc import IntegrityError
from config import db, api
from models.alfabe_models import Professor
from flask_restx import Resource, fields
from flask_jwt_extended import JWTManager, create_access_token, jwt_required

ns_user_professores = api.namespace('professores', description='Operações relacionadas aos professores')

user_professores_get_model = api.model('UserProfessor', {
    'id_professor': fields.Integer,
    'matricula_professor': fields.String,
    'cpf': fields.String,
    'telefone': fields.String,
    'email': fields.String,
})

user_professores_create_model = api.model('CreateUserProfessor', {
    'matricula_professor': fields.String(required=True),
    'cpf': fields.String(required=True),
    'telefone': fields.String(required=True),
    'email': fields.String(required=True),
})

user_professores_update_model = api.model('UpdateUserProfessor', {
    'cpf': fields.String,
    'telefone': fields.String,
    'email': fields.String
})

user_professores_delete_model = api.model('DeleteUserProfessor', {
    'id_professor': fields.Integer(required=True)
})

user_professores_login_model = api.model('LoginUserProfessor', {
    'matricula_professor': fields.String(required=True),
    'cpf': fields.String(required=True)
})

@ns_user_professores.route('/get') # Rota para listar professores
class UserProfessorList(Resource):
    @jwt_required()
    @ns_user_professores.marshal_list_with(user_professores_get_model)
    def get(self):
        professors = Professor.query.all()
        return professors, 200

@ns_user_professores.route('/create') # Rota para criar um novo professor
class UserProfessorCreate(Resource):
    @jwt_required()
    @ns_user_professores.expect(user_professores_create_model)
    def post(self):
        data = request.get_json()
        new_professor = Professor(matricula_professor=data['matricula_professor'], cpf=data['cpf'], telefone=data['telefone'], email=data['email'])
        db.session.add(new_professor)
        if data['matricula_professor'] == '' or data['cpf'] == '' or data['telefone'] == '' or data['email'] == '':
            return {'message': 'Todos os campos são obrigatórios'}, 400
        if data['matricula_professor'] == Professor.matricula_professor:
            return {'message': 'Matrícula já existe'}, 400
        try:
            db.session.commit()
            return {'message': 'Professor criado com sucesso'}, 201
        except IntegrityError as e:
            db.session.rollback()
            return {'message': 'Erro ao criar professor', 'error': str(e.orig)}, 400    

@ns_user_professores.route('/login') # Rota para login de professor
class UserProfessorLogin(Resource):
    @ns_user_professores.expect(user_professores_login_model)
    def post(self):
        data = request.get_json()
        professor = Professor.query.filter_by(matricula_professor=data['matricula_professor']).first()
        access_token = create_access_token(identity=str(professor.id_professor), expires_delta=timedelta(hours=8)) if professor else None

        try:
            if professor and professor.cpf == data['cpf']:
                return {
                'message': 'Login realizado com sucesso',
                'token': access_token,
                'cpf': professor.cpf,
                'matricula': professor.matricula_professor
                }, 200
            else:
                return {'message': 'Login ou senha inválidos'}, 401  
        except Exception as e:
            return {'message': 'Erro ao realizar login', 'error': str(e.orig)}, 500
        
@ns_user_professores.route('/update/<int:id_professor>') # Rota para atualizar um professor
class UserProfessorUpdate(Resource):
    @jwt_required()
    @ns_user_professores.expect(user_professores_update_model)
    def put(self, id_professor):
        data = request.get_json()
        professor = Professor.query.filter_by(id_professor=id_professor).first()
        
        try: 
            if professor:
                if 'matricula_professor' in data:
                    professor.matricula_professor = data['matricula_professor']
                if 'cpf' in data:
                    professor.cpf = data['cpf']
                if 'telefone' in data:
                    professor.telefone = data['telefone']
                if 'email' in data:
                    professor.email = data['email']
                db.session.commit()
                return {'message': 'Professor atualizado com sucesso'}, 200
            else:
                return {'message': 'Professor não encontrado'}, 404  

        except IntegrityError as e:
            db.session.rollback()
            return {'message': 'Erro ao atualizar professor', 'error': str(e.orig)}, 400

@ns_user_professores.route('/delete/<int:id_professor>') # Rota para deletar um professor
class UserProfessorDelete(Resource):
    @jwt_required()
    def delete(self, id_professor_id):
        professor = Professor.query.filter_by(id_professor=id_professor_id).first()
        
        try:
            if professor:
                db.session.delete(professor)
                db.session.commit()
                return {'message': 'Professor deletado com sucesso'}, 200
            else:
                return {'message': 'Professor não encontrado'}, 404
        except Exception as e:
            db.session.rollback()
            return {'message': 'Erro ao deletar professor', 'error': str(e.orig)}, 400    