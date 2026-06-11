from repositories.user_repository import UserRepository
from models import User

class AuthService:
    def __init__(self):
        self.repo = UserRepository()

    def autenticar(self, email, senha):
        u = self.repo.buscar_por_email(email)
        if u and u.ativo and u.check_password(senha):
            return u
        return None

    def registrar(self, username, email, senha, role="professor"):
        if role not in User.ROLES:
            raise ValueError(f"Papel invalido: {role}")
        if self.repo.buscar_por_email(email):
            raise ValueError("E-mail ja cadastrado.")
        u = User(username=username, email=email, role=role)
        u.set_password(senha)
        return self.repo.salvar(u)
