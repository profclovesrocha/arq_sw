import sqlite3
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR, "imip.db")


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS aluno (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER,
            turma TEXT,
            internacao TEXT
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS professor (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            area TEXT,
            contato TEXT
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS planopedagogico (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            aluno_id INTEGER NOT NULL,
            professor_id INTEGER,
            titulo TEXT NOT NULL,
            metas TEXT NOT NULL,
            estado_emocional TEXT,
            roteiro TEXT NOT NULL,
            FOREIGN KEY(aluno_id) REFERENCES aluno(id),
            FOREIGN KEY(professor_id) REFERENCES professor(id)
        )
    """)
    conn.commit()
    conn.close()


def create_aluno(nome, idade, turma, internacao):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO aluno (nome, idade, turma, internacao) VALUES (?, ?, ?, ?)",
                   (nome, idade, turma, internacao))
    conn.commit()
    conn.close()


def list_alunos():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM aluno ORDER BY nome")
    rows = cursor.fetchall()
    conn.close()
    return rows


def create_professor(nome, area, contato):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO professor (nome, area, contato) VALUES (?, ?, ?)", (nome, area, contato))
    conn.commit()
    conn.close()


def list_professores():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM professor ORDER BY nome")
    rows = cursor.fetchall()
    conn.close()
    return rows


def create_plano(aluno_id, professor_id, titulo, metas, estado_emocional, roteiro):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO planopedagogico (aluno_id, professor_id, titulo, metas, estado_emocional, roteiro) VALUES (?, ?, ?, ?, ?, ?)",
        (aluno_id, professor_id, titulo, metas, estado_emocional, roteiro)
    )
    conn.commit()
    conn.close()


def list_planos():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT p.*, a.nome as aluno_nome, t.nome as professor_nome FROM planopedagogico p LEFT JOIN aluno a ON p.aluno_id=a.id LEFT JOIN professor t ON p.professor_id=t.id ORDER BY p.id DESC")
    rows = cursor.fetchall()
    conn.close()
    return rows


def get_plano(plan_id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT p.*, a.nome as aluno_nome, t.nome as professor_nome FROM planopedagogico p LEFT JOIN aluno a ON p.aluno_id=a.id LEFT JOIN professor t ON p.professor_id=t.id WHERE p.id = ?", (plan_id,))
    plano = cursor.fetchone()
    conn.close()
    return plano


def delete_plano(plan_id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM planopedagogico WHERE id = ?", (plan_id,))
    conn.commit()
    conn.close()


def generate_decision_support_plan(student_name, age, condition, learning_goals, emotional_state):
    summary = []
    summary.append(f"Paciente: {student_name}")
    if age:
        summary.append(f"Idade: {age}")
    if condition:
        summary.append(f"Condição clínica: {condition}")

    summary.append(f"Estado emocional: {emotional_state or 'estável'}")
    summary.append(f"Objetivos de aprendizagem: {learning_goals}")

    narrative = (
        "Narrativa interativa: o paciente é protagonista da aventura do aprendizado. "
        "Inclua elementos emocionais adaptados ao ritmo e estado atual."
    )

    strategy = [
        "1) Atividades sensoriais guiadas com imagens e histórias de ambiente hospitalar.",
        "2) Jogo de palavras com letras móveis adaptado ao nível de leitura.",
        "3) Intervalos de verificação afetiva para checar sentimento e ajustar ritmo."
    ]

    if emotional_state:
        estado = emotional_state.lower()
        if "ans" in estado or "triste" in estado or "depre" in estado:
            strategy.append("Apoio especial: reflexão emocional leve e música calmante.")

    plan = "\n".join(summary) + "\n\n" + narrative + "\n" + "\n".join(strategy)
    return plan