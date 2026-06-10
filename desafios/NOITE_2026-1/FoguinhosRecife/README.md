## TURMA NOITE 2026-1

GRUPO:
* Cauã Andrade
* Diogenes Raimundo
* Giovanna Melo
* Laura Marques
* Maria Eduarda Cavalcante
* Tereza Ana Barros
---
# Documentação: Plataforma Eve 

## RESUMO 
Este documento apresenta o protótipo para o projeto de Arquitetura de Software, focado na análise da defasagem da socialização, sincretismo cultural e vida noturna na cidade do Recife. A proposta utiliza princípios de *Smart City* para estimular interações interpessoais e culturais na região.

---

## 1. INTRODUÇÃO
**Contexto:** Na década de 90, movimentos como o Manguebeat e a Noite Cubana colocaram Recife em um holofote cultural nacional e internacional.
**Declínio:** Fatores como o fechamento de comércios, insegurança e a pandemia de 2020 contribuíram para a queda das interações sociais.
**Impactos:** A escassez de atividades socioculturais gera impactos diretos na economia, na saúde mental e no desenvolvimento cognitivo da população.

---

## 2. PROPOSTA 
**Mediador Digital:** A plataforma conecta cidadãos a eventos culturais e espaços urbanos para promover a visibilidade da temporada cultural atual.
**HotSpots Culturais:** Utiliza geolocalização para criar um ambiente interativo onde pontos no mapa representam eventos e manifestações culturais.
**Personalização:** Algoritmos de recomendação analisam preferências individuais (gênero, caráter do evento) para sugerir experiências ativas.
**Integração:** Conexão com APIs externas de venda de ingressos e agendas institucionais para garantir dados sempre atualizados.

---

## 3. METODOLOGIA 
O desenvolvimento segue uma abordagem **modular** dividida em duas frentes principais:

1. **Base do Mapa:** Desenvolvimento de núcleo interativo usando HTML, CSS, JavaScript e bibliotecas como Leaflet ou Google Maps API. Foco em usabilidade (UX/UI) e informações detalhadas por evento.
2. **Integração Backend:** Uso de **Flask** para a coleta automatizada de dados de plataformas externas (ex: Ticketmaster) e bases governamentais.

---

## 4. ARQUITETURA 
Adota-se o **Modelo em Camadas** para organizar os níveis de responsabilidade do sistema:

**Separação de Preocupações:** Divisão clara entre interface, processamento e persistência de dados.
**Desenvolvimento Incremental:** Estrutura que facilita a adição de novas funcionalidades no futuro.
**Autonomia de Serviços:** O isolamento na Camada de Serviço garante que mudanças em APIs externas exijam alterações apenas em funções específicas, sem comprometer o sistema todo.

---

## 5. COMPONENTES 

### Serviço de Mapa de Eventos 
* **Responsabilidade:** Renderizar interface cartográfica interativa com eventos em tempo real.
* **Tecnologias:** Leaflet.js e Jinja2.

### Módulo de "Catálogo" de Eventos 
* **Responsabilidade:** Ingestão de dados e normalização de campos (data, preço, local) vindos de fontes distintas.
* **Recomendação:** Motor de filtragem que cruza categorias de eventos com o histórico do usuário.

### Classe de Perfil de Usuário
* **Responsabilidade:** Gerenciar estado, credenciais e preferências de forma encapsulada (OO).
* **Destaque:** Serve como ponte entre o banco de dados e o motor de recomendação.

### Módulo de Rede Social 
* **Responsabilidade:** Gerenciar conexões e microcomunidades.
* **Funcionalidades:** Troca de informações em grupos de interesse e Mural de Discussão para caronas e dúvidas sobre eventos.