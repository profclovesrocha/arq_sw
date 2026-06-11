from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from blueprints.auth import auth_bp
from services.auth_service import AuthService

svc = AuthService()

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("pedagogico.dashboard"))
    if request.method == "POST":
        u = svc.autenticar(request.form.get("email","").strip(),
                           request.form.get("password",""))
        if u:
            login_user(u)
            return redirect(url_for("pedagogico.dashboard"))
        flash("E-mail ou senha invalidos.", "danger")
    return render_template("auth/login.html")

@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))

@auth_bp.route("/registro", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        try:
            svc.registrar(request.form.get("username","").strip(),
                          request.form.get("email","").strip(),
                          request.form.get("password",""),
                          request.form.get("role","professor"))
            flash("Conta criada! Faca login.", "success")
            return redirect(url_for("auth.login"))
        except ValueError as e:
            flash(str(e), "danger")
    return render_template("auth/registro.html")
