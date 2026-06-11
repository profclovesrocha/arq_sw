class IAProvider:
    """Porta da Arquitetura Hexagonal — interface abstrata para IA."""
    def gerar_historia(self, perfil): raise NotImplementedError
    def gerar_atividades(self, perfil): raise NotImplementedError
