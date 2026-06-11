from flask import request, jsonify,  render_template
from flask_jwt_extended import jwt_required
from sqlalchemy import func
from sqlalchemy.exc import IntegrityError
from config import db, api
from models.alfabe_models import Responsavel
from flask_restx import Resource, fields
import datetime

ns_responsavel = api.namespace('responsavel', description='Operações relacionadas aos responsáveis')

responsavel_get_all_model = api.model('Responsavel', {
    'id_responsavel': fields.Integer,
    'matricula_responsavel': fields.String,
    'cpf': fields.String,
    'telefone': fields.String,
    'email': fields.String,
    'id_aluno': fields.Integer
})

responsavel_create_model = api.model('CreateResponsavel', {
    'matricula_responsavel': fields.String(required=True),
    'cpf': fields.String(required=True),
    'telefone': fields.String(required=True),
    'email': fields.String(required=True),
    'id_aluno': fields.Integer(required=True)
})

responsavel_delete_model = api.model('DeleteResponsavel', {
    'id_responsavel': fields.Integer(required=True)
})

responsavel_update_model = api.model('UpdateResponsavel', {
    'cpf': fields.String,
    'telefone': fields.String,
    'email': fields.String,
    'id_aluno': fields.Integer
})

@ns_responsavel.route('/getall') # Rota para listar todos os responsáveis (EXCLUSIVO PARA DEV)
class ResponsavelList(Resource):
    @jwt_required()
    @ns_responsavel.marshal_list_with(responsavel_get_all_model)
    def get(self):
        responsaveis = Responsavel.query.all()
        return responsaveis, 200
    
@ns_responsavel.route('/create') # Rota para criar uma nova visita
class ResponsavelCreate(Resource):
    @jwt_required()
    @ns_responsavel.expect(responsavel_create_model)
    def post(self):
        data = request.get_json()
        user_guest = Responsavel.query.filter_by(id=data['user_guest_id']).first()
        new_resposavel = Responsavel(
            matricula_responsavel=data['matricula_responsavel'],
            cpf=data['cpf'],
            telefone=data['telefone'],
            email=data['email'],
            id_aluno=data['id_aluno']
        )

        db.session.add(new_resposavel)
        try:
            db.session.commit()
            return {'message': 'Responsável criado com sucesso'}, 201
        except IntegrityError as e:
            db.session.rollback()
            return {'message': 'Erro ao criar responsável', 'error': str(e.orig)}, 400

@ns_responsavel.route('/delete') # Rota para deletar um responsável
class ResponsavelDelete(Resource):
    @jwt_required()
    @ns_responsavel.expect(responsavel_delete_model)
    def delete(self):
        data = request.get_json()
        responsavel = Responsavel.query.filter_by(id=data['id_responsavel']).first()

        try:
            if responsavel:
                db.session.delete(responsavel)
                db.session.commit()
                return {'message': 'Responsável deletado com sucesso'}, 200
            else:
                return {'message': 'Responsável não encontrado'}, 404   
        except Exception as e:
            db.session.rollback()
            return {'message': 'Erro ao deletar responsável', 'error': str(e.orig)}, 400          

@ns_responsavel.route('/update/<int:id>') # Rota para atualizar um responsável
class ResponsavelUpdate(Resource):
    @jwt_required()
    @ns_responsavel.expect(responsavel_update_model)
    def put(self, id):
        data = request.get_json()
        responsavel = Responsavel.query.filter_by(id=id).first()

        try:
            if responsavel:
                if 'cpf' in data:
                    responsavel.cpf = data['cpf']
                if 'telefone' in data:
                    responsavel.telefone = data['telefone']
                if 'email' in data:
                    responsavel.email = data['email']
                if 'id_aluno' in data:
                    responsavel.id_aluno = data['id_aluno']
                db.session.commit()
                return {'message': 'Responsável atualizado com sucesso'}, 200
            else:
                return {'message': 'Responsável não encontrado'}, 404   
        except Exception as e:
            db.session.rollback()
            return {'message': 'Erro ao atualizar responsável', 'error': str(e.orig)}, 400