from flask import render_template
from flask_login import login_required
from blueprints.relatorios import relatorios_bp
from services.relatorio_service import RelatorioService

svc = RelatorioService()

@relatorios_bp.route("/")
@login_required
def index():
    return render_template("relatorios/index.html", alunos=svc.listar_alunos())

@relatorios_bp.route("/aluno/<int:aluno_id>")
@login_required
def progresso(aluno_id):
    dados = svc.progresso_aluno(aluno_id)
    return render_template("relatorios/progresso.html", **dados)
