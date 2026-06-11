# TURMA NOITE 2026-1

GRUPO:

*   Lucas José
*   Pedro Henrique
*   Alexsandro correia
*   Lucas Henrique Gomes da Silva
*   João Lucas Silverio de Santana


# Exploradores do Espaço: Jornada do Conhecimento Estelar

## Solução Tecnológica para Educação Hospitalar no IMIP

Este projeto apresenta uma solução tecnológica gamificada, desenvolvida para proporcionar educação e entretenimento a crianças hospitalizadas no IMIP (Instituto de Medicina Integral Professor Fernando Figueira). Através de uma jornada espacial interativa, o sistema oferece desafios de conhecimento em diversas áreas, adaptando-se ao progresso do "Comandante" (a criança).

## Funcionalidades

*   **Perfil do Comandante:** Criação de um perfil anônimo para cada criança, com um "título épico" gerado aleatoriamente e acompanhamento de experiência (XP) e missões concluídas.
*   **Desafios Interativos:** Perguntas em diversas disciplinas (Matemática, Português, Ciências, História, Geografia, Inglês) com três níveis de dificuldade (Fácil, Médio, Difícil).
*   **Progressão Adaptativa:** O sistema seleciona desafios inéditos e ajusta o nível de dificuldade com base na experiência acumulada pelo Comandante.
*   **Interface Lúdica:** Uma interface de console simples, mas envolvente, que simula um computador de bordo de uma nave espacial.
*   **Privacidade e Segurança (LGPD):** O design da arquitetura em camadas e o uso de IDs anônimos garantem a proteção dos dados sensíveis dos pacientes.

## Arquitetura do Projeto

O projeto adota um **Estilo Arquitetural em Camadas (Layered Architecture)**, visando segurança, escalabilidade e modularidade. As camadas são:

1.  **Camada de Dados (Perfil do Paciente):** Gerencia os perfis dos comandantes, incluindo seus interesses, experiência e missões concluídas. Utiliza IDs anônimos para conformidade com a LGPD.
2.  **Camada de Conteúdo (Banco de Conteúdo Multidisciplinar):** Armazena as perguntas e respostas categorizadas por tema e nível de dificuldade.
3.  **Camada de Serviços (Módulo de IA Generativa):** Responsável por selecionar desafios inéditos e adaptados ao perfil e nível de experiência do Comandante.
4.  **Camada de Lógica (Subsistema de Progresso Pedagógico):** Registra o sucesso nas missões, atualiza a experiência do Comandante e gerencia o progresso.
5.  **Camada de Interface (Módulo de Acolhimento Lúdico):** Interage diretamente com o usuário, apresentando as perguntas e processando as respostas.

### Fluxo de Dados

A coordenação entre os componentes permite um fluxo de feedback instantâneo:

*   **Atualização de XP:** Pontos de experiência são concedidos ao Comandante após cada missão bem-sucedida.
*   **Registro de ID Único:** Cada pergunta respondida com sucesso é registrada para evitar repetições.
*   **Liberação de Nova Missão:** O sistema seleciona dinamicamente novas missões com base no progresso do Comandante.

## Estrutura de Pastas

```
GrupoStarGuardian/
├── Trabalho de Cloves/
│   ├── Código/
│   │   ├── main.py    # Código principal da aplicação
│   │  
│   └── Slides/
│       └── Exploradores_do_Espaço_Jornada_do_Conhecimento_Estelar_no_IMIP.pdf # Apresentação do projeto
└── README.md              # Este arquivo
```

## Como Executar o Projeto

Para executar o projeto, siga os passos abaixo:

1.  **Pré-requisitos:** Certifique-se de ter o Python 3 instalado em seu sistema.

2.  **Navegue até o diretório do código:**
    ```bash
    cd GrupoStarGuardian/Trabalho de Cloves/Código
    ```

3.  **Execute o script principal:**
    ```bash
    python3 "main.py"
    ```


4.  **Interaja com o jogo:** Siga as instruções no console para responder às perguntas e avançar na jornada espacial.

## Tecnologias Utilizadas

*   **Python 3:** Linguagem de programação principal.
*   **Módulos Padrão do Python:** `random` (para seleção aleatória de perguntas e geração de títulos), `uuid` (para geração de IDs anônimos), `time` (para possíveis delays ou simulações de tempo, embora não explicitamente usado no loop principal).

## Créditos

**Autores:** Grupo Star Guardian
**Desenvolvido para:** IMIP (Instituto de Medicina Integral Professor Fernando Figueira)
**Contexto:** Desafio IMIP | Arquitetura de Software e Humanização

---

