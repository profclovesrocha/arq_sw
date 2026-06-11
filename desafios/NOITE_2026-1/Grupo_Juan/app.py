from flask import Flask, render_template, redirect, url_for, flash, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'eduhosp-secret-2024'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///eduhosp.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20), default='student')
    hospital = db.Column(db.String(150))
    ward = db.Column(db.String(100))
    age = db.Column(db.Integer)
    avatar_color = db.Column(db.String(20), default='#4f9cf9')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    enrollments = db.relationship('Enrollment', backref='student', lazy=True, foreign_keys='Enrollment.student_id')
    taught_classes = db.relationship('Classroom', backref='teacher', lazy=True)

class Classroom(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    subject = db.Column(db.String(100))
    description = db.Column(db.Text)
    teacher_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    color = db.Column(db.String(20), default='#4f9cf9')
    code = db.Column(db.String(10), unique=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    posts = db.relationship('Post', backref='classroom', lazy=True, cascade='all, delete-orphan')
    enrollments = db.relationship('Enrollment', backref='classroom', lazy=True, cascade='all, delete-orphan')

class Enrollment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    classroom_id = db.Column(db.Integer, db.ForeignKey('classroom.id'), nullable=False)
    joined_at = db.Column(db.DateTime, default=datetime.utcnow)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    content = db.Column(db.Text, nullable=False)
    post_type = db.Column(db.String(20), default='announcement')
    classroom_id = db.Column(db.Integer, db.ForeignKey('classroom.id'), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    due_date = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    author = db.relationship('User', backref='posts')
    comments = db.relationship('Comment', backref='post', lazy=True, cascade='all, delete-orphan')

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    author = db.relationship('User', backref='comments')

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

import random, string

def gen_code():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

COLORS = ['#e74c8b', '#4f9cf9', '#27ae60', '#f39c12', '#8e44ad', '#16a085', '#e67e22', '#2980b9']

@app.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password_hash, password):
            login_user(user, remember=True)
            return redirect(url_for('dashboard'))
        flash('E-mail ou senha incorretos.', 'error')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        role = request.form.get('role', 'student')
        hospital = request.form.get('hospital', '')
        ward = request.form.get('ward', '')
        age = request.form.get('age', None)

        if User.query.filter_by(email=email).first():
            flash('Este e-mail já está cadastrado.', 'error')
            return render_template('register.html')

        user = User(
            name=name, email=email,
            password_hash=generate_password_hash(password),
            role=role, hospital=hospital, ward=ward,
            age=int(age) if age else None,
            avatar_color=random.choice(COLORS)
        )
        db.session.add(user)
        db.session.commit()
        login_user(user)
        flash('Bem-vindo(a) ao Ravix!', 'success')
        return redirect(url_for('dashboard'))
    return render_template('register.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/dashboard')
@login_required
def dashboard():
    if current_user.role == 'teacher':
        classrooms = Classroom.query.filter_by(teacher_id=current_user.id).all()
    else:
        enrollments = Enrollment.query.filter_by(student_id=current_user.id).all()
        classrooms = [e.classroom for e in enrollments]
    
    classroom_ids = [c.id for c in classrooms]
    if classroom_ids:
        recent_posts = Post.query.filter(Post.classroom_id.in_(classroom_ids)).order_by(Post.created_at.desc()).limit(5).all()
    else:
        recent_posts = []

    total_students = 0
    if current_user.role == 'teacher':
        total_students = sum(len(c.enrollments) for c in classrooms)
    else:
        total_students = len(classrooms)
    
    return render_template('dashboard.html', classrooms=classrooms, recent_posts=recent_posts, total_students=total_students)

@app.route('/classroom/create', methods=['GET', 'POST'])
@login_required
def create_classroom():
    if current_user.role != 'teacher':
        flash('Apenas professores podem criar turmas.', 'error')
        return redirect(url_for('dashboard'))
    if request.method == 'POST':
        classroom = Classroom(
            name=request.form.get('name'),
            subject=request.form.get('subject'),
            description=request.form.get('description'),
            teacher_id=current_user.id,
            color=request.form.get('color', random.choice(COLORS)),
            code=gen_code()
        )
        db.session.add(classroom)
        db.session.commit()
        flash('Turma criada com sucesso!', 'success')
        return redirect(url_for('classroom_view', cid=classroom.id))
    return render_template('create_classroom.html', colors=COLORS)

@app.route('/classroom/join', methods=['POST'])
@login_required
def join_classroom():
    code = request.form.get('code', '').strip().upper()
    classroom = Classroom.query.filter_by(code=code).first()
    if not classroom:
        flash('Código de turma inválido.', 'error')
        return redirect(url_for('dashboard'))
    existing = Enrollment.query.filter_by(student_id=current_user.id, classroom_id=classroom.id).first()
    if existing:
        flash('Você já está nessa turma.', 'info')
        return redirect(url_for('classroom_view', cid=classroom.id))
    enrollment = Enrollment(student_id=current_user.id, classroom_id=classroom.id)
    db.session.add(enrollment)
    db.session.commit()
    flash(f'Você entrou na turma "{classroom.name}"!', 'success')
    return redirect(url_for('classroom_view', cid=classroom.id))

@app.route('/classroom/<int:cid>')
@login_required
def classroom_view(cid):
    classroom = Classroom.query.get_or_404(cid)
    if current_user.role == 'teacher' and classroom.teacher_id != current_user.id:
        flash('Acesso negado.', 'error')
        return redirect(url_for('dashboard'))
    if current_user.role == 'student':
        enrollment = Enrollment.query.filter_by(student_id=current_user.id, classroom_id=cid).first()
        if not enrollment:
            flash('Você não está inscrito nessa turma.', 'error')
            return redirect(url_for('dashboard'))
    
    posts = Post.query.filter_by(classroom_id=cid).order_by(Post.created_at.desc()).all()
    students = User.query.join(Enrollment, Enrollment.student_id == User.id).filter(Enrollment.classroom_id == cid).all()
    return render_template('classroom.html', classroom=classroom, posts=posts, students=students)

@app.route('/classroom/<int:cid>/post', methods=['POST'])
@login_required
def create_post(cid):
    classroom = Classroom.query.get_or_404(cid)
    if classroom.teacher_id != current_user.id:
        return jsonify({'error': 'Não autorizado'}), 403
    
    due_date = None
    due_str = request.form.get('due_date')
    if due_str:
        try:
            due_date = datetime.strptime(due_str, '%Y-%m-%dT%H:%M')
        except:
            pass

    post = Post(
        title=request.form.get('title'),
        content=request.form.get('content'),
        post_type=request.form.get('post_type', 'announcement'),
        classroom_id=cid,
        author_id=current_user.id,
        due_date=due_date
    )
    db.session.add(post)
    db.session.commit()
    flash('Publicado com sucesso!', 'success')
    return redirect(url_for('classroom_view', cid=cid))

@app.route('/post/<int:pid>/comment', methods=['POST'])
@login_required
def add_comment(pid):
    post = Post.query.get_or_404(pid)
    content = request.form.get('content', '').strip()
    if content:
        comment = Comment(content=content, post_id=pid, author_id=current_user.id)
        db.session.add(comment)
        db.session.commit()
    return redirect(url_for('classroom_view', cid=post.classroom_id))

@app.route('/post/<int:pid>/delete', methods=['POST'])
@login_required
def delete_post(pid):
    post = Post.query.get_or_404(pid)
    classroom = post.classroom
    if classroom.teacher_id != current_user.id:
        flash('Não autorizado.', 'error')
        return redirect(url_for('classroom_view', cid=classroom.id))
    db.session.delete(post)
    db.session.commit()
    flash('Publicação removida.', 'success')
    return redirect(url_for('classroom_view', cid=classroom.id))

@app.route('/profile')
@login_required
def profile():
    if current_user.role == 'teacher':
        classrooms = Classroom.query.filter_by(teacher_id=current_user.id).all()
        total_students = sum(len(c.enrollments) for c in classrooms)
        total_posts = sum(len(c.posts) for c in classrooms)
        return render_template('profile.html', classrooms=classrooms, total_students=total_students, total_posts=total_posts)
    else:
        enrollments = Enrollment.query.filter_by(student_id=current_user.id).all()
        classrooms = [e.classroom for e in enrollments]
        return render_template('profile.html', classrooms=classrooms, total_students=0, total_posts=0)

def seed():
    with app.app_context():
        db.create_all()
        if not User.query.first():
            teacher = User(
                name='Professora Ana Lima',
                email='ana@ravix.com',
                password_hash=generate_password_hash('123456'),
                role='teacher',
                hospital='Hospital das Clínicas',
                avatar_color='#e74c8b'
            )
            student = User(
                name='Lucas Oliveira',
                email='lucas@ravix.com',
                password_hash=generate_password_hash('123456'),
                role='student',
                hospital='Hospital das Clínicas',
                ward='Pediatria - Ala B',
                age=14,
                avatar_color='#4f9cf9'
            )
            db.session.add_all([teacher, student])
            db.session.commit()

            classroom = Classroom(
                name='Matemática 9º Ano',
                subject='Matemática',
                description='Turma de matemática para alunos internados. Vamos aprender juntos! 💙',
                teacher_id=teacher.id,
                color='#4f9cf9',
                code='MAT001'
            )
            db.session.add(classroom)
            db.session.commit()

            enrollment = Enrollment(student_id=student.id, classroom_id=classroom.id)
            db.session.add(enrollment)

            posts = [
                Post(title='Bem-vindos à turma!',
                     content='Olá a todos! Estou muito feliz em poder continuar os estudos com vocês aqui. Lembrem-se: a doença pode parar o corpo, mas nunca a mente! 🌟',
                     post_type='announcement', classroom_id=classroom.id, author_id=teacher.id),
                Post(title='Atividade: Frações no dia a dia',
                     content='Pessoal, quero que vocês observem algo no hospital que possa ser representado por frações. Pode ser a divisão de um prato, horário de remédios, etc. Descrevam no comentário!',
                     post_type='assignment', classroom_id=classroom.id, author_id=teacher.id),
                Post(title='Material: Introdução a Geometria',
                     content='Aqui está o resumo que preparei sobre formas geométricas. Reparem nas formas ao redor do quarto! Janelas retangulares, relógios circulares... a geometria está em todo lugar! 📐',
                     post_type='material', classroom_id=classroom.id, author_id=teacher.id),
            ]
            db.session.add_all(posts)
            db.session.commit()

if __name__ == '__main__':
    seed()
    app.run(debug=True, port=5000)
