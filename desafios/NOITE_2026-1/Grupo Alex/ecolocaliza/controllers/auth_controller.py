from flask import Blueprint, render_template, request, redirect, url_for, session, flash
# Importação modificada para apontar corretamente para a classe
from models.user_model import User

auth_blueprint = Blueprint('auth', __name__)

# As rotas /login, /register e /logout permanecem EXATAMENTE iguais às anteriores, 
# pois a camada 'Controller' não precisa saber COMO o 'Model' salva os dados.
# (Isso prova que sua arquitetura MVC está perfeita!)

@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if User.verify_credentials(username, password):
            session['user'] = username
            return redirect(url_for('geo.dashboard'))
        else:
            flash('Usuário ou senha inválidos!', 'error')
            
    return render_template('login.html')

@auth_blueprint.route('/register', methods=['POST'])
def register():
    username = request.form.get('reg_username')
    password = request.form.get('reg_password')
    
    if not username or not password:
        flash('Preencha todos os campos para cadastrar.', 'error')
        return redirect(url_for('auth.login'))
        
    if User.register_user(username, password):
        flash('Cadastro realizado! Agora faça seu login.', 'success')
    else:
        flash('Este nome de usuário já está sendo usado.', 'error')
        
    return redirect(url_for('auth.login'))

@auth_blueprint.route('/login/google')
def google_login():
    """Rota simulada para o clique no botão do Google."""
    session['user'] = 'Explorador Google'
    return redirect(url_for('geo.dashboard'))

@auth_blueprint.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('auth.login'))