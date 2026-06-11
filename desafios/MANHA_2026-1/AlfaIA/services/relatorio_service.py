from repositories.trilha_repository import TrilhaRepository, AlunoRepository
from repositories.atividade_repository import AtividadeRepository

class RelatorioService:
    def __init__(self):
        self.repo_t  = TrilhaRepository()
        self.repo_a  = AlunoRepository()
        self.repo_at = AtividadeRepository()

    def progresso_aluno(self, aluno_id):
        aluno   = self.repo_a.buscar_por_id(aluno_id)
        trilhas = self.repo_t.listar_por_aluno(aluno_id)
        total, concluidas = 0, 0
        for t in trilhas:
            ats = self.repo_at.buscar_por_trilha(t.id)
            total += len(ats)
            concluidas += sum(1 for a in ats if a.concluida)
        pct = round(concluidas / total * 100, 1) if total else 0
        return {"aluno": aluno, "trilhas": trilhas,
                "total": total, "concluidas": concluidas, "percentual": pct}

    def listar_alunos(self):
        return self.repo_a.listar_ativos()
