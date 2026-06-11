from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from blueprints.pedagogico import pedagogico_bp
from services.trilha_service import TrilhaService
from repositories.trilha_repository import AlunoRepository
from repositories.atividade_repository import AtividadeRepository
from models import Aluno
from extensions import db

trilha_svc = TrilhaService()
aluno_repo = AlunoRepository()
at_repo    = AtividadeRepository()

@pedagogico_bp.route("/")
@pedagogico_bp.route("/dashboard")
@login_required
def dashboard():
    trilhas = trilha_svc.listar_por_professor(current_user.id)
    alunos  = aluno_repo.listar_ativos()
    return render_template("pedagogico/dashboard.html", trilhas=trilhas, alunos=alunos)

@pedagogico_bp.route("/aluno/novo", methods=["GET","POST"])
@login_required
def novo_aluno():
    if request.method == "POST":
        a = Aluno(nome=request.form.get("nome","").strip(),
                  idade=int(request.form.get("idade",7)),
                  nivel_atual=request.form.get("nivel_atual","pre-silabico"))
        aluno_repo.salvar(a)
        flash(f"Aluno {a.nome} cadastrado!", "success")
        return redirect(url_for("pedagogico.dashboard"))
    return render_template("pedagogico/novo_aluno.html", niveis=Aluno.NIVEIS)

@pedagogico_bp.route("/trilha/nova", methods=["GET","POST"])
@login_required
def nova_trilha():
    alunos = aluno_repo.listar_ativos()
    if request.method == "POST":
        try:
            t = trilha_svc.criar_trilha(
                int(request.form.get("aluno_id")),
                current_user.id,
                request.form.get("titulo","").strip())
            flash("Trilha criada com IA!", "success")
            return redirect(url_for("pedagogico.ver_trilha", trilha_id=t.id))
        except Exception as e:
            flash(str(e), "danger")
    return render_template("pedagogico/nova_trilha.html", alunos=alunos)

@pedagogico_bp.route("/trilha/<int:trilha_id>")
@login_required
def ver_trilha(trilha_id):
    t = trilha_svc.buscar_por_id(trilha_id)
    if not t:
        flash("Trilha nao encontrada.", "danger")
        return redirect(url_for("pedagogico.dashboard"))
    ats = at_repo.buscar_por_trilha(trilha_id)
    return render_template("pedagogico/trilha.html", trilha=t, atividades=ats)

@pedagogico_bp.route("/atividade/<int:at_id>/concluir", methods=["POST"])
@login_required
def concluir_atividade(at_id):
    at = at_repo.marcar_concluida(at_id)
    flash("Atividade concluida!", "success")
    return redirect(url_for("pedagogico.ver_trilha", trilha_id=at.trilha_id))

@pedagogico_bp.route("/trilha/<int:trilha_id>/deletar", methods=["POST"])
@login_required
def deletar_trilha(trilha_id):
    trilha_svc.deletar(trilha_id)
    flash("Trilha removida.", "info")
    return redirect(url_for("pedagogico.dashboard"))
