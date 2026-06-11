from app import db

# =========================
# TABELA DE USUÁRIOS
# =========================

class User(db.Model):

    # Nome da tabela
    __tablename__ = "users"

    # ID do usuário
    id = db.Column(db.Integer, primary_key=True)

    # Nome
    name = db.Column(db.String(100), nullable=False)

    # Email único
    email = db.Column(db.String(120), unique=True, nullable=False)

    # Senha criptografada
    password = db.Column(db.String(255), nullable=False)

    # Tipo do usuário
    # aluno ou professor
    role = db.Column(db.String(20), nullable=False)


# =========================
# TABELA DE QUIZ
# =========================

class Quiz(db.Model):

    __tablename__ = "quizzes"

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(100), nullable=False)

    level = db.Column(db.String(50))


    questions = db.relationship(
        "Question",
        backref="quiz",
        lazy=True
    )


# =========================
# TABELA DE QUESTÕES
# =========================

class Question(db.Model):

    __tablename__ = "questions"

    id = db.Column(db.Integer, primary_key=True)

    # Chave estrangeira para quiz
    quiz_id = db.Column(
        db.Integer,
        db.ForeignKey("quizzes.id")
    )

    # Palavra incompleta
    word_with_missing = db.Column(
        db.String(100),
        nullable=False
    )

    # Resposta correta
    correct_answer = db.Column(
        db.String(100),
        nullable=False
    )


# =========================
# TENTATIVA DO ALUNO
# =========================

class Attempt(db.Model):

    __tablename__ = "attempts"

    id = db.Column(db.Integer, primary_key=True)

    student_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id")
    )

    quiz_id = db.Column(
        db.Integer,
        db.ForeignKey("quizzes.id")
    )

    # Nota do quiz
    score = db.Column(db.Float)

    student = db.relationship(
        "User",
        backref="attempts"
    )

    quiz = db.relationship(
        "Quiz",
        backref="attempts"
    )


# =========================
# RESPOSTAS
# =========================

class Answer(db.Model):

    __tablename__ = "answers"

    id = db.Column(db.Integer, primary_key=True)

    attempt_id = db.Column(
        db.Integer,
        db.ForeignKey("attempts.id")
    )

    question_id = db.Column(
        db.Integer,
        db.ForeignKey("questions.id")
    )

    student_answer = db.Column(
        db.String(100)
    )

    is_correct = db.Column(
        db.Boolean
    )

    attempt = db.relationship(
        "Attempt",
        backref="answers"
    )

    question = db.relationship(
        "Question"
    )