from flask import Blueprint, render_template, request, session, redirect, url_for, jsonify

geo_blueprint = Blueprint('geo', __name__)

@geo_blueprint.route('/dashboard')
def dashboard():
    # Proteção de rota: se não estiver logado, volta para o login
    if 'user' not in session:
        return redirect(url_for('auth.login'))
    return render_template('dashboard.html', username=session['user'])

@geo_blueprint.route('/api/save-geo', methods=['POST'])
def save_geolocation():
    """Recebe a geolocalização enviada pelo JavaScript via POST"""
    if 'user' not in session:
        return jsonify({"status": "error", "message": "Não autorizado"}), 401
        
    data = request.get_json()
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    
    # Aqui o seu Model poderia salvar esses dados no banco de dados.
    print(f"Geolocalização recebida de {session['user']}: Lat {latitude}, Lon {longitude}")
    
    return jsonify({"status": "success", "message": "Coordenadas recebidas no servidor!"})