from flask import render_template, request, redirect, url_for, flash
from model import (
    create_aluno,
    list_alunos,
    create_professor,
    list_professores,
    create_plano,
    list_planos,
    get_plano,
    delete_plano,
    generate_decision_support_plan,
)


def init_app(app):
    @app.route("/")
    def homepage():
        planos = list_planos()
        return render_template("index.html", planos=planos)

    @app.route("/students")
    def list_students():
        students = list_alunos()
        return render_template("students.html", students=students)

    @app.route("/teachers")
    def list_teachers():
        teachers = list_professores()
        return render_template("teachers.html", teachers=teachers)

    @app.route("/students/new", methods=["GET", "POST"])
    def new_student():
        if request.method == "POST":
            nome = request.form.get("nome", "").strip()
            idade = request.form.get("idade", "").strip()
            turma = request.form.get("turma", "").strip()
            internacao = request.form.get("internacao", "").strip()

            if not nome:
                flash("Nome do aluno é obrigatório", "danger")
                return redirect(url_for("new_student"))

            create_aluno(nome, int(idade) if idade.isdigit() else None, turma, internacao)
            flash("Aluno registrado com sucesso", "success")
            return redirect(url_for("list_students"))

        return render_template("student_form.html")

    @app.route("/teachers/new", methods=["GET", "POST"])
    def new_teacher():
        if request.method == "POST":
            nome = request.form.get("nome", "").strip()
            area = request.form.get("area", "").strip()
            contato = request.form.get("contato", "").strip()

            if not nome:
                flash("Nome do professor é obrigatório", "danger")
                return redirect(url_for("new_teacher"))

            create_professor(nome, area, contato)
            flash("Professor registrado com sucesso", "success")
            return redirect(url_for("list_teachers"))

        return render_template("teacher_form.html")

    @app.route("/plans/new", methods=["GET", "POST"])
    def create_pedagogical_plan():
        students = list_alunos()
        teachers = list_professores()

        if request.method == "POST":
            aluno_id = request.form.get("aluno_id")
            professor_id = request.form.get("professor_id")
            metas = request.form.get("metas", "").strip()
            estado_emocional = request.form.get("estado_emocional", "").strip()

            if not aluno_id or not metas:
                flash("Selecione o aluno e informe as metas de aprendizagem", "danger")
                return redirect(url_for("create_pedagogical_plan"))

            aluno = next((s for s in students if s["id"] == int(aluno_id)), None)
            professor = next((t for t in teachers if t["id"] == int(professor_id)), None) if professor_id else None

            roteiro = generate_decision_support_plan(
                student_name=aluno["nome"],
                age=str(aluno["idade"]) if aluno["idade"] is not None else "não informado",
                condition=aluno["internacao"] or "Não especificado",
                learning_goals=metas,
                emotional_state=estado_emocional or "estável"
            )

            create_plano(
                aluno_id=int(aluno_id),
                professor_id=int(professor_id) if professor_id else None,
                titulo=f"Plano para {aluno['nome']}",
                metas=metas,
                estado_emocional=estado_emocional,
                roteiro=roteiro,
            )
            flash("Plano pedagógico criado com sucesso", "success")
            return redirect(url_for("homepage"))

        return render_template("plan_form.html", students=students, teachers=teachers)

    @app.route("/plans/<int:plan_id>")
    def show_plan(plan_id):
        plan = get_plano(plan_id)
        if not plan:
            flash("Plano não encontrado.", "warning")
            return redirect(url_for("homepage"))
        return render_template("plan.html", plan=plan)

    @app.route("/plans/<int:plan_id>/delete", methods=["POST"])
    def remove_plan(plan_id):
        delete_plano(plan_id)
        flash("Plano removido", "success")
        return redirect(url_for("homepage"))




