# DATAS DAS ENTREGAS:
- DESAFIO 1: 05/MAR/2026
- DESAFIO 2: 19/MAR/2026 (da AULA 4) - 17/MAR TURMA NOITE
- DESAFIO 3: 26/MAR/2026 (da AULA 5) - 24/MAR TURMA NOITE
- DESAFIO 4: 16/ABR/2026 (da AULA 6) - 14/ABR TURMA NOITE
- DESAFIO FINAL: 09/JUNHO/2026 [NOITE] / 11/JUNHO/2026 [NOITE]

### 🏛️ Seminário Final: Arquitetura do Sistema de Apoio à Decisão Pedagógica (IMIP)

**Equipes:** Até 5 integrantes.
**Cenário:** O IMIP necessita de um sistema robusto para gerenciar trilhas de alfabetização personalizadas por IA para crianças internadas, garantindo humanização e segurança de dados.

#### 📋 1. Estrutura do Trabalho (O que deve ser apresentado)

As equipes devem projetar e apresentar a solução dividida em quatro eixos principais:

**A. Definição Estratégica e Estilo Arquitetural (Aulas 1 e 4)**
*   **Escolha do Estilo:** Justificar a escolha entre uma arquitetura **em camadas**, **microsserviços** ou **orientada a eventos**.
*   **Visões Arquiteturais:** Apresentar a visão lógica do sistema, destacando como ele atende requisitos de qualidade como **disponibilidade** e **segurança (LGPD)**.

**B. Design de Componentes e Conectores (Aulas 2 e 3)**
*   **Componentização:** Descrever os blocos essenciais, como o **Módulo de IA Generativa**, o **Subsistema de Relatórios Pedagógicos** e o **Módulo de Acolhimento Lúdico**.
*   **Estratégia de Conexão:** Definir onde será usada **comunicação síncrona** (ex: login do professor via Chamada de Procedimento) e onde será **assíncrona** (ex: geração de imagens por IA via Troca de Mensagens).

**C. Implementação e Estrutura em Flask (Aula 5)**
*   **Padrão MVC + Blueprint:** Demonstrar como o projeto seria organizado fisicamente (diretório `blueprints/`, `models.py`, `app.py`).
*   **Modelagem de Usuários:** Detalhar a entidade `User` (professores e extensionistas), incluindo o uso de **hashing bcrypt** para segurança de senhas.

**D. Princípios Avançados e Evolução (Aula 6)**
*   **Clean/Hexagonal Architecture:** Explicar como a lógica de negócio (o processo pedagógico) será isolada de ferramentas externas (o banco de dados ou a API de IA), usando **portas e adaptadores**.

#### 📽️ 2. Formato da Apresentação
1.  **Pitch Inicial (5 min):** Apresentação do problema no contexto do IMIP.
2.  **Defesa Arquitetural (15 min):** Explicação dos diagramas de componentes, conectores e escolha do padrão Flask/MVC.
3.  **Rationale e Trade-offs (5 min):** Justificativa das decisões técnicas (ex: "por que escolhemos comunicação assíncrona para a IA?").
4.  **Sessão de Perguntas (5 min).**

---

#### ⚖️ 3. Critérios de Avaliação (Rubrica)

| Critério | Descrição | Peso |
| :--- | :--- | :--- |
| **Coerência Técnica** | Aplicação correta dos conceitos de componentes, conectores e estilos arquiteturais. | 30% |
| **Qualidade da Estrutura** | Organização do projeto seguindo padrões profissionais (Blueprints, App Factory, Migrations). | 25% |
| **Robustez e Segurança** | Demonstração de proteção de dados (LGPD), tratamento de senhas e atributos de qualidade. | 20% |
| **Humanização e Inovação** | Como a arquitetura facilita a co-criação narrativa e o acolhimento da criança no IMIP. | 15% |
| **Apresentação e Rationale** | Capacidade de justificar decisões técnicas e balancear trade-offs complexos. | 10% |

---

#### 🛠️ Ferramentas Sugeridas para o Projeto
*   **Modelagem:** Draw.io, UML ou C4 Model.
*   **Protótipo de Código:** IDE Online Replit para anatomia de uma aplicação Flask.
*   **Gestão de Código:** GitHub para versionamento e colaboração em equipe.

**Dica para os Estudantes:** Foquem na **modularidade** (baixo acoplamento entre os módulos hospitalares e educacionais) para facilitar a manutenção futura do sistema.
  
# SUGESTÃO - FERRAMENTAS COMPLEMENTAR
- Flask: https://flask.palletsprojects.com/en/stable/
- Selenium: https://www.selenium.dev/
- ou outras para testes.

# SUGESTÃO - Desafios para Smart City 
- https://docs.google.com/document/d/1C0nNNBLqCDSXJoIcvWlhaoC26HUpmbETfKGtKsIpeJs/edit?usp=sharing
- StoryBee: Análise Completa do Gerador de Histórias Infantis por IA para o Brasil https://skywork.ai/skypage/pt/storybee-ai-story-generator/1988079527933714432
- IA Generativa na Educação: Personalizando Histórias para Facilitar o Aprendizado de Leitura em Crianças https://sol.sbc.org.br/index.php/sbie/article/view/31364
- EXEMPLOS DE PROJETOS PRONTOS: https://github.com/clovesrocha/app-ideias
