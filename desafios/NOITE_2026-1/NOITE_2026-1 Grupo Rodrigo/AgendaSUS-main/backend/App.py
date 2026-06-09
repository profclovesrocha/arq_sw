from flask import Flask, render_template
import os
from flask_cors import CORS
from controllers.user_controller import user_bp
from controllers.appointment_controller import appointment_bp
from controllers.schedule_controller import schedule_bp
from controllers.clinic_controller import clinic_bp
from controllers.specialtie_controller import specialtie_bp

base_dir = os.path.abspath(os.path.dirname(__file__))

template_dir = os.path.join(base_dir, '.frontend', 'dist')
static_dir = os.path.join(base_dir, '.frontend', 'dist', 'assets')

app = Flask(
    __name__,
    static_folder=static_dir,
    template_folder=template_dir,
    static_url_path='/assets'
)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

app.register_blueprint(user_bp, url_prefix='/api')
app.register_blueprint(appointment_bp, url_prefix='/api')
app.register_blueprint(schedule_bp, url_prefix='/api')
app.register_blueprint(clinic_bp, url_prefix='/api')
app.register_blueprint(specialtie_bp, url_prefix='/api') 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)