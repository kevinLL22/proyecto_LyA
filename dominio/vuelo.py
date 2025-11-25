class Vuelo:
    def __init__(self, id_vuelo, codigo, origen, destino, horario, avion):
        self.id_vuelo = id_vuelo
        self.codigo = codigo
        self.origen = origen
        self.destino = destino
        self.horario = horario
        self.avion = avion
        self.tripulacion = []
        self.pasajeros = []
    
    def agregar_pasajero(self, pasajero):
        if pasajero not in self.pasajeros:
            self.pasajeros.append(pasajero)
    
    def eliminar_pasajero(self, pasajero):
        if pasajero in self.pasajeros:
            self.pasajeros.remove(pasajero)
    
    def agregar_tripulante(self, tripulante):
        if tripulante not in self.tripulacion:
            self.tripulacion.append(tripulante)
    
    def cantidad_pasajeros(self):
        return len(self.pasajeros)
    
    def peso_total_equipaje(self):
        total = 0.0
        for pasajero in self.pasajeros:
            total += pasajero.peso_total_equipaje()
        return total
    
    def tiene_capacidad_disponible(self):
        cantidad = self.cantidad_pasajeros()
        peso = self.peso_total_equipaje()
        return self.avion.tiene_capacidad(cantidad, peso)
