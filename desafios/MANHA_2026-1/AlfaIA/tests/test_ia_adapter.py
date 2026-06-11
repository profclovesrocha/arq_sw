from adapters.ia_provider.openai_adapter import MockIAAdapter
from adapters.ia_provider import IAProvider
from services.ia_service import IAService

def test_mock_gera_historia():
    svc = IAService(provider=MockIAAdapter())
    h, _ = svc.gerar_conteudo({"nome": "Ana", "idade": 7, "nivel": "iniciante"})
    assert isinstance(h, str) and len(h) > 0

def test_porta_abstrata():
    p = IAProvider()
    try:
        p.gerar_historia({})
        assert False
    except NotImplementedError:
        pass
