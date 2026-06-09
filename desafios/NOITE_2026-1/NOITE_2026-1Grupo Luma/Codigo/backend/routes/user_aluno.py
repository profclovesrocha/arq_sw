from flask import request, jsonify,  render_template
from flask_jwt_extended import jwt_required
from sqlalchemy.exc import IntegrityError
from config import db, api
from models.alfabe_models import Aluno
import re
from flask_restx import Resource, fields
ns_user_aluno = api.namespace('aluno', description='Operações relacionadas aos alunos')

user_aluno_get_all_model = api.model('UserAluno', {
    'id_aluno': fields.Integer,
    'matricula_aluno': fields.String,
    'idade': fields.Integer,
    'Responsaveis': fields.List(fields.Nested(api.model('Responsavel', {
        'id_responsavel': fields.Integer,
    }))),
    'progessos': fields.List(fields.Nested(api.model('Progresso', {
        'id_progresso': fields.Integer,
    }))),
    'prontuarios': fields.List(fields.Nested(api.model('Prontuario', {
        'id_prontuario': fields.Integer,
    }))),
    'chamados_medicos': fields.List(fields.Nested(api.model('ChamadoMedico', {
        'id_chamado': fields.Integer,
    }))),
    'sessoes': fields.List(fields.Nested(api.model('Sessao', {
        'id_sessao': fields.Integer,
    })))
})

user_aluno_create_model = api.model('CreateUserAluno', {
    'matricula_aluno': fields.String(required=True, description='Matrícula do aluno'),
    'idade': fields.Integer(required=True, description='Idade do aluno')
})

aluno_update_model = api.model('UpdateUserAluno', {
    'idade': fields.Integer(description='Idade do aluno')
})

aluno_delete_model = api.model('DeleteUserAluno', {
    'id_aluno': fields.Integer(required=True, description='ID do aluno a ser deletado')
})

@ns_user_aluno.route('/getall') # Rota para listar todos os alunos (EXCLUSIVO PARA DEV)
class UserAlunoList(Resource):
    @ns_user_aluno.marshal_list_with(user_aluno_get_all_model)
    def get(self):
        guests = Aluno.query.all()
        return guests, 200

@ns_user_aluno.route('/getbymatricula/<string:matricula>') # Rota para buscar um aluno pela matrícula
class UserAlunoGetByMatricula(Resource):
    @jwt_required()
    @ns_user_aluno.marshal_list_with(user_aluno_get_all_model)
    def get(self, matricula):
        try:
            guests = Aluno.query.filter(Aluno.matricula_aluno.like(f'%{matricula}%')).all()
            return guests, 200
        except IntegrityError as e:
            db.session.rollback()
            return {
                'message': 'Erro ao procurar matrícula',
                'error': str(e.orig)
            }, 400     

@ns_user_aluno.route('/getbyage/<string:idade>') # Rota para buscar um aluno pela idade
class UserAlunoGetByAge(Resource):
    @jwt_required()
    @ns_user_aluno.marshal_list_with(user_aluno_get_all_model)
    def get(self, idade):
        try:
            guests = Aluno.query.filter(Aluno.idade.like(f'%{idade}%')).all()
            return guests, 200
        except IntegrityError as e:
            db.session.rollback()
            return {
                'message': 'Erro ao procurar idade',
                'error': str(e.orig)
            }, 400     

@ns_user_aluno.route('/create') # Rota para criar um novo aluno
class UserAlunoCreate(Resource):
    @jwt_required()
    @ns_user_aluno.expect(user_aluno_create_model)
    def post(self):
        data = request.get_json()
        pattern_cpf = r'^\d{3}\.\d{3}\.\d{3}-\d{2}$'

        try: 
            if not (data.get('matricula_aluno') and data.get('idade')):
                    return {'message': 'Todos os campos são obrigatórios'}, 400  
            if Aluno.query.filter_by(matricula_aluno=data['matricula_aluno']).first():
                return {'message': 'Matrícula já existe'}, 400
            aluno = Aluno(
                matricula_aluno=data['matricula_aluno'],
                idade=data['idade']
            )
            db.session.add(aluno)
            db.session.commit()
            return {
                    'message': 'Aluno criado com sucesso',
                    'aluno': aluno.to_dict()
                }, 201
        except IntegrityError as e:
            db.session.rollback()
            return {
                'message': 'Erro ao criar o usuário',
                'error': str(e.orig)
            }, 400     
        
@ns_user_aluno.route('/delete') # Rota para deletar um aluno
class UserAlunoDelete(Resource):
    @jwt_required()
    @ns_user_aluno.expect(aluno_delete_model)
    def delete(self):
        data = request.get_json()
        aluno = Aluno.query.filter_by(id_aluno=data['id_aluno']).first()

        try:
            if aluno:
                db.session.delete(aluno)
                db.session.commit()
                return {'message': 'Aluno deletado com sucesso'}, 200
            else:
                return {'message': 'Aluno não encontrado'}, 404   
        except Exception as e:
            db.session.rollback()
            return {'message': 'Erro ao deletar aluno', 'error': str(e.orig)}, 400
    
@ns_user_aluno.route('/update/<int:id>') # Rota para atualizar um aluno
class UserAlunoUpdate(Resource):
    @jwt_required()
    @ns_user_aluno.expect(aluno_update_model)
    def put(self, id):
        data = request.get_json()
        aluno = Aluno.query.filter_by(id_aluno=id).first()

        try:
            if aluno:
                if 'idade' in data:
                    aluno.idade = data['idade']
                db.session.commit()
                return {'message': 'Aluno atualizado com sucesso'}, 200
            else:
                return {'message': 'Aluno não encontrado'}, 404  

        except IntegrityError as e:
            db.session.rollback()
            return {'message': 'Erro ao atualizar aluno', 'error': str(e.orig)}, 400