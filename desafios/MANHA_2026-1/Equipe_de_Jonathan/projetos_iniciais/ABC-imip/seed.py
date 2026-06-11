from app import create_app, db
from app.models import Quiz, Question

app = create_app()

with app.app_context():

    # Evita criar duplicado
    existing_quiz = Quiz.query.filter_by(title="Vogais").first()

    if existing_quiz:
        print("Quiz já existe.")
        exit()

    quiz = Quiz(
        title="Vogais",
        level="Fácil"
    )

    db.session.add(quiz)
    db.session.commit()

    questions = [

        Question(
            quiz_id=quiz.id,
            word_with_missing="C_SA",
            correct_answer="A"
        ),

        Question(
            quiz_id=quiz.id,
            word_with_missing="M_SA",
            correct_answer="E"
        ),

        Question(
            quiz_id=quiz.id,
            word_with_missing="B_LA",
            correct_answer="O"
        )

    ]

    db.session.add_all(questions)

    db.session.commit()

    print("Dados inseridos com sucesso!")