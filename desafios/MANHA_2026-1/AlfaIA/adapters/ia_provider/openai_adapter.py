import random
from adapters.ia_provider import IAProvider


class OpenAIAdapter(IAProvider):

    # ── HISTÓRIAS POR NÍVEL ─────────────────────────────────────────────
    HISTORIAS = {
        "iniciante": [
            {
                "emoji": "🐱",
                "texto": (
                    "O gato do {nome}\n\n"
                    "{nome} tem um gato.\n"
                    "O gato e malhado.\n"
                    "O gato late? Nao!\n"
                    "O gato mia: miau!\n\n"
                    "{nome} da leite pro gato.\n"
                    "O gato bebe o leite.\n"
                    "O gato fica feliz.\n\n"
                    "A e de abelha.\n"
                    "B e de bola.\n"
                    "C e de casa.\n"
                    "G e de GATO!\n\n"
                    "Muito bem, {nome}! Voce aprendeu a letra G hoje! 🌟"
                )
            },
            {
                "emoji": "🌞",
                "texto": (
                    "O dia do {nome}\n\n"
                    "{nome} acorda cedo.\n"
                    "O sol ja esta no ceu.\n"
                    "O sol e grande e amarelo.\n\n"
                    "{nome} toma o cafe.\n"
                    "Tem pao com manteiga.\n"
                    "Tem leite quentinho.\n\n"
                    "Depois {nome} vai brincar.\n"
                    "Brinca com a bola.\n"
                    "Brinca com o cachorro.\n\n"
                    "S e de SOL.\n"
                    "P e de PAO.\n"
                    "B e de BOLA.\n\n"
                    "Que dia bonito para aprender! ☀️"
                )
            },
            {
                "emoji": "🐸",
                "texto": (
                    "O sapo cantor\n\n"
                    "No lago morava um sapo.\n"
                    "O sapo se chamava {nome}.\n\n"
                    "{nome} cantava todo dia:\n"
                    "A - E - I - O - U!\n\n"
                    "As rãs perguntavam:\n"
                    "— {nome}, o que voce canta?\n\n"
                    "{nome} respondia:\n"
                    "— Canto as vogais!\n"
                    "— A de agua!\n"
                    "— E de estrela!\n"
                    "— I de ilha!\n"
                    "— O de ovo!\n"
                    "— U de uva!\n\n"
                    "As rãs aprenderam as vogais com {nome}. 🐸"
                )
            },
            {
                "emoji": "🎈",
                "texto": (
                    "A festa do {nome}\n\n"
                    "{nome} ganhou uma festa!\n"
                    "Tinha bolo.\n"
                    "Tinha bala.\n"
                    "Tinha balao.\n\n"
                    "O bolo era de chocolate.\n"
                    "A bala era doce.\n"
                    "O balao era vermelho.\n\n"
                    "B e de BOLO.\n"
                    "B e de BALA.\n"
                    "B e de BALAO.\n\n"
                    "Que letra bacana o B! Ele aparece em tudo que e gostoso! 🎂"
                )
            },
            {
                "emoji": "🌧️",
                "texto": (
                    "A chuva de letras\n\n"
                    "Caia uma chuva diferente.\n"
                    "Nao caiam gotas de agua.\n"
                    "Caiam letras do ceu!\n\n"
                    "{nome} abriu a janela.\n"
                    "Uma letra caiu na mao:\n"
                    "Era um A!\n\n"
                    "Depois veio um B.\n"
                    "Depois um C.\n"
                    "Depois um D!\n\n"
                    "{nome} recolheu todas as letras.\n"
                    "Juntou: A + M + O + R.\n"
                    "Formou a palavra: AMOR!\n\n"
                    "E essa foi a primeira palavra de {nome}! ❤️"
                )
            },
        ],

        "intermediario": [
            {
                "emoji": "🦁",
                "texto": (
                    "O leao que aprendeu a ler\n\n"
                    "No meio da selva morava um leao chamado {nome}.\n"
                    "{nome} era o rei dos animais, mas tinha um segredo:\n"
                    "ainda nao sabia ler muito bem.\n\n"
                    "Um dia, {nome} encontrou uma placa no caminho.\n"
                    "A placa dizia: PE-RI-GO!\n\n"
                    "{nome} leu em voz alta: PE... RI... GO...\n"
                    "— PERIGO! — rugiu o leao.\n\n"
                    "Era uma armadilha de cacadores!\n"
                    "Graças a leitura, {nome} se salvou.\n\n"
                    "Desde entao, {nome} praticava leitura todo dia.\n"
                    "Porque ler pode salvar vidas, ate mesmo de um leao! 🦁"
                )
            },
            {
                "emoji": "🚀",
                "texto": (
                    "A viagem espacial de {nome}\n\n"
                    "Era uma noite estrelada quando {nome} subiu em sua nave espacial.\n"
                    "O painel estava cheio de botoes com silabas escritas:\n"
                    "MA - TE - MA - TI - CA!\n\n"
                    "— Para decolar, leia o codigo! — disse o computador.\n\n"
                    "{nome} leu com cuidado:\n"
                    "— Des... ti... no: LUA!\n\n"
                    "A nave disparou pelo espaco!\n"
                    "Estrelas passavam em velocidade.\n"
                    "Planetas de todas as cores!\n\n"
                    "Na lua, {nome} encontrou um recado:\n"
                    "SO-MOS-FE-LI-ZES-QUAN-DO-A-PREN-DE-MOS!\n\n"
                    "Somos felizes quando aprendemos! 🌙"
                )
            },
            {
                "emoji": "🍕",
                "texto": (
                    "A receita secreta\n\n"
                    "A avo de {nome} tinha uma receita secreta de bolo.\n"
                    "Estava escrita num papel bem velho.\n\n"
                    "{nome} pegou o papel e leu com cuidado:\n\n"
                    "IN-GRE-DI-EN-TES:\n"
                    "— Dois ovos\n"
                    "— Uma xicara de farinha\n"
                    "— Meio copo de leite\n"
                    "— Tres colheres de acucar\n\n"
                    "MO-DO DE FA-ZER:\n"
                    "— Misture tudo\n"
                    "— Ponha na forma\n"
                    "— Asse por 40 minutos\n\n"
                    "{nome} fez o bolo sozinho!\n"
                    "A avo provou e disse: perfeito!\n\n"
                    "Ler receitas e uma das magias da leitura! 🎂"
                )
            },
            {
                "emoji": "🌊",
                "texto": (
                    "O peixe que virou escritor\n\n"
                    "No fundo do mar, {nome} era diferente dos outros peixes.\n"
                    "Enquanto os demais nadavam, {nome} lia mensagens nas pedras.\n\n"
                    "Um dia, encontrou uma mensagem especial:\n"
                    "A-JU-DA! ES-TOU PER-DI-DO!\n\n"
                    "{nome} leu e entendeu: alguem precisava de socorro!\n\n"
                    "Seguindo as pistas escritas nas pedras, {nome} achou um peixinho perdido.\n\n"
                    "O peixinho perguntou:\n"
                    "— Como voce me encontrou?\n\n"
                    "{nome} respondeu:\n"
                    "— Aprendi a ler. E quem sabe ler\n"
                    "  nunca fica perdido! 🐟"
                )
            },
        ],

        "avancado": [
            {
                "emoji": "📚",
                "texto": (
                    "A biblioteca magica\n\n"
                    "Havia uma biblioteca no coracao da cidade onde {nome} morava.\n"
                    "Diziam que seus livros eram magicos: ao ler, voce entrava na historia!\n\n"
                    "{nome} escolheu um livro chamado 'A Floresta dos Enigmas'.\n"
                    "Ao abrir a primeira pagina, o quarto desapareceu.\n\n"
                    "Na floresta, havia uma guardia chamada Coruja Sabia.\n"
                    "Ela falou: — Para passar, responda: qual e o poder das palavras?\n\n"
                    "{nome} pensou e respondeu:\n"
                    "— As palavras tem o poder de ensinar, de emocionar, de conectar pessoas.\n"
                    "  Um livro pode mudar uma vida. Ja mudou a minha.\n\n"
                    "A Coruja abriu o caminho e disse:\n"
                    "— Quem entende o valor das palavras\n"
                    "  nunca estara sozinho. Bem-vindo, leitor! 🦉"
                )
            },
            {
                "emoji": "🏔️",
                "texto": (
                    "A carta do futuro\n\n"
                    "Um dia, {nome} encontrou uma carta dentro de um livro velho.\n"
                    "Era uma carta de uma crianca do passado, escrita ha 50 anos.\n\n"
                    "A carta dizia:\n\n"
                    "'Ola, crianca do futuro!\n"
                    "Nao sei quem voce e, mas sei que voce sabe ler.\n"
                    "Isso me deixa feliz.\n\n"
                    "Eu aprendi a ler num tempo dificil.\n"
                    "Nao tinha muitos livros, mas os que tinha\n"
                    "me levavam para mundos que eu nunca conheceria.\n\n"
                    "Cuide dos seus livros.\n"
                    "Cuide das suas palavras.\n"
                    "Elas sao o maior tesouro que existe.'\n\n"
                    "{nome} dobrou a carta com cuidado e a guardou.\n"
                    "Naquele dia, entendeu que ler e uma conversa\n"
                    "que atravessa o tempo. 💌"
                )
            },
            {
                "emoji": "🌍",
                "texto": (
                    "O jornal do mundo\n\n"
                    "A professora pediu para {nome} ler um trecho de jornal.\n\n"
                    "A manchete dizia:\n"
                    "'CRIANCAS DE TODO O MUNDO\n"
                    " LUTAM PELO DIREITO DE ESTUDAR'\n\n"
                    "{nome} leu o texto completo.\n"
                    "Descobriu que em alguns paises, criancas\n"
                    "caminham horas para chegar a uma escola.\n\n"
                    "Depois da leitura, a professora perguntou:\n"
                    "— O que voce sentiu ao ler essa noticia?\n\n"
                    "{nome} respondeu:\n"
                    "— Senti que tenho sorte de poder aprender.\n"
                    "  E que devo aproveitar cada aula, cada livro,\n"
                    "  cada palavra nova que eu aprendo.\n\n"
                    "A professora sorriu.\n"
                    "Essa era exatamente a resposta certa. 🌟"
                )
            },
        ]
    }

    # ── ATIVIDADES POR NÍVEL ────────────────────────────────────────────
    ATIVIDADES = {
        "iniciante": [
            # QUIZ — letra inicial
            {"titulo": "Qual a primeira letra?", "tipo": "quiz",
             "conteudo": "GATO começa com qual letra?|G|P|T|M|G|Certo! G de GATO! 🐱"},
            {"titulo": "Qual a primeira letra?", "tipo": "quiz",
             "conteudo": "BOLA começa com qual letra?|A|C|B|D|B|Isso! B de BOLA! ⚽"},
            {"titulo": "Qual a primeira letra?", "tipo": "quiz",
             "conteudo": "CASA começa com qual letra?|K|C|S|G|C|Muito bem! C de CASA! 🏠"},
            {"titulo": "Qual a primeira letra?", "tipo": "quiz",
             "conteudo": "PATO começa com qual letra?|B|T|F|P|P|Correto! P de PATO! 🦆"},
            {"titulo": "Qual a primeira letra?", "tipo": "quiz",
             "conteudo": "MACA começa com qual letra?|N|A|M|L|M|Isso mesmo! M de MACA! 🍎"},
            # QUIZ — vogal
            {"titulo": "Qual e a vogal?", "tipo": "quiz",
             "conteudo": "Qual dessas e uma VOGAL?|B|A|C|D|A|Correto! A e uma vogal. As vogais sao: A E I O U! 🌟"},
            {"titulo": "Qual e a vogal?", "tipo": "quiz",
             "conteudo": "Qual dessas e uma VOGAL?|M|F|E|S|E|Isso! E e uma vogal. Voce ja sabe as vogais! ✨"},
            # LIGAR — letra × palavra
            {"titulo": "Ligue a letra ao animal", "tipo": "ligar",
             "conteudo": "G:Gato|B:Boi|P:Pato|M:Macaco"},
            {"titulo": "Ligue a letra à fruta", "tipo": "ligar",
             "conteudo": "U:Uva|A:Abacaxi|M:Manga|L:Laranja"},
            {"titulo": "Ligue a vogal ao desenho", "tipo": "ligar",
             "conteudo": "A:Abelha|E:Estrela|I:Igreja|O:Ovo"},
            # COMPLETAR — sílaba simples
            {"titulo": "Complete a palavra", "tipo": "completar",
             "conteudo": "GA__O|T|C|P|T|GA-T-O = GATO! 🐱"},
            {"titulo": "Complete a palavra", "tipo": "completar",
             "conteudo": "BO__A|L|N|R|L|BO-L-A = BOLA! ⚽"},
            {"titulo": "Complete a palavra", "tipo": "completar",
             "conteudo": "PA__O|T|C|M|T|PA-T-O = PATO! 🦆"},
        ],

        "intermediario": [
            # QUIZ — sílabas
            {"titulo": "Quantas silabas?", "tipo": "quiz",
             "conteudo": "Quantas silabas tem BORBOLETA?|2|3|4|5|4|Certo! BOR-BO-LE-TA = 4 silabas! 🦋"},
            {"titulo": "Quantas silabas?", "tipo": "quiz",
             "conteudo": "Quantas silabas tem CACHORRO?|2|3|4|1|3|Isso! CA-CHOR-RO = 3 silabas! 🐶"},
            {"titulo": "Quantas silabas?", "tipo": "quiz",
             "conteudo": "Quantas silabas tem JANELA?|2|3|4|1|3|Correto! JA-NE-LA = 3 silabas! 🪟"},
            {"titulo": "Quantas silabas?", "tipo": "quiz",
             "conteudo": "Quantas silabas tem CHOCOLATE?|3|4|5|2|4|Muito bem! CHO-CO-LA-TE = 4 silabas! 🍫"},
            # QUIZ — rima
            {"titulo": "Qual palavra rima?", "tipo": "quiz",
             "conteudo": "Qual palavra rima com FLOR?|Mesa|Amor|Casa|Porta|Amor|Perfeito! FLOR e AMOR rimam! 🌹"},
            {"titulo": "Qual palavra rima?", "tipo": "quiz",
             "conteudo": "Qual palavra rima com PATO?|Bola|Gato|Chuva|Livro|Gato|Isso! PATO e GATO rimam! 🦆"},
            {"titulo": "Qual palavra rima?", "tipo": "quiz",
             "conteudo": "Qual palavra rima com CAMA?|Porta|Chama|Livro|Bolo|Chama|Correto! CAMA e CHAMA rimam! ✨"},
            # COMPLETAR — sílaba complexa
            {"titulo": "Complete a silaba", "tipo": "completar",
             "conteudo": "CA__RO|R|N|T|R|CA-R-RO = CARRO! 🚗"},
            {"titulo": "Complete a silaba", "tipo": "completar",
             "conteudo": "MA__A|C|N|R|C|MA-C-A = MACA! 🍎"},
            {"titulo": "Forme a palavra", "tipo": "completar",
             "conteudo": "BA + NA + NA = ?|BANANA|LARANJA|MANGA|BANANA|BA-NA-NA = BANANA! 🍌"},
            {"titulo": "Forme a palavra", "tipo": "completar",
             "conteudo": "BO + LO + DE = ?|BOLICHE|BOLODE|BOLO|BOLO|B-O-L-O = BOLO! 🎂"},
            # LIGAR — sílaba × palavra
            {"titulo": "Ligue a silaba a palavra", "tipo": "ligar",
             "conteudo": "MA:Maca|SO:Sol|CA:Casa|PA:Pato"},
            {"titulo": "Ligue o animal ao som", "tipo": "ligar",
             "conteudo": "Gato:Miau|Cachorro:Au-au|Vaca:Mu|Sapo:Croac"},
        ],

        "avancado": [
            # QUIZ — compreensao
            {"titulo": "Leia e responda", "tipo": "quiz",
             "conteudo": "Frase: O menino foi à escola de bicicleta. Como o menino foi à escola?|A pe|De carro|De bicicleta|De onibus|De bicicleta|Correto! A frase diz que ele foi DE BICICLETA! 🚲"},
            {"titulo": "Leia e responda", "tipo": "quiz",
             "conteudo": "Frase: Maria ganhou um livro de presente no seu aniversario. O que Maria ganhou?|Uma boneca|Um livro|Um bolo|Um jogo|Um livro|Isso! Ela ganhou um LIVRO de presente! 📚"},
            {"titulo": "Qual o plural?", "tipo": "quiz",
             "conteudo": "Qual e o plural de FLOR?|Floras|Flores|Floris|Flors|Flores|Muito bem! O plural de FLOR e FLORES! 🌸"},
            {"titulo": "Qual o plural?", "tipo": "quiz",
             "conteudo": "Qual e o plural de MAO?|Maos|Maoes|Maes|Mos|Maos|Correto! O plural de MAO e MAOS! 👐"},
            {"titulo": "Qual o sinonimo?", "tipo": "quiz",
             "conteudo": "Qual palavra tem o mesmo sentido de FELIZ?|Triste|Alegre|Cansado|Com raiva|Alegre|Isso! FELIZ e ALEGRE tem o mesmo sentido! 😊"},
            # COMPLETAR — frase
            {"titulo": "Complete a frase", "tipo": "completar",
             "conteudo": "O ___ ladra para o carteiro.|cachorro|gato|passaro|cachorro|O CACHORRO ladra! 🐶"},
            {"titulo": "Complete a frase", "tipo": "completar",
             "conteudo": "A ___ brilha no ceu a noite.|lua|sol|chuva|lua|A LUA brilha a noite! 🌙"},
            {"titulo": "Complete a frase", "tipo": "completar",
             "conteudo": "Os peixes vivem no ___.|mar|ceu|floresta|mar|Os peixes vivem no MAR! 🐟"},
            # LIGAR — sinonimos
            {"titulo": "Ligue os sinonimos", "tipo": "ligar",
             "conteudo": "Feliz:Alegre|Triste:Choroso|Grande:Enorme|Bonito:Lindo"},
            {"titulo": "Ligue verbo a ação", "tipo": "ligar",
             "conteudo": "Correr:Atletismo|Nadar:Piscina|Cantar:Musica|Desenhar:Arte"},
        ]
    }

    def gerar_historia(self, perfil):
        nivel = perfil.get("nivel", "iniciante")
        nome  = perfil.get("nome", "crianca")
        pool  = self.HISTORIAS.get(nivel, self.HISTORIAS["iniciante"])
        h     = random.choice(pool)
        return h["emoji"] + "|" + h["texto"].format(nome=nome)

    def gerar_atividades(self, perfil):
        nivel = perfil.get("nivel", "iniciante")
        pool  = self.ATIVIDADES.get(nivel, self.ATIVIDADES["iniciante"])

        # Agrupa por tipo e sorteia um de cada tipo diferente
        # Isso garante máxima variedade a cada trilha criada
        por_tipo = {}
        for a in pool:
            por_tipo.setdefault(a["tipo"], []).append(a)

        tipos_disponiveis = list(por_tipo.keys())
        random.shuffle(tipos_disponiveis)

        escolhidos = []
        for tipo in tipos_disponiveis:
            if len(escolhidos) >= 2:
                break
            # Dentro do mesmo tipo, pega um aleatório diferente do já escolhido
            candidatos = [a for a in por_tipo[tipo] if a not in escolhidos]
            if candidatos:
                escolhidos.append(random.choice(candidatos))

        return escolhidos[:2]


class MockIAAdapter(IAProvider):
    def gerar_historia(self, perfil):
        return "📖|Historia de teste para " + perfil.get("nome", "crianca") + "."
    def gerar_atividades(self, perfil):
        return [{"titulo": "Atividade mock", "tipo": "quiz",
                 "conteudo": "Pergunta?|A|B|C|D|A|Correto!"}]
