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
    url_prefix="/quizzes"
)


# =========================
# LISTAR QUIZZES
# GET /quizzes
# =========================
@quiz_bp.route("", methods=["GET"])
#@jwt_required()
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


# =========================
# BUSCAR QUIZ POR ID
# GET /quizzes/<id>
# =========================
@quiz_bp.route("/<int:quiz_id>", methods=["GET"])
#@jwt_required()
def get_quiz(quiz_id):

    quiz = Quiz.query.get(quiz_id)

    if not quiz:
        return jsonify({
            "error": "Quiz não encontrado"
        }), 404

    questions = Question.query.filter_by(
        quiz_id=quiz_id
    ).all()

    return jsonify({
        "id": quiz.id,
        "title": quiz.title,
        "level": quiz.level,
        "questions": [
            {
                "id": question.id,
                "word_with_missing": question.word_with_missing
            }
            for question in questions
        ]
    }), 200


# =========================
# ENVIAR RESPOSTAS
# POST /quizzes/submit
# =========================
@quiz_bp.route("/submit", methods=["POST"])
#@jwt_required()
def submit_quiz():

    try:

        data = request.get_json()

        if not data:
            return jsonify({
                "error": "Corpo da requisição inválido"
            }), 400

        quiz_id = data.get("quiz_id")
        answers = data.get("answers")

        if not quiz_id:
            return jsonify({
                "error": "quiz_id é obrigatório"
            }), 400

        if not answers:
            return jsonify({
                "error": "answers é obrigatório"
            }), 400

        # Verifica se o quiz existe
        quiz = Quiz.query.get(quiz_id)

        if not quiz:
            return jsonify({
                "error": "Quiz não encontrado"
            }), 404

        score = 0

        # Cria tentativa
        attempt = Attempt(
            student_id=1,
            quiz_id=quiz_id,
            score=0
        )

        db.session.add(attempt)

        # Gera ID sem commit
        db.session.flush()

        # Corrige respostas
        for answer in answers:

            question = Question.query.get(
                answer.get("question_id")
            )

            if not question:
                return jsonify({
                    "error": f"Questão {answer.get('question_id')} não encontrada"
                }), 404

            # Segurança:
            # garante que a questão pertence ao quiz enviado
            if question.quiz_id != quiz_id:
                return jsonify({
                    "error": f"A questão {question.id} não pertence ao quiz informado"
                }), 400

            student_answer = answer.get(
                "student_answer",
                ""
            )

            is_correct = (
                student_answer.strip().lower()
                ==
                question.correct_answer.strip().lower()
            )

            if is_correct:
                score += 1

            new_answer = Answer(
                attempt_id=attempt.id,
                question_id=question.id,
                student_answer=student_answer,
                is_correct=is_correct
            )

            db.session.add(new_answer)

        # Atualiza nota final
        attempt.score = score

        db.session.commit()

        total_questions = len(answers)

        return jsonify({
            "message": "Quiz enviado com sucesso",
            "attempt_id": attempt.id,
            "quiz_id": quiz_id,
            "score": score,
            "total_questions": total_questions,
            "correct_answers": score,
            "wrong_answers": total_questions - score
        }), 200

    except Exception as e:

        db.session.rollback()

        return jsonify({
            "error": "Erro ao processar o quiz",
            "details": str(e)
        }), 500