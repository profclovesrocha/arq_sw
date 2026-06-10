"""
Seed script para popular o banco com categorias, lições e questões.
Dados espelham os mocks do frontend alfabe-front.

Uso: python seed.py
"""
from config import app, db
from models.alfabe_models import (
    Categoria, Licao, LicaoStep, Alternativa, Professor
)


def seed_categorias():
    """Cria as 4 categorias."""
    categorias = [
        Categoria(id='vogais', nome='Vogais', descricao='Aprenda as 5 vogais do alfabeto', icone='🔤'),
        Categoria(id='consoantes', nome='Consoantes', descricao='Descubra as 21 consoantes', icone='🔡'),
        Categoria(id='silabas', nome='Sílabas', descricao='Junte letras e forme sílabas', icone='✂️'),
        Categoria(id='palavras', nome='Palavras', descricao='Forme e reconheça palavras', icone='📖'),
    ]
    for c in categorias:
        if not Categoria.query.get(c.id):
            db.session.add(c)
    db.session.commit()
    print("✓ Categorias criadas")


def _criar_step_informativo(licao_id, ordem, titulo, conteudo):
    step = LicaoStep(
        id_licao=licao_id, ordem=ordem, tipo='card-informativo',
        titulo=titulo, conteudo=conteudo
    )
    db.session.add(step)
    db.session.flush()
    return step


def _criar_step_pergunta(licao_id, ordem, enunciado, opcoes, resposta_correta):
    step = LicaoStep(
        id_licao=licao_id, ordem=ordem, tipo='pergunta',
        enunciado=enunciado
    )
    db.session.add(step)
    db.session.flush()

    for i, texto in enumerate(opcoes):
        alt = Alternativa(id_step=step.id, texto=texto, correta=(i == resposta_correta))
        db.session.add(alt)

    return step


def seed_licoes_vogais():
    licoes_data = [
        {
            'id': 'vogais-1', 'nivel': 1, 'titulo': 'Conhecendo as Vogais',
            'steps': [
                ('info', 'O que são vogais?', 'As vogais são letras especiais: A, E, I, O, U. Elas fazem sons abertos e bonitos!'),
                ('pergunta', 'Qual dessas letras é uma vogal?', ['B', 'A', 'D', 'F'], 1),
                ('info', 'A letra A', 'O "A" é a primeira vogal. A palavra "abelha" começa com A!'),
                ('pergunta', 'Qual dessas letras NÃO é uma vogal?', ['A', 'E', 'B', 'I'], 2),
                ('pergunta', 'Quantas vogais tem o alfabeto?', ['3', '4', '5', '6'], 2),
            ]
        },
        {
            'id': 'vogais-2', 'nivel': 2, 'titulo': 'Vogais nas Palavras',
            'steps': [
                ('info', 'Vogais nas palavras', 'Toda palavra tem pelo menos uma vogal. Sem vogais, não conseguimos falar!'),
                ('pergunta', 'Qual vogal está na palavra "BOLA"?', ['E', 'O', 'U', 'I'], 1),
                ('info', 'Encontrando vogais', 'Na palavra "GATO" temos duas vogais: o "A" e o "O". Você consegue encontrá-las?'),
                ('pergunta', 'Quantas vogais tem a palavra "CASA"?', ['1', '3', '2', '4'], 2),
                ('pergunta', 'Qual vogal está no meio da palavra "PÉ"?', ['A', 'I', 'E', 'U'], 2),
            ]
        },
        {
            'id': 'vogais-3', 'nivel': 3, 'titulo': 'Começando com Vogal',
            'steps': [
                ('info', 'Palavras que começam com vogal', 'Muitas palavras legais começam com vogal: Abelha, Elefante, Igreja, Ônibus, Uva!'),
                ('pergunta', 'Qual palavra começa com a vogal "A"?', ['Banana', 'Abelha', 'Gato', 'Casa'], 1),
                ('pergunta', 'Qual palavra começa com a vogal "E"?', ['Faca', 'Bola', 'Elefante', 'Dente'], 2),
                ('pergunta', 'Qual palavra começa com a vogal "I"?', ['Igreja', 'Pato', 'Rato', 'Sapo'], 0),
                ('pergunta', 'Qual palavra começa com a vogal "U"?', ['Sino', 'Leite', 'Mesa', 'Uva'], 3),
            ]
        },
    ]
    _seed_licoes('vogais', licoes_data)


def seed_licoes_consoantes():
    licoes_data = [
        {
            'id': 'consoantes-1', 'nivel': 1, 'titulo': 'Conhecendo as Consoantes',
            'steps': [
                ('info', 'O que são consoantes?', 'Consoantes são todas as letras que não são vogais. São 21 consoantes no alfabeto!'),
                ('pergunta', 'Qual dessas letras é uma consoante?', ['A', 'B', 'E', 'I'], 1),
                ('info', 'A letra B', 'O "B" faz o som de "bê". Bola, boneca, bicicleta começam com B!'),
                ('pergunta', 'Qual dessas letras NÃO é uma consoante?', ['C', 'D', 'O', 'F'], 2),
                ('pergunta', 'Quantas consoantes tem o alfabeto?', ['21', '5', '10', '26'], 0),
            ]
        },
        {
            'id': 'consoantes-2', 'nivel': 2, 'titulo': 'Consoantes nas Palavras',
            'steps': [
                ('info', 'Consoantes e vogais juntas', 'As consoantes precisam das vogais para formar sons. Juntas elas criam palavras!'),
                ('pergunta', 'Qual a consoante da palavra "PÁ"?', ['A', 'P', 'E', 'O'], 1),
                ('info', 'Encontrando consoantes', 'Na palavra "MALA" temos as consoantes M e L, e as vogais A e A.'),
                ('pergunta', 'Quantas consoantes tem a palavra "BOI"?', ['0', '3', '1', '2'], 2),
                ('pergunta', 'Qual dessas palavras tem MAIS consoantes?', ['Uva', 'Oi', 'Prato', 'Eu'], 2),
            ]
        },
        {
            'id': 'consoantes-3', 'nivel': 3, 'titulo': 'Sons das Consoantes',
            'steps': [
                ('info', 'Consoantes têm sons diferentes', 'O "R" faz sons diferentes: "rato" (forte) e "caro" (suave). Que legal!'),
                ('pergunta', 'Qual letra faz o som de "ssss"?', ['R', 'T', 'S', 'D'], 2),
                ('pergunta', 'A palavra "CAJU" começa com qual consoante?', ['J', 'A', 'C', 'U'], 2),
                ('pergunta', 'Qual consoante aparece duas vezes em "PIPA"?', ['I', 'P', 'A', 'R'], 1),
                ('pergunta', 'Qual palavra começa com a consoante "M"?', ['Abelha', 'Elefante', 'Macaco', 'Uva'], 2),
            ]
        },
    ]
    _seed_licoes('consoantes', licoes_data)


def seed_licoes_silabas():
    licoes_data = [
        {
            'id': 'silabas-1', 'nivel': 1, 'titulo': 'O que é uma Sílaba?',
            'steps': [
                ('info', 'Sílabas são pedacinhos', 'Uma sílaba é cada "pedacinho" de uma palavra. CASA = CA-SA (2 sílabas)!'),
                ('pergunta', 'Quantas sílabas tem a palavra "PÉ"?', ['1', '2', '3', '4'], 0),
                ('info', 'Toda sílaba tem uma vogal', 'Cada sílaba tem pelo menos uma vogal. A vogal é o coração da sílaba!'),
                ('pergunta', 'Quantas sílabas tem "GATO"?', ['3', '1', '4', '2'], 3),
                ('pergunta', 'Qual das palavras tem APENAS 1 sílaba?', ['CASA', 'PÃO', 'BOLA', 'GATO'], 1),
            ]
        },
        {
            'id': 'silabas-2', 'nivel': 2, 'titulo': 'Contando Sílabas',
            'steps': [
                ('info', 'Vamos contar sílabas!', 'Para contar sílabas, bata palmas enquanto fala a palavra. Cada palma é uma sílaba!'),
                ('pergunta', 'Quantas sílabas tem "BORBOLETA"?', ['5', '3', '4', '2'], 2),
                ('info', 'Pratique!', 'JA-NE-LA tem 3 sílabas. MA-CA-CO também tem 3. Você consegue pensar em outras?'),
                ('pergunta', 'Quantas sílabas tem "JANELA"?', ['4', '2', '3', '5'], 2),
                ('pergunta', 'Qual palavra tem 2 sílabas?', ['ABELHA', 'SOL', 'MACACO', 'CASA'], 3),
            ]
        },
        {
            'id': 'silabas-3', 'nivel': 3, 'titulo': 'Palavras Longas',
            'steps': [
                ('info', 'Palavras longas têm muitas sílabas!', 'BOR-BO-LE-TA tem 4 sílabas! Palavras longas são como um trem com muitos vagões.'),
                ('pergunta', 'Qual palavra tem MAIS sílabas?', ['SOL', 'CASA', 'BORBOLETA', 'GATO'], 2),
                ('pergunta', 'Quantas sílabas tem "TE-LE-VI-SÃO"?', ['5', '4', '6', '3'], 1),
                ('pergunta', 'A palavra "CA-VA-LO" tem quantas sílabas?', ['2', '4', '1', '3'], 3),
                ('pergunta', 'Qual a sílaba que falta? CA-VA-___', ['LA', 'RA', 'SO', 'TO'], 0),
            ]
        },
    ]
    _seed_licoes('silabas', licoes_data)


def seed_licoes_palavras():
    licoes_data = [
        {
            'id': 'palavras-1', 'nivel': 1, 'titulo': 'Palavras Simples',
            'steps': [
                ('info', 'O que é uma palavra?', 'Uma palavra é um conjunto de letras com significado. "SOL", "LUA", "PÉ" são palavras!'),
                ('pergunta', 'Qual dessas é uma palavra real?', ['XYZ', 'PÁ', 'QRF', 'BWD'], 1),
                ('info', 'Palavras curtas', 'Palavras de 1 sílaba são curtas e rápidas de falar: PÃO, SOL, PÉ, MAR!'),
                ('pergunta', 'Qual palavra indica o astro do dia?', ['LUA', 'SOL', 'MAR', 'CÉU'], 1),
                ('pergunta', 'Qual dessas palavras é mais curta?', ['BORBOLETA', 'JANELA', 'PÉ', 'MACACO'], 2),
            ]
        },
        {
            'id': 'palavras-2', 'nivel': 2, 'titulo': 'Palavras com 2 Sílabas',
            'steps': [
                ('info', 'Palavras com 2 sílabas', 'BOLA = BO-LA, GATO = GA-TO. Essas palavras têm exatamente 2 sílabas!'),
                ('pergunta', 'Qual dessas palavras tem 2 sílabas?', ['SOL', 'BORBOLETA', 'CASA', 'TELEVISÃO'], 2),
                ('info', 'Mais exemplos!', 'PATO, MALA, FOCA, PELE. Todas têm 2 sílabas. Você consegue bater palmas?'),
                ('pergunta', 'A criança brinca com a ___ (2 sílabas)', ['BOLA', 'BORBOLETA', 'PÉ', 'SOL'], 0),
                ('pergunta', 'Qual animal tem 2 sílabas no nome?', ['BORBOLETA', 'GATO', 'JACARÉ', 'ELEFANTE'], 1),
            ]
        },
        {
            'id': 'palavras-3', 'nivel': 3, 'titulo': 'Palavras Longas',
            'steps': [
                ('info', 'Palavras compridas', 'Palavras longas têm 3 ou mais sílabas. MA-CA-CO, ELE-FAN-TE, BOR-BO-LE-TA!'),
                ('pergunta', 'Qual animal tem 3 sílabas no nome?', ['PÃO', 'GATO', 'MACACO', 'SOL'], 2),
                ('pergunta', 'Qual palavra tem 4 sílabas?', ['GATO', 'BORBOLETA', 'CASA', 'SOL'], 1),
                ('pergunta', 'Complete a palavra: ELE-FAN-___', ['TE', 'SA', 'LA', 'DO'], 0),
                ('pergunta', 'Qual a palavra mais longa?', ['PAI', 'BOLA', 'JANELA', 'BORBOLETA'], 3),
            ]
        },
    ]
    _seed_licoes('palavras', licoes_data)


def _seed_licoes(categoria_id, licoes_data):
    """Helper para criar lições de uma categoria."""
    for licao_data in licoes_data:
        if Licao.query.get(licao_data['id']):
            continue

        licao = Licao(
            id=licao_data['id'],
            id_categoria=categoria_id,
            nivel=licao_data['nivel'],
            titulo=licao_data['titulo'],
        )
        db.session.add(licao)
        db.session.flush()

        for ordem, step_data in enumerate(licao_data['steps'], start=1):
            if step_data[0] == 'info':
                _criar_step_informativo(licao.id, ordem, step_data[1], step_data[2])
            elif step_data[0] == 'pergunta':
                _criar_step_pergunta(licao.id, ordem, step_data[1], step_data[2], step_data[3])

    db.session.commit()
    print(f"✓ Lições de {categoria_id} criadas")


def seed_professor_demo():
    """Cria um professor de demonstração."""
    if Professor.query.filter_by(matricula='PROF-001').first():
        print("✓ Professor demo já existe")
        return

    professor = Professor(nome='Professor Demo', matricula='PROF-001')
    professor.set_senha('123456')
    db.session.add(professor)
    db.session.commit()
    print("✓ Professor demo criado (matrícula: PROF-001, senha: 123456)")


def run_seed():
    """Executa todo o seed."""
    print("Iniciando seed...")
    seed_categorias()
    seed_licoes_vogais()
    seed_licoes_consoantes()
    seed_licoes_silabas()
    seed_licoes_palavras()
    seed_professor_demo()
    print("\n✅ Seed completo!")


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        run_seed()
