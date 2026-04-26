import os
import sqlite3
from flask import Flask, render_template, jsonify
import requests
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

app = Flask(__name__)

# --- EXPLICAÇÃO DO BACK-END ---
# 1. Flask: Micro-framework que gerencia as rotas (URLs).
# 2. Requests: Biblioteca para fazer chamadas HTTP para APIs externas.
# 3. Rota '/': Renderiza a página principal.
# 4. Rota '/api/eventos': Busca no banco de dados primeiro. Se vazio, vai na API.

# --- CONFIGURAÇÃO DO BANCO DE DADOS ---
def init_db():
    conn = sqlite3.connect('eventos.db')
    cursor = conn.cursor()
    # Cria a tabela caso ela não exista
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS eventos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            lat REAL,
            lng REAL,
            data TEXT,
            local TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Inicializa o banco ao iniciar a aplicação
init_db()

def buscar_eventos_api():
    """
    Busca eventos do banco de dados. Se o banco estiver vazio,
    faz a requisição na API real, salva no banco e retorna os dados.
    """
    conn = sqlite3.connect('eventos.db')
    conn.row_factory = sqlite3.Row # Permite acessar colunas pelo nome (ex: row['nome'])
    cursor = conn.cursor()
    
    # 1. Tenta buscar do banco de dados primeiro
    cursor.execute('SELECT * FROM eventos')
    eventos_db = cursor.fetchall()
    
    if eventos_db:
        print("Dados carregados do Banco de Dados local.")
        conn.close()
        return [dict(row) for row in eventos_db]
        
    # 2. Se o banco estiver vazio, busca da API real
    print("Banco de dados vazio. Buscando na API externa...")
    
    API_KEY = os.getenv("MINHA_CHAVE_API") # Lê a chave do arquivo .env
    API_URL = os.getenv("URL_DA_API", "SUA_URL_DA_API") # Lê a URL do .env
    
    # IMPORTANTE: A forma de enviar a chave varia dependendo de qual API você usa.
    # Exemplo usando Header (comum):
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }
    
    try:
        # --- AQUI É ONDE A MÁGICA ACONTECE ---
        # ATENÇÃO: Adapte esta parte de acordo com a documentação da SUA API real
        
        # response = requests.get(API_URL, headers=headers)
        # response.raise_for_status() # Verifica se a requisição deu erro (ex: 404, 401)
        # dados_api = response.json()
        
        # Simulação temporária de um retorno de API real para você ver funcionando:
        dados_api = [
             { "nome": "Evento 1 da API Real", "lat": -23.5874, "lng": -46.6576, "data": "20/05/2024", "local": "Local A" },
             { "nome": "Evento 2 da API Real", "lat": -23.5505, "lng": -46.6333, "data": "22/05/2024", "local": "Local B" }
        ]
        
        eventos_formatados = []
        
        # 3. Itera sobre os dados da API e salva no banco de dados local
        for item in dados_api: 
            # (Você precisará mapear as chaves corretamente ex: item['name'] ao invés de item['nome'])
            evento = {
                "nome": item.get("nome"),
                "lat": item.get("lat"),
                "lng": item.get("lng"),
                "data": item.get("data"),
                "local": item.get("local")
            }
            
            # Insere no SQLite
            cursor.execute('''
                INSERT INTO eventos (nome, lat, lng, data, local)
                VALUES (?, ?, ?, ?, ?)
            ''', (evento['nome'], evento['lat'], evento['lng'], evento['data'], evento['local']))
            
            eventos_formatados.append(evento)
            
        conn.commit()
        conn.close()
        
        return eventos_formatados
        
    except Exception as e:
        print(f"Erro ao comunicar com a API: {e}")
        conn.close()
        return []

@app.route('/')
def index():
    """Renderiza a interface principal do mapa."""
    return render_template('index.html')

@app.route('/api/eventos')
def get_eventos():
    """Endpoint que retorna os eventos em formato JSON para o JavaScript."""
    eventos = buscar_eventos_api()
    return jsonify(eventos)

# --- TEMPLATE HTML (Incluso no mesmo projeto para fins didáticos) ---
# Em um projeto real, este conteúdo ficaria em templates/index.html
index_html = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mapa de Eventos Local</title>
    
    <!-- Leaflet CSS (Biblioteca de Mapas) -->
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
    
    <style>
        body { margin: 0; padding: 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
        header { 
            background: #2c3e50; color: white; padding: 1rem; text-align: center;
            box-shadow: 0 2px 5px rgba(0,0,0,0.2); position: relative; z-index: 1000;
        }
        #map { 
            height: calc(100vh - 70px); /* Altura total menos o header */
            width: 100%; 
        }
        .popup-content h3 { margin: 0 0 10px 0; color: #e67e22; }
        .popup-content p { margin: 5px 0; font-size: 0.9rem; }
    </style>
</head>
<body>

<header>
    <h1>Explorar Eventos Próximos</h1>
</header>

<div id="map"></div>

<!-- Leaflet JS -->
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

<script>
    // 1. Inicializar o Mapa (Foco em São Paulo como exemplo)
    const map = L.map('map').setView([-23.5505, -46.6333], 13);

    // 2. Adicionar a camada visual do OpenStreetMap
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '© OpenStreetMap contributors'
    }).addTo(map);

    // 3. Função para carregar eventos da nossa API Flask
    async function carregarEventos() {
        try {
            const response = await fetch('/api/eventos');
            const eventos = await response.json();

            eventos.forEach(evento => {
                // Criar um marcador para cada evento
                const marker = L.marker([evento.lat, evento.lng]).addTo(map);
                
                // Conteúdo do balãozinho (Popup)
                const popupContent = `
                    <div class="popup-content">
                        <h3>${evento.nome}</h3>
                        <p><strong>Data:</strong> ${evento.data}</p>
                        <p><strong>Local:</strong> ${evento.local}</p>
                        <button onclick="alert('Inscrição para: ${evento.nome}')" style="width:100%; cursor:pointer; background:#2ecc71; color:white; border:none; padding:5px; border-radius:3px;">
                            Ver Detalhes
                        </button>
                    </div>
                `;
                
                marker.bindPopup(popupContent);
            });
        } catch (error) {
            console.error("Erro ao carregar eventos:", error);
        }
    }

    // Iniciar carregamento
    carregarEventos();
</script>

</body>
</html>
"""

# Nota: Para rodar o Flask, normalmente salvamos o HTML em uma pasta separada.
# Como sou uma IA gerando um exemplo único, aqui está a lógica de como você deve estruturar.

if __name__ == '__main__':
    # Em um ambiente de desenvolvimento local, você criaria a pasta 'templates'
    # e salvaria o conteúdo de index_html lá dentro como index.html.
    import os
    if not os.path.exists('templates'):
        os.makedirs('templates')
    with open('templates/index.html', 'w', encoding='utf-8') as f:
        f.write(index_html)
    
    app.run(debug=True)