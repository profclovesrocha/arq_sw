from datetime import datetime
from flask import request
from flask_jwt_extended import jwt_required
from sqlalchemy.exc import IntegrityError
from config import db, api
from models.alfabe_models import Aluno, ProgressoNivel, Licao, Categoria
from flask_restx import Resource, fields
import re

ns_alunos = api.namespace('alunos', description='Operações de alunos')

# --- Modelos de serialização ---

aluno_model = api.model('Aluno', {
    'id': fields.Integer,
    'nome': fields.String,
    'matricula': fields.String,
    'idade': fields.Integer,
})

aluno_login_model = api.model('LoginAluno', {
    'matricula': fields.String(required=True, description='Matrícula do aluno'),
})

aluno_cadastro_model = api.model('CadastroAluno', {
    'nome': fields.String(required=True, description='Nome do aluno'),
    'cpf': fields.String(required=True, description='CPF do aluno (formato: 000.000.000-00)'),
    'idade': fields.Integer(required=True, description='Idade do aluno (3-12)'),
})

nivel_progresso_model = api.model('NivelProgresso', {
    'categoriaId': fields.String,
    'nivelId': fields.String,
    'concluido': fields.Boolean,
    'estrelas': fields.Integer,
})

conquista_model = api.model('Conquista', {
    'id': fields.String,
    'nome': fields.String,
    'categoriaId': fields.String,
    'nivelId': fields.String,
    'desbloqueada': fields.Boolean,
})

progresso_response_model = api.model('ProgressoResponse', {
    'estudanteId': fields.String,
    'estrelas': fields.Integer,
    'niveis': fields.List(fields.Nested(nivel_progresso_model)),
    'conquistas': fields.List(fields.Nested(conquista_model)),
})

concluir_licao_model = api.model('ConcluirLicao', {
    'categoriaId': fields.String(required=True),
    'nivelId': fields.String(required=True),
})

concluir_response_model = api.model('ConcluirResponse', {
    'estrelas_ganhas': fields.Integer,
    'conquista': fields.String,
    'ja_concluida': fields.Boolean,
})

NOMES_NIVEL = {'1': 'Básico', '2': 'Reconhecimento', '3': 'Intermediário'}


def _gerar_matricula():
    """Gera matrícula no formato ALF-YYYY-NNNN."""
    ano = datetime.utcnow().year
    ultimo = Aluno.query.order_by(Aluno.id.desc()).first()
    proximo_num = (ultimo.id + 1) if ultimo else 1
    return f"ALF-{ano}-{proximo_num:04d}"


def _montar_progresso(aluno):
    """Monta resposta de progresso no formato esperado pelo frontend."""
    registros = ProgressoNivel.query.filter_by(id_aluno=aluno.id).all()

    niveis = []
    conquistas = []
    total_estrelas = 0

    for reg in registros:
        licao = reg.licao
        nivel_id = str(licao.nivel)
        categoria_id = licao.id_categoria

        niveis.append({
            'categoriaId': categoria_id,
            'nivelId': nivel_id,
            'concluido': True,
            'estrelas': reg.estrelas,
        })

        nome_nivel = NOMES_NIVEL.get(nivel_id, f'Nível {nivel_id}')
        categoria = Categoria.query.get(categoria_id)
        nome_categoria = categoria.nome if categoria else categoria_id

        conquistas.append({
            'id': f'{categoria_id}-{nivel_id}',
            'nome': f'{nome_categoria} — {nome_nivel}',
            'categoriaId': categoria_id,
            'nivelId': nivel_id,
            'desbloqueada': True,
        })

        total_estrelas += reg.estrelas

    return {
        'estudanteId': str(aluno.id),
        'estrelas': total_estrelas,
        'niveis': niveis,
        'conquistas': conquistas,
    }


# --- Endpoints ---

@ns_alunos.route('/login')
class AlunoLogin(Resource):
    @ns_alunos.expect(aluno_login_model)
    def post(self):
        """Login de aluno por matrícula."""
        data = request.get_json()
        matricula = data.get('matricula', '').strip()

        if not matricula:
            return {'message': 'Matrícula é obrigatória'}, 400

        aluno = Aluno.query.filter_by(matricula=matricula).first()
        if not aluno:
            return {'message': 'Matrícula não encontrada'}, 404

        return {
            'id': aluno.id,
            'nome': aluno.nome,
            'matricula': aluno.matricula,
            'idade': aluno.idade,
        }, 200


@ns_alunos.route('/cadastro')
class AlunoCadastro(Resource):
    @jwt_required()
    @ns_alunos.expect(aluno_cadastro_model)
    def post(self):
        """Cadastro de novo aluno (requer autenticação de professor)."""
        data = request.get_json()

        nome = data.get('nome', '').strip()
        cpf = data.get('cpf', '').strip()
        idade = data.get('idade')

        # Validações
        if not nome or not cpf or idade is None:
            return {'message': 'Todos os campos são obrigatórios (nome, cpf, idade)'}, 400

        pattern_cpf = r'^\d{3}\.\d{3}\.\d{3}-\d{2}$'
        if not re.match(pattern_cpf, cpf):
            return {'message': 'CPF deve estar no formato 000.000.000-00'}, 400

        if not (3 <= idade <= 12):
            return {'message': 'Idade deve estar entre 3 e 12 anos'}, 400

        if Aluno.query.filter_by(cpf=cpf).first():
            return {'message': 'CPF já cadastrado'}, 409

        try:
            matricula = _gerar_matricula()
            aluno = Aluno(nome=nome, matricula=matricula, cpf=cpf, idade=idade)
            db.session.add(aluno)
            db.session.commit()

            return {
                'id': aluno.id,
                'nome': aluno.nome,
                'matricula': aluno.matricula,
                'idade': aluno.idade,
            }, 201
        except IntegrityError:
            db.session.rollback()
            return {'message': 'Erro ao cadastrar aluno'}, 500


@ns_alunos.route('/<int:id_aluno>/progresso')
class AlunoProgresso(Resource):
    @jwt_required()
    def get(self, id_aluno):
        """Retorna progresso completo do aluno."""
        aluno = Aluno.query.get(id_aluno)
        if not aluno:
            return {'message': 'Aluno não encontrado'}, 404

        return _montar_progresso(aluno), 200


@ns_alunos.route('/<int:id_aluno>/progresso/concluir')
class AlunoConcluirLicao(Resource):
    @jwt_required()
    @ns_alunos.expect(concluir_licao_model)
    def post(self, id_aluno):
        """Registra conclusão de lição para o aluno."""
        aluno = Aluno.query.get(id_aluno)
        if not aluno:
            return {'message': 'Aluno não encontrado'}, 404

        data = request.get_json()
        categoria_id = data.get('categoriaId', '').strip()
        nivel_id = data.get('nivelId', '').strip()

        if not categoria_id or not nivel_id:
            return {'message': 'categoriaId e nivelId são obrigatórios'}, 400

        # Buscar a lição correspondente
        licao_id = f'{categoria_id}-{nivel_id}'
        licao = Licao.query.get(licao_id)
        if not licao:
            return {'message': 'Lição não encontrada'}, 404

        # Verificar se já concluiu
        existente = ProgressoNivel.query.filter_by(
            id_aluno=aluno.id, id_licao=licao_id
        ).first()

        if existente:
            return {'estrelas_ganhas': 0, 'conquista': None, 'ja_concluida': True}, 200

        # Calcular estrelas (nível 1=1, 2=2, 3=3)
        estrelas = licao.nivel

        # Registrar progresso
        progresso = ProgressoNivel(
            id_aluno=aluno.id,
            id_licao=licao_id,
            estrelas=estrelas,
        )
        db.session.add(progresso)
        db.session.commit()

        categoria = Categoria.query.get(categoria_id)
        nome_categoria = categoria.nome if categoria else categoria_id
        nome_nivel = NOMES_NIVEL.get(nivel_id, f'Nível {nivel_id}')
        conquista_nome = f'{nome_categoria} — {nome_nivel}'

        return {
            'estrelas_ganhas': estrelas,
            'conquista': conquista_nome,
            'ja_concluida': False,
        }, 200
