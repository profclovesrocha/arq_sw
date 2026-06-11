import pytest
from app import create_app
from extensions import db as _db
from services.auth_service import AuthService

@pytest.fixture
def app():
    app = create_app("testing")
    with app.app_context():
        _db.create_all()
        yield app
        _db.drop_all()

def test_registrar(app):
    with app.app_context():
        u = AuthService().registrar("prof_x", "x@imip.br", "senha123")
        assert u.id is not None
        assert u.password_hash != "senha123"

def test_login_ok(app):
    with app.app_context():
        AuthService().registrar("prof_y", "y@imip.br", "abc456")
        u = AuthService().autenticar("y@imip.br", "abc456")
        assert u is not None

def test_login_senha_errada(app):
    with app.app_context():
        AuthService().registrar("prof_z", "z@imip.br", "correta")
        u = AuthService().autenticar("z@imip.br", "errada")
        assert u is None

def test_papel_invalido(app):
    with app.app_context():
        with pytest.raises(ValueError):
            AuthService().registrar("h", "h@h.com", "123", role="hacker")
