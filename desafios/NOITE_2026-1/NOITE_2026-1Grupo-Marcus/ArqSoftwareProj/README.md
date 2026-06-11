## EcoCidade Inteligente 🌿

Sistema web para gestão e incentivo à coleta seletiva, conectando cidadãos e prefeitura para melhorar o controle e a participação na reciclagem urbana.

## 📌 Sobre o projeto

O EcoCidade Inteligente permite que moradores encontrem ecopontos, agendem coleta de recicláveis, acompanhem histórico de reciclagem e recebam notificações sobre coleta no bairro.

Para a gestão pública, o sistema oferece controle de solicitações, monitoramento de bairros e geração de relatórios ambientais.

## 🚀 Funcionalidades
Localização de ecopontos
Agendamento de coleta domiciliar
Histórico de reciclagem do usuário
Sistema de pontos por participação
Notificações de coleta
Painel administrativo para gestão pública

## 🎯 Objetivo

Incentivar a reciclagem e melhorar a gestão de resíduos urbanos por meio da tecnologia, promovendo sustentabilidade e engajamento social.

## 🚀 Tecnologias utilizadas

### 🔧 Backend
- Python 3.x
- Flask
- SQLAlchemy 2.0.30
- Flask-SQLAlchemy 3.1.1
- Flask-Migrate 4.0.7
- Flask-JWT-Extended 4.6.0
- Flask-Mail 0.10.0
- Flask-CORS 4.0.1
- Marshmallow 3.21.3
- Werkzeug 3.0.3

### 🗄️ Banco de dados & mensageria
- Psycopg2-binary 2.9.9
- Redis 5.0.4
- Celery 5.4.0

### ⚙️ Serviços e utilitários
- Requests 2.32.3
- Python-dotenv 1.0.1
- APScheduler 3.10.4
- Geopy 2.4.1
- Google Maps API (googlemaps 4.10.0)
- Bcrypt 4.1.3

---

## 👥 Equipe de desenvolvimento

- Marcus Souza — Backend / API / Arquitetura
- Eduardo Filho — Banco de dados / Integração MySQL
- Helena Nunes — Frontend
- Gabriella Guedes — Frontend / UI/UX
- Prof. Mentor Cloves Rocha 

---

## 🧠 Arquitetura do sistema

O projeto segue uma arquitetura em camadas baseada em API REST, com separação de responsabilidades inspirada no padrão MVC:

- **Models**: definição das entidades e acesso ao banco de dados (SQLAlchemy)
- **Controllers (Routes)**: gerenciamento das rotas e requisições HTTP (Flask)
- **Services**: regras de negócio e processamento da aplicação
- **View**: frontend separado (quando aplicável)

A comunicação entre camadas ocorre via JSON, seguindo o padrão RESTful.
