import requests
import json

BASE = 'http://127.0.0.1:5001'

# 1. Login professor
print('=== Login Professor ===')
r = requests.post(f'{BASE}/professores/login', json={'matricula': 'PROF-001', 'senha': '123456'})
print(f'Status: {r.status_code}')
data = r.json()
print(json.dumps(data, indent=2, ensure_ascii=False))
token = data.get('token')

headers = {'Authorization': f'Bearer {token}'}

# 2. Cadastro aluno
print('\n=== Cadastro Aluno ===')
r = requests.post(f'{BASE}/alunos/cadastro', json={'nome': 'Maria', 'cpf': '123.456.789-00', 'idade': 6}, headers=headers)
print(f'Status: {r.status_code}')
print(json.dumps(r.json(), indent=2, ensure_ascii=False))

# 3. Login aluno
print('\n=== Login Aluno ===')
r = requests.post(f'{BASE}/alunos/login', json={'matricula': 'ALF-2026-0001'})
print(f'Status: {r.status_code}')
print(json.dumps(r.json(), indent=2, ensure_ascii=False))

# 4. Get categorias
print('\n=== Categorias ===')
r = requests.get(f'{BASE}/categorias/', headers=headers)
print(f'Status: {r.status_code}')
print(json.dumps(r.json(), indent=2, ensure_ascii=False))

# 5. Get licao
print('\n=== Licao vogais/1 ===')
r = requests.get(f'{BASE}/licoes/vogais/1', headers=headers)
print(f'Status: {r.status_code}')
resp = r.json()
titulo = resp.get('titulo')
steps = resp.get('steps', [])
print(f'Titulo: {titulo}')
print(f'Steps: {len(steps)}')

# 6. Concluir licao
print('\n=== Concluir Licao ===')
r = requests.post(f'{BASE}/alunos/1/progresso/concluir', json={'categoriaId': 'vogais', 'nivelId': '1'}, headers=headers)
print(f'Status: {r.status_code}')
print(json.dumps(r.json(), indent=2, ensure_ascii=False))

# 7. Get progresso
print('\n=== Progresso ===')
r = requests.get(f'{BASE}/alunos/1/progresso', headers=headers)
print(f'Status: {r.status_code}')
print(json.dumps(r.json(), indent=2, ensure_ascii=False))

# 8. Professor lista alunos
print('\n=== Professor - Lista Alunos ===')
r = requests.get(f'{BASE}/professores/alunos', headers=headers)
print(f'Status: {r.status_code}')
print(json.dumps(r.json(), indent=2, ensure_ascii=False))

# 9. Concluir mesma licao (repetição)
print('\n=== Repetir Licao (deve retornar ja_concluida) ===')
r = requests.post(f'{BASE}/alunos/1/progresso/concluir', json={'categoriaId': 'vogais', 'nivelId': '1'}, headers=headers)
print(f'Status: {r.status_code}')
print(json.dumps(r.json(), indent=2, ensure_ascii=False))
