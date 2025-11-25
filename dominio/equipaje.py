class Equipaje:
    def __init__(self, codigo_unico, peso, id_pasajero, descripcion=None):
        self.codigo_unico = codigo_unico
        self.peso = peso
        self.id_pasajero = id_pasajero
        self.descripcion = descripcion
