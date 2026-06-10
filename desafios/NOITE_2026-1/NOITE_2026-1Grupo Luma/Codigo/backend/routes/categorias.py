from config import api
from models.alfabe_models import Categoria, Licao, LicaoStep, Alternativa
from flask_restx import Resource, fields
from flask_jwt_extended import jwt_required

ns_categorias = api.namespace('categorias', description='Categorias de atividades')
ns_licoes = api.namespace('licoes', description='Lições e seus conteúdos')

# --- Modelos ---

categoria_model = api.model('Categoria', {
    'id': fields.String,
    'nome': fields.String,
    'descricao': fields.String,
    'icone': fields.String,
})


# --- Endpoints de Categoria ---

@ns_categorias.route('/')
class CategoriaList(Resource):
    @jwt_required()
    def get(self):
        """Lista todas as categorias."""
        categorias = Categoria.query.all()
        return [{
            'id': c.id,
            'nome': c.nome,
            'descricao': c.descricao,
            'icone': c.icone,
        } for c in categorias], 200


# --- Endpoints de Lição ---

@ns_licoes.route('/<string:categoria_id>/<int:nivel>')
class LicaoDetail(Resource):
    @jwt_required()
    def get(self, categoria_id, nivel):
        """Retorna uma lição completa com todos os steps."""
        licao = Licao.query.filter_by(id_categoria=categoria_id, nivel=nivel).first()
        if not licao:
            return {'message': 'Lição não encontrada'}, 404

        steps = []
        for step in licao.steps:
            if step.tipo == 'card-informativo':
                steps.append({
                    'tipo': 'card-informativo',
                    'titulo': step.titulo,
                    'conteudo': step.conteudo,
                })
            elif step.tipo == 'pergunta':
                alternativas = Alternativa.query.filter_by(id_step=step.id).all()
                opcoes = [a.texto for a in alternativas]
                resposta_correta = next(
                    (i for i, a in enumerate(alternativas) if a.correta), 0
                )
                steps.append({
                    'tipo': 'pergunta',
                    'enunciado': step.enunciado,
                    'opcoes': opcoes,
                    'respostaCorreta': resposta_correta,
                })

        return {
            'id': licao.id,
            'categoriaId': licao.id_categoria,
            'nivelId': str(licao.nivel),
            'titulo': licao.titulo,
            'steps': steps,
        }, 200
