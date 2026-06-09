from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from models.user_model import User

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if User.verify_credentials(username, password):
            session['user'] = username  # Cria a sessão do usuário
            return redirect(url_for('geo.dashboard'))
        else:
            flash('Usuário ou senha inválidos!', 'error')
            
    return render_template('login.html')

@auth_blueprint.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('auth.login'))