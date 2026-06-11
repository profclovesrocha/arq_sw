from adapters.ia_provider.openai_adapter import OpenAIAdapter

class IAService:
    def __init__(self, provider=None):
        self.provider = provider or OpenAIAdapter()

    def gerar_conteudo(self, perfil):
        historia   = self.provider.gerar_historia(perfil)
        atividades = self.provider.gerar_atividades(perfil)
        return historia, atividades
