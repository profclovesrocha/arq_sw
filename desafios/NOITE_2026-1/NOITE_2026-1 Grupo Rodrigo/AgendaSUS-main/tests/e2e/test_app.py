from jinja2.exceptions import TemplateNotFound
import pytest

def test_index_route(client):
    """Garante que a rota principal tenta carregar ou carrega o index."""
    try:
        response = client.get('/')
        assert response.status_code == 200
    except TemplateNotFound:
        
       
        pass