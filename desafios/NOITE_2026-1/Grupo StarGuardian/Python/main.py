import time
import random
import uuid


class PerfilComandante:
    def __init__(self, interesses):
        # GERADOR DE TÍTULO ÉPICO (Privacidade + Lodicidade)
        adjetivos = ["Valente", "Brilhante", "Veloz", "Curioso", "Invencível", "Sábio", "Explorador", "Galáctico"]
        substantivos = ["Estrela", "Cometa", "Foguete", "Planeta", "Nebulosa", "Cosmos", "Astro", "Raio"]
        
        self.titulo_epico = f"{random.choice(substantivos)} {random.choice(adjetivos)}"
        self.id_anonimo = str(uuid.uuid4())[:4] # Apenas para controle interno
        self.fase_escolar = "Fundamental I" 
        self.interesses = interesses
        self.experiencia = 0
        self.missoes_concluidas = set() 

    def ganhar_xp(self, pontos):
        self.experiencia += pontos


CONTEUDO_INFANTIL = {
    'Matemática': {
        'Fácil': [
            ["MAT_F_01", "Se sua nave tem 3 cristais e você encontra mais 2, quantos tem agora?", ["4", "5", "6"], 1],
            ["MAT_F_02", "Quantos planetas você vê aqui: 🪐 🪐 🪐?", ["2", "3", "4"], 1],
            ["MAT_F_03", "Qual número vem depois do 9 na contagem para o lançamento?", ["8", "10", "11"], 1],
        ],
        'Médio': [
            ["MAT_M_01", "A constelação tem 7 estrelas. Se 3 se apagarem, quantas restam?", ["4", "5", "10"], 0],
            ["MAT_M_02", "Dobro de 4 foguetes é igual a:", ["6", "8", "10"], 1],
            ["MAT_M_03", "Se um astronauta tem 10 balas e dá 2 para cada amigo, quantos amigos ele pode presentear?", ["3", "4", "5"], 1],
        ],
        'Difícil': [
            ["MAT_D_01", "Se um foguete viaja a 20 km/s, quantos km ele percorre em 3 segundos?", ["60 km", "100 km", "120 km"], 0],
            ["MAT_D_02", "Qual é a raiz quadrada de 16?", ["2", "4", "8"], 1],
            ["MAT_D_03", "Se um planeta tem 5 luas e cada lua tem 3 crateras, quantas crateras existem no total?", ["15", "20", "25"], 0],
        ]
    },
    'Português': {
        'Fácil': [
            ["POR_F_01", "Qual é a primeira letra da palavra 'ASTRONAUTA'?", ["E", "O", "A"], 2],
            ["POR_F_02", "Complete a palavra: L_A (Brilha à noite)", ["U", "O", "I"], 0],
            ["POR_F_03", "Qual o nome do animal que faz 'Au Au' na nave?", ["Gato", "Cachorro", "Peixe"], 1],
        ],
        'Médio': [
            ["POR_M_01", "Como se escreve o nome do nosso planeta?", ["Terra", "Tera", "Terrah"], 0],
            ["POR_M_02", "Qual palavra rima com 'FOGUETE'?", ["Estrela", "Sorvete", "Planeta"], 1],
            ["POR_M_03", "Qual é o plural de 'ESTRELA'?", ["Estrelas", "Estrelos", "Estrelas"], 0],
        ],
        'Difícil': [
            ["POR_D_01", "Qual é o antônimo de 'LENTO'?", ["Rápido", "Devagar", "Parado"], 0],
            ["POR_D_02", "Complete a frase: O astronauta é um ____ do espaço.", ["Explorador", "Cozinheiro", "Médico"], 0],
            ["POR_D_03", "Qual é o verbo na frase: 'O foguete decolou rapidamente'?", ["Foguete", "Decolou", "Rapidamente"], 1],
        ]
    },
    'Ciências': {
        'Fácil': [
            ["CIE_F_01", "O Sol é uma:", ["Estrela", "Planeta", "Lua"], 0],
            ["CIE_F_02", "Qual animal vive na água?", ["Leão", "Peixe", "Pássaro"], 1],
            ["CIE_F_03", "O que usamos para respirar?", ["Água", "Ar", "Comida"], 1],
        ],
        'Médio': [
            ["CIE_M_01", "A Lua gira em volta de qual planeta?", ["Marte", "Terra", "Sol"], 1],
            ["CIE_M_02", "O que as plantas precisam para crescer?", ["Suco", "Luz e Água", "Chocolate"], 1],
            ["CIE_M_03", "Qual é o maior planeta do sistema solar?", ["Júpiter", "Saturno", "Marte"], 0],
        ],
        'Difícil': [
            ["CIE_D_01", "O que é a Via Láctea?", ["Uma galáxia", "Um planeta", "Uma estrela"], 0],
            ["CIE_D_02", "Qual é o nome do nosso sistema solar?", ["Via Láctea", "Andrômeda", "Triângulo"], 0],
            ["CIE_D_03", "O que é um cometa?", ["Um tipo de estrela", "Um pedaço de gelo e rocha que orbita o Sol", "Um planeta"], 1],
        ]
    },
    'História': {
        'Fácil': [
            ["HIS_F_01", "Antigamente usavam caravelas no mar. Hoje usamos o quê no espaço?", ["Carros", "Foguetes", "Bicicletas"], 1],
            ["HIS_F_02", "Quem foram os primeiros habitantes do Brasil?", ["Astronautas", "Indígenas", "Robôs"], 1],
            ["HIS_F_03", "Como os antigos guardavam histórias antes dos computadores?", ["Em livros e desenhos", "No YouTube", "No Pendrive"], 0],
        ],
        'Médio': [
            ["HIS_M_01", "Qual princesa assinou a Lei Áurea para libertar as pessoas escravizadas no Brasil?", ["Princesa Diana", "Princesa Isabel", "Princesa Leia"], 1],
            ["HIS_M_02", "Em que dia comemoramos a Independência do Brasil?", ["25 de Dezembro", "7 de Setembro", "1 de Janeiro"], 1],
            ["HIS_M_03", "Quem foi o líder das caravelas que chegaram ao Brasil no ano de 1500?", ["Pedro Álvares Cabral", "Dom Pedro I", "Zumbi dos Palmares"], 0]
        ],
        'Difícil': [
            ["HIS_D_01", "Qual era o nome do sistema de governo onde reis e rainhas mandavam em tudo?", ["Democracia", "Monarquia", "República"], 1],
            ["HIS_D_02", "Qual grande invenção permitiu que as notícias viajassem rápido antes da internet?", ["Telégrafo", "Teletransporte", "Espelho"], 0],
            ["HIS_D_03", "Quem foi o primeiro presidente do Brasil, logo após a Proclamação da República?", ["Deodoro da Fonseca", "Getúlio Vargas", "Dom Pedro II"], 0]

        ]
    },
    'Geografia': {
        'Fácil': [
            ["GEO_F_01", "Qual é o nome do planeta onde nós moramos?", ["Marte", "Terra", "Júpiter"], 1],
            ["GEO_F_02", "Como chamamos o lado onde o Sol nasce todos os dias?", ["Nascente", "Poente", "Sul"], 0],
            ["GEO_F_03", "Qual objeto representa o nosso planeta de forma redonda?", ["Mapa", "Globo Terrestre", "Triângulo"], 1],
        ],
        'Médio': [
            ["GEO_M_01", "Qual destes é um bioma brasileiro que parece uma floresta espacial muito densa?", ["Caatinga", "Amazônia", "Cerrado"], 1],
            ["GEO_M_02", "Como chamamos a linha imaginária que divide a Terra em Norte e Sul?", ["Linha do Equador", "Trópico de Câncer", "Meridiano"], 0],
            ["GEO_M_03", "Qual é a capital do nosso país, o Brasil?", ["São Paulo", "Rio de Janeiro", "Brasília"], 2]
        ],
        'Difícil': [
            ["GEO_D_01", "Qual fenômeno faz a Terra girar em volta de si mesma criando o dia e a noite?", ["Translação", "Rotação", "Gravidade"], 1],
            ["GEO_D_02", "Qual é o nome da camada de ar que protege a Terra como o escudo da nossa nave?", ["Atmosfera", "Hidrosfera", "Litosfera"], 0],
            ["GEO_D_03", "Como se chama a camada mais interna e quente do nosso planeta?", ["Crosta", "Manto", "Núcleo"], 2]
        ]
    },
    'Inglês': {
        'Fácil': [
            ["ENG_F_01", "Como dizemos 'Olá' em inglês para um novo amigo espacial?", ["Goodbye", "Hello", "Thank you"], 1],
            ["ENG_F_02", "Qual é a cor 'Blue' das estrelas?", ["Vermelho", "Azul", "Amarelo"], 1],
            ["ENG_F_03", "Como chamamos o nosso grande amigo 'Sol' em inglês?", ["Moon", "Star", "Sun"], 2]
        ],
        'Médio': [
            ["ENG_M_01", "Se você vir um 'Dog' na nave, qual animal você encontrou?", ["Gato", "Cachorro", "Pássaro"], 1],
            ["ENG_M_02", "Como dizemos 'Bom dia' quando o sol nasce na estação?", ["Good night", "Good afternoon", "Good morning"], 2],
            ["ENG_M_03", "Qual dessas frutas é a 'Apple' que os astronautas comem?", ["Maçã", "Banana", "Uva"], 0]
        ],
        'Difícil': [
            ["ENG_D_01", "Como se diz 'Eu amo o espaço' em inglês?", ["I love space", "I hate space", "Space is big"], 0],
            ["ENG_D_02", "Qual é o plural de 'Star' (Estrela)?", ["Stares", "Stars", "Staring"], 1],
            ["ENG_D_03", "Como perguntamos 'Qual o seu nome?' para um alienígena?", ["How are you?", "Where are you?", "What is your name?"], 2]
        ]
    }
}


class ComputadorDeBordoIA:
    def selecionar_desafio_inedito(self, perfil):
        temas = list(CONTEUDO_INFANTIL.keys())
        random.shuffle(temas)
        nivel = 'Fácil' if perfil.experiencia < 50 else 'Médio' if perfil.experiencia < 150 else 'Difícil'
        
        for tema in temas:
            perguntas = CONTEUDO_INFANTIL[tema].get(nivel, [])
            novas = [p for p in perguntas if p[0] not in perfil.missoes_concluidas]
            if novas:
                return tema, nivel, random.choice(novas)
        return None


class DiarioDeBordo:
    def registrar_sucesso(self, perfil, pergunta_id):
        perfil.missoes_concluidas.add(pergunta_id)
        perfil.ganhar_xp(15)
        print(f"\n[SISTEMA] Missão concluída! XP: {perfil.experiencia}")


class InterfaceEstelar:
    def __init__(self, perfil, ia, diario):
        self.perfil = perfil
        self.ia = ia
        self.diario = diario

    def loop_missoes(self):
        print("\n" + "✨"*30)
        print(f" BEM-VINDO, COMANDANTE {self.perfil.titulo_epico.upper()}!")
        print(f" SUA JORNADA COMEÇA AGORA NA ESTAÇÃO IMIP.")
        print("✨"*30)
        
        while True:
            resultado = self.ia.selecionar_desafio_inedito(self.perfil)
            if not resultado:
                print("\nSetor explorado! Parabéns, Comandante!")
                break
            
            tema, nivel, dados = resultado
            p_id, pergunta, opcoes, correta = dados
            
            print(f"\n--- MISSÃO: {tema.upper()} ---")
            print(f"PERGUNTA: {pergunta}")
            
            letras = ['A', 'B', 'C']
            for i, opcao in enumerate(opcoes):
                print(f"  {letras[i]}) {opcao}")
            
            escolha = input("\nSua resposta (ou 'SAIR'): ").upper().strip()
            if escolha == 'SAIR': break
                
            mapa = {'A': 0, 'B': 1, 'C': 2}
            if escolha in mapa:
                if mapa[escolha] == correta:
                    print(f"\n[IA] Incrível, {self.perfil.titulo_epico}! Você acertou!")
                    self.diario.registrar_sucesso(self.perfil, p_id)
                else:
                    print(f"\n[IA] Quase lá, {self.perfil.titulo_epico}! Tente novamente na próxima.")
            else:
                print("\n[AVISO] Comando inválido.")


def main():
    comandante = PerfilComandante(["Estrelas"])
    ia = ComputadorDeBordoIA()
    diario = DiarioDeBordo()
    app = InterfaceEstelar(comandante, ia, diario)
    
    try:
        app.loop_missoes()
    except KeyboardInterrupt:
        print("\nDesconectando...")

if __name__ == "__main__":
    main()