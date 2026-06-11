from models import Trilha, Aluno
from extensions import db

class TrilhaRepository:
    def salvar(self, trilha):
        db.session.add(trilha)
        db.session.commit()
        return trilha
    def buscar_por_id(self, tid):
        return Trilha.query.get(int(tid))
    def listar_por_professor(self, pid):
        return Trilha.query.filter_by(professor_id=pid).order_by(Trilha.criada_em.desc()).all()
    def listar_por_aluno(self, aid):
        return Trilha.query.filter_by(aluno_id=aid).order_by(Trilha.criada_em.desc()).all()
    def deletar(self, tid):
        t = self.buscar_por_id(tid)
        if t:
            db.session.delete(t)
            db.session.commit()

class AlunoRepository:
    def buscar_por_id(self, aid):
        return Aluno.query.get(int(aid))
    def listar_ativos(self):
        return Aluno.query.filter_by(ativo=True).order_by(Aluno.nome).all()
    def salvar(self, aluno):
        db.session.add(aluno)
        db.session.commit()
        return aluno
