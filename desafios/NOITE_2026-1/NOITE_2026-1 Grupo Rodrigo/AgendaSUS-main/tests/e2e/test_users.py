def test_get_users_api(client):
    """Testa se a API de usuários retorna status 200 e o formato correto."""
    response = client.get('/api/users')
    
    assert response.status_code == 200
    # se a resposta for json, você pode validar o conteúdo
    assert response.is_json