class Usuario:
    def __init__(self, id_usuario: int, username: str, password: str, rol: str):
        self.id_usuario = id_usuario
        self.username = username
        self.password = password
        self.rol = rol

    def to_dict(self):
        return {
            "id_usuario": self.id_usuario,
            "username": self.username,
            "password": self.password,
            "rol": self.rol
        }

    @staticmethod
    def from_dict(data):
        return Usuario(
            id_usuario=int(data.get("id_usuario")),
            username=str(data.get("username")),
            password=str(data.get("password")),
            rol=str(data.get("rol"))
        )
