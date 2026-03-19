Documento Técnico – Arquitetura e Decisões de Projeto
## 1. Diagrama Arquitetural
O sistema desenvolvido adota uma arquitetura do tipo cliente-servidor, estruturada em três
camadas principais: front-end, back-end e banco de dados. Essa organização permite a separação
de responsabilidades, promovendo maior manutenibilidade e escalabilidade do sistema.
No front-end, foram utilizadas tecnologias como HTML, CSS e JavaScript, responsáveis pela
interface com o usuário, incluindo telas de autenticação, interação dos alunos com os jogos e
visualização de desempenho por parte dos professores.
O back-end foi desenvolvido utilizando o framework Flask, em Python, sendo responsável pela
lógica de negócio, gerenciamento de sessões, autenticação de usuários e comunicação com o
banco de dados.
O banco de dados utilizado foi o SQLite, escolhido por sua simplicidade e facilidade de integração,
sendo responsável pelo armazenamento de informações como dados dos usuários e pontuações
dos alunos.
A comunicação entre as camadas ocorre por meio de requisições HTTP, sendo os dados
trafegados em formato JSON, permitindo atualização dinâmica das informações na interface do
usuário.

## 2. Documento de Rationale
As decisões técnicas adotadas no desenvolvimento deste projeto foram orientadas por critérios de
simplicidade, eficiência e adequação ao contexto educacional.
O uso do framework Flask foi motivado por sua leveza e facilidade de aprendizagem, possibilitando
a implementação rápida de funcionalidades essenciais, como autenticação e criação de rotas.
A escolha do SQLite como sistema de gerenciamento de banco de dados deve-se à sua natureza
embarcada, dispensando a necessidade de configuração de servidores adicionais, o que o torna
adequado para aplicações de pequeno porte.
A separação entre usuários do tipo aluno e professor foi implementada com o objetivo de
proporcionar diferentes níveis de acesso e funcionalidades, permitindo uma experiência mais
organizada e funcional.
O uso de JavaScript com requisições assíncronas (fetch) possibilita a atualização dinâmica dos
dados, melhorando a experiência do usuário ao evitar recarregamentos desnecessários da página.
Adicionalmente, o sistema contribui para a humanização do cuidado ao promover uma abordagem
lúdica no processo de aprendizagem, incentivando o engajamento e permitindo o
acompanhamento individual do desempenho dos alunos.

## 3. Análise de Trade-offs
Durante o desenvolvimento do sistema, foram identificados diversos trade-offs entre segurança,
desempenho e simplicidade de implementação.
No que se refere à segurança, optou-se inicialmente por armazenar senhas em formato simples,
priorizando a facilidade de implementação. Contudo, reconhece-se que a utilização de técnicas de
hash seria mais adequada em um ambiente de produção.
Em relação ao banco de dados, o SQLite foi escolhido por sua praticidade, embora apresente
limitações de escalabilidade quando comparado a soluções mais robustas, como PostgreSQL.
Outro ponto relevante foi a substituição do uso de armazenamento local (localStorage) pelo banco
de dados, visando maior consistência e confiabilidade das informações.
Por fim, a escolha por requisições HTTP tradicionais em detrimento de tecnologias como
WebSockets reflete a busca por um equilíbrio entre funcionalidade e complexidade, mantendo o
sistema simples e eficiente.
Conclui-se que as decisões adotadas permitem o funcionamento adequado do sistema no contexto
proposto, ao mesmo tempo em que possibilitam futuras evoluções para atender demandas mais
complexas.
