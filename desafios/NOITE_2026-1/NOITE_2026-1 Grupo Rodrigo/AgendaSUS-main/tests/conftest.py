import pytest
import sys
import os

# 1. Captura o caminho absoluto de onde o arquivo conftest.py está (pasta tests)
diretorio_testes = os.path.dirname(os.path.abspath(__file__))

# 2. Sobe para a raiz do projeto (AgendaSUS)
raiz_projeto = os.path.abspath(os.path.join(diretorio_testes, ".."))

# 3. Aponta diretamente para a pasta backend
pasta_backend = os.path.abspath(os.path.join(raiz_projeto, "backend"))

# 4. Adiciona ao sistema do Python para ele reconhecer os módulos internos
if pasta_backend not in sys.path:
    sys.path.insert(0, pasta_backend)

from App import app as flask_app

@pytest.fixture
def app():
    flask_app.config.update({
        "TESTING": True,
    })
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()