from dominio.persona import Persona


class Usuario(Persona):
    def __init__(self, id_persona, nombre, documento, email, telefono, nombre_usuario, password, rol):
        super().__init__(id_persona, nombre, documento, email, telefono)
        self.nombre_usuario = nombre_usuario
        self.password = password
        self.rol = rol
