from models import Atividade
from extensions import db

class AtividadeRepository:
    def salvar(self, at):
        db.session.add(at)
        db.session.commit()
        return at
    def buscar_por_trilha(self, tid):
        return Atividade.query.filter_by(trilha_id=tid).order_by(Atividade.ordem).all()
    def buscar_por_id(self, aid):
        return Atividade.query.get(int(aid))
    def marcar_concluida(self, aid):
        at = self.buscar_por_id(aid)
        if at:
            at.concluida = True
            db.session.commit()
        return at
