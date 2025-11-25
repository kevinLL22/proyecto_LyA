from dominio.persona import Persona


class Pasajero(Persona):
    def __init__(self, id_persona, nombre, documento, email, telefono, codigo_pasajero):
        super().__init__(id_persona, nombre, documento, email, telefono)
        self.codigo_pasajero = codigo_pasajero
        self.equipajes = []
    
    def agregar_equipaje(self, equipaje):
        if equipaje not in self.equipajes:
            self.equipajes.append(equipaje)
    
    def peso_total_equipaje(self):
        total = 0.0
        for equipaje in self.equipajes:
            total += equipaje.peso
        return total
