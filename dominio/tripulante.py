from dominio.persona import Persona


class Tripulante(Persona):
    def __init__(self, id_persona, nombre, documento, email, telefono, rol_tripulacion, licencia):
        super().__init__(id_persona, nombre, documento, email, telefono)
        self.rol_tripulacion = rol_tripulacion
        self.licencia = licencia

