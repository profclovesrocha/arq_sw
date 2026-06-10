def test_get_clinics_list(client):
    """Garante que a API de clínicas lista os dados corretamente."""
    response = client.get('/api/clinics')
    
    assert response.status_code == 200
    assert response.is_json
    # garante que o retorno é uma lista (mesmo que vazia no início)
    assert isinstance(response.json, list)