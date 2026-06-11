from repositories.trilha_repository import TrilhaRepository, AlunoRepository
from repositories.atividade_repository import AtividadeRepository
from models import Trilha, Atividade
from services.ia_service import IAService

class TrilhaService:
    MAPA_NIVEL = {
        "pre-silabico":  "iniciante",
        "silabico":      "iniciante",
        "silabico-alfa": "intermediario",
        "alfabetico":    "avancado",
    }

    def __init__(self):
        self.repo_t  = TrilhaRepository()
        self.repo_a  = AlunoRepository()
        self.repo_at = AtividadeRepository()
        self.ia      = IAService()

    def criar_trilha(self, aluno_id, professor_id, titulo):
        aluno = self.repo_a.buscar_por_id(aluno_id)
        if not aluno:
            raise ValueError("Aluno nao encontrado.")
        nivel  = self.MAPA_NIVEL.get(aluno.nivel_atual, "iniciante")
        perfil = {"nome": aluno.nome, "idade": aluno.idade, "nivel": nivel}

        trilha = Trilha(titulo=titulo, nivel=nivel,
                        professor_id=professor_id, aluno_id=aluno_id)
        self.repo_t.salvar(trilha)

        historia, atividades_ia = self.ia.gerar_conteudo(perfil)
        self.repo_at.salvar(Atividade(
            titulo=f"Historia: {aluno.nome}", tipo="historia",
            conteudo=historia, ordem=1, trilha_id=trilha.id))
        for i, at in enumerate(atividades_ia, start=2):
            self.repo_at.salvar(Atividade(
                titulo=at["titulo"], tipo=at["tipo"],
                conteudo=at["conteudo"], ordem=i, trilha_id=trilha.id))
        return trilha

    def listar_por_professor(self, pid):
        return self.repo_t.listar_por_professor(pid)

    def buscar_por_id(self, tid):
        return self.repo_t.buscar_por_id(tid)

    def deletar(self, tid):
        self.repo_t.deletar(tid)
