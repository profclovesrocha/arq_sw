from datetime import datetime
from config import db
from werkzeug.security import generate_password_hash, check_password_hash


class Aluno(db.Model):
    __tablename__ = 'aluno'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    matricula = db.Column(db.String(20), unique=True, nullable=False)
    cpf = db.Column(db.String(14), unique=True, nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    criado_em = db.Column(db.DateTime, default=datetime.utcnow)

    # Relacionamentos
    progressos = db.relationship('ProgressoNivel', backref='aluno', lazy=True)


class Professor(db.Model):
    __tablename__ = 'professor'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    matricula = db.Column(db.String(20), unique=True, nullable=False)
    senha_hash = db.Column(db.String(255), nullable=False)
    criado_em = db.Column(db.DateTime, default=datetime.utcnow)

    def set_senha(self, senha):
        self.senha_hash = generate_password_hash(senha)

    def verificar_senha(self, senha):
        return check_password_hash(self.senha_hash, senha)


class Categoria(db.Model):
    __tablename__ = 'categoria'

    id = db.Column(db.String(20), primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    descricao = db.Column(db.String(200), nullable=False)
    icone = db.Column(db.String(10))

    licoes = db.relationship('Licao', backref='categoria', lazy=True)


class Licao(db.Model):
    __tablename__ = 'licao'

    id = db.Column(db.String(30), primary_key=True)
    id_categoria = db.Column(db.String(20), db.ForeignKey('categoria.id'), nullable=False)
    nivel = db.Column(db.Integer, nullable=False)
    titulo = db.Column(db.String(100), nullable=False)

    steps = db.relationship('LicaoStep', backref='licao', lazy=True, order_by='LicaoStep.ordem')

    __table_args__ = (
        db.UniqueConstraint('id_categoria', 'nivel', name='uq_categoria_nivel'),
    )


class LicaoStep(db.Model):
    __tablename__ = 'licao_step'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_licao = db.Column(db.String(30), db.ForeignKey('licao.id'), nullable=False)
    ordem = db.Column(db.Integer, nullable=False)
    tipo = db.Column(db.String(20), nullable=False)

    # Campos para card-informativo
    titulo = db.Column(db.String(100))
    conteudo = db.Column(db.Text)

    # Campos para pergunta
    enunciado = db.Column(db.String(300))

    alternativas = db.relationship('Alternativa', backref='step', lazy=True)

    __table_args__ = (
        db.CheckConstraint("tipo IN ('card-informativo', 'pergunta')", name='chk_tipo_step'),
    )


class Alternativa(db.Model):
    __tablename__ = 'alternativa'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_step = db.Column(db.Integer, db.ForeignKey('licao_step.id'), nullable=False)
    texto = db.Column(db.String(100), nullable=False)
    correta = db.Column(db.Boolean, default=False, nullable=False)


class ProgressoNivel(db.Model):
    __tablename__ = 'progresso_nivel'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_aluno = db.Column(db.Integer, db.ForeignKey('aluno.id'), nullable=False)
    id_licao = db.Column(db.String(30), db.ForeignKey('licao.id'), nullable=False)
    estrelas = db.Column(db.Integer, nullable=False)
    data_conclusao = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    licao = db.relationship('Licao', backref='progressos')

    __table_args__ = (
        db.UniqueConstraint('id_aluno', 'id_licao', name='uq_aluno_licao'),
        db.CheckConstraint('estrelas >= 1 AND estrelas <= 3', name='chk_estrelas'),
    )