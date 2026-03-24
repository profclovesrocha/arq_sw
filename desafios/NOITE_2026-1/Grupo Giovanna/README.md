# [cite_start]Documentação: Plataforma Eve [cite: 1]

## [cite_start]RESUMO [cite: 2]
[cite_start]Este documento apresenta o protótipo para o projeto de Arquitetura de Software, focado na análise da defasagem da socialização, sincretismo cultural e vida noturna na cidade do Recife[cite: 3]. [cite_start]A proposta utiliza princípios de *Smart City* para estimular interações interpessoais e culturais na região[cite: 4].

---

## [cite_start]1. INTRODUÇÃO [cite: 5]
* [cite_start]**Contexto:** Na década de 90, movimentos como o Manguebeat e a Noite Cubana colocaram Recife em um holofote cultural nacional e internacional[cite: 6, 7].
* [cite_start]**Declínio:** Fatores como o fechamento de comércios, insegurança e a pandemia de 2020 contribuíram para a queda das interações sociais[cite: 8, 9].
* [cite_start]**Impactos:** A escassez de atividades socioculturais gera impactos diretos na economia, na saúde mental e no desenvolvimento cognitivo da população[cite: 10].

---

## [cite_start]2. PROPOSTA [cite: 11]
* [cite_start]**Mediador Digital:** A plataforma conecta cidadãos a eventos culturais e espaços urbanos para promover a visibilidade da temporada cultural atual[cite: 13].
* [cite_start]**HotSpots Culturais:** Utiliza geolocalização para criar um ambiente interativo onde pontos no mapa representam eventos e manifestações culturais[cite: 14, 15].
* [cite_start]**Personalização:** Algoritmos de recomendação analisam preferências individuais (gênero, caráter do evento) para sugerir experiências ativas[cite: 16, 17].
* [cite_start]**Integração:** Conexão com APIs externas de venda de ingressos e agendas institucionais para garantir dados sempre atualizados[cite: 20].

---

## [cite_start]3. METODOLOGIA [cite: 23]
[cite_start]O desenvolvimento segue uma abordagem **modular** dividida em duas frentes principais[cite: 24]:

1. [cite_start]**Base do Mapa:** Desenvolvimento de núcleo interativo usando HTML, CSS, JavaScript e bibliotecas como Leaflet ou Google Maps API[cite: 26, 27]. [cite_start]Foco em usabilidade (UX/UI) e informações detalhadas por evento[cite: 28, 29].
2. [cite_start]**Integração Backend:** Uso de **Flask** para a coleta automatizada de dados de plataformas externas (ex: Ticketmaster) e bases governamentais[cite: 30, 31].

---

## [cite_start]4. ARQUITETURA [cite: 32]
[cite_start]Adota-se o **Modelo em Camadas** para organizar os níveis de responsabilidade do sistema[cite: 33]:

* [cite_start]**Separação de Preocupações:** Divisão clara entre interface, processamento e persistência de dados[cite: 36].
* [cite_start]**Desenvolvimento Incremental:** Estrutura que facilita a adição de novas funcionalidades no futuro[cite: 38].
* [cite_start]**Autonomia de Serviços:** O isolamento na Camada de Serviço garante que mudanças em APIs externas exijam alterações apenas em funções específicas, sem comprometer o sistema todo[cite: 39, 40].

---

## [cite_start]5. COMPONENTES [cite: 41]

### [cite_start]Serviço de Mapa de Eventos [cite: 42]
* [cite_start]**Responsabilidade:** Renderizar interface cartográfica interativa com eventos em tempo real[cite: 44].
* [cite_start]**Tecnologias:** Leaflet.js e Jinja2[cite: 45].

### [cite_start]Módulo de "Catálogo" de Eventos [cite: 46]
* [cite_start]**Responsabilidade:** Ingestão de dados e normalização de campos (data, preço, local) vindos de fontes distintas[cite: 47, 48].
* [cite_start]**Recomendação:** Motor de filtragem que cruza categorias de eventos com o histórico do usuário[cite: 49].

### [cite_start]Classe de Perfil de Usuário [cite: 50]
* [cite_start]**Responsabilidade:** Gerenciar estado, credenciais e preferências de forma encapsulada (OO)[cite: 51].
* [cite_start]**Destaque:** Serve como ponte entre o banco de dados e o motor de recomendação[cite: 52].

### [cite_start]Módulo de Rede Social [cite: 53]
* [cite_start]**Responsabilidade:** Gerenciar conexões e microcomunidades[cite: 54].
* [cite_start]**Funcionalidades:** Troca de informações em grupos de interesse e Mural de Discussão para caronas e dúvidas sobre eventos[cite: 55, 57, 58].