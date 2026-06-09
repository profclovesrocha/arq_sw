class User:
    # Usuário de teste simulado
    USER_DATA = {
        "admin": "senha123"
    }

    @classmethod
    def verify_credentials(cls, username, password):
        """Verifica se o usuário existe e a senha está correta."""
        if username in cls.USER_DATA and cls.USER_DATA[username] == password:
            return True
            
        return False