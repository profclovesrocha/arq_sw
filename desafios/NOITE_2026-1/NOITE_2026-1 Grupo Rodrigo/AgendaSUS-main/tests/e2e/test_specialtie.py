from unittest.mock import patch

def test_get_specialties_data_success(client):
    """Testa se a API retorna a lista de especialidades corretamente em formato JSON."""
    
    # dados fictícios para simular o que viria do banco de dados
    mock_data = [
        {"id": 1, "name": "Cardiologia"},
        {"id": 2, "name": "Pediatria"}
    ]
    
    # intercepta a função do controller que busca as especialidades
    with patch('controllers.specialtie_controller.get_specialties_data') as mock_get:
        # força o controller a retornar a nossa lista simulada em vez de ir ao banco
        mock_get.return_value = mock_data
        
        response = client.get('/api/specialties')
    
    # validações da resposta da API
    assert response.status_code == 200
    assert response.is_json
    assert isinstance(response.json, list)