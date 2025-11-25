class Avion:
    def __init__(self, id_avion, modelo, matricula, msn, capacidad_pasajeros, peso_max_equipaje):
        self.id_avion = id_avion
        self.modelo = modelo
        self.matricula = matricula
        self.msn = msn
        self.capacidad_pasajeros = capacidad_pasajeros
        self.peso_max_equipaje = peso_max_equipaje
    
    def tiene_capacidad(self, cantidad_pasajeros, peso_equipaje_total):
        if cantidad_pasajeros <= self.capacidad_pasajeros and peso_equipaje_total <= self.peso_max_equipaje:
            return True
        return False
