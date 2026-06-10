from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.models import (
    Quiz,
    Question,
    Attempt,
    Answer
)

from app import db

quiz_bp = Blueprint(
    "quiz",
    __name__,
    url_prefix="/quizzes")

@quiz_bp.route("", methods=["GET"])
@jwt_required()

# ROTA PARA LISTAR QUIZZES
def get_quizzes():
    quizzes = Quiz.query.all()

    response = []
    for quiz in quizzes:
        response.append({
            "id": quiz.id,
            "title": quiz.title,
            "level": quiz.level
        })

    return jsonify(response), 200

# ENVIAR RESPOSTAS
@quiz_bp.route("/submit", methods=["POST"])
@jwt_required()
def submit_quiz():

    data = request.get_json()

    score = 0

    # Cria tentativa
    attempt = Attempt(
        student_id=get_jwt_identity(),
        quiz_id=data["quiz_id"],
        score=0
    )

    db.session.add(attempt)
    db.session.commit()

    # Percorre respostas
    for answer in data["answers"]:

        # Busca questão
        question = Question.query.get(
            answer["question_id"]
        )

        # Verifica acerto
        is_correct = (
            answer["student_answer"].lower()
            ==
            question.correct_answer.lower()
        )

        # Soma ponto
        if is_correct:
            score += 1

        # Salva resposta
        new_answer = Answer(
            attempt_id=attempt.id,
            question_id=question.id,
            student_answer=answer["student_answer"],
            is_correct=is_correct
        )

        db.session.add(new_answer)

    # Atualiza nota
    attempt.score = score

    db.session.commit()

    return jsonify({
        "message": "Quiz enviado",
        "score": score
    })