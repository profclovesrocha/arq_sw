from unittest.mock import patch

def test_get_free_schedules_success(client):
    """Testa a listagem geral de horários livres disponíveis."""
    mock_schedules = [
        {"id": 10, "data": "2026-06-15", "hora": "14:00", "medico": "Dr. Silva"}
    ]
    
    with patch('controllers.schedule_controller.get_schedules_data') as mock_get:
        mock_get.return_value = mock_schedules
        response = client.get('/api/free_schedules')
        
    assert response.status_code == 200
    assert response.is_json

def test_get_filtered_schedules_search(client):
    """Testa a rota de busca de horários filtrados passando parâmetros na URL."""
    # simula o envio de filtros na URL
    query_params = {"data": "2026-06-15", "especialidade": "1"}
    
    with patch('controllers.schedule_controller.get_filtered_schedules') as mock_filter:
        mock_filter.return_value = [] # simula que não achou nada para esses filtros, mas respondeu 200
        response = client.get('/api/filtered_schedules/search', query_string=query_params)
        
    assert response.status_code == 200

def test_get_patient_schedules_search(client):
    """Testa a busca de agendamentos vinculados a um paciente específico."""
    
    query_params = {"patient_id": "1"}
    
    with patch('controllers.schedule_controller.get_patient_schedules') as mock_patient_schedules:
        mock_patient_schedules.return_value = [{"id_consulta": 1, "status": "Confirmado"}]
        response = client.get('/api/schedule_by_patient/search', query_string=query_params)
        
    assert response.status_code == 200
    assert response.is_json