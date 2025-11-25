from dominio.vuelo import Vuelo


class GestorVuelos:
    def __init__(self, vuelo_repositorio, avion_repositorio, pasajero_repositorio):
        self.vuelo_repositorio = vuelo_repositorio
        self.avion_repositorio = avion_repositorio
        self.pasajero_repositorio = pasajero_repositorio
    
    def programar_vuelo(self, id_vuelo, codigo, origen, destino, horario, id_avion):
        avion = self.avion_repositorio.obtener_por_id(id_avion)
        if avion is None:
            return None
        vuelo = Vuelo(id_vuelo, codigo, origen, destino, horario, avion)
        self.vuelo_repositorio.agregar(vuelo)
        return vuelo
    
    def obtener_vuelo(self, id_vuelo):
        return self.vuelo_repositorio.obtener_por_id(id_vuelo)
    
    def listar_vuelos(self):
        return self.vuelo_repositorio.listar_todos()
    
    def asignar_pasajero_a_vuelo(self, id_vuelo, id_pasajero):
        vuelo = self.vuelo_repositorio.obtener_por_id(id_vuelo)
        if vuelo is None:
            return None
        pasajero = self.pasajero_repositorio.obtener_por_id(id_pasajero)
        if pasajero is None:
            return None
        vuelo.agregar_pasajero(pasajero)
        return vuelo
    
    def eliminar_pasajero_de_vuelo(self, id_vuelo, id_pasajero):
        vuelo = self.vuelo_repositorio.obtener_por_id(id_vuelo)
        if vuelo is None:
            return None
        pasajero = self.pasajero_repositorio.obtener_por_id(id_pasajero)
        if pasajero is None:
            return None
        vuelo.eliminar_pasajero(pasajero)
        return vuelo
    
    def cantidad_pasajeros_vuelo(self, id_vuelo):
        vuelo = self.vuelo_repositorio.obtener_por_id(id_vuelo)
        if vuelo is None:
            return 0
        return vuelo.cantidad_pasajeros()
    
    def peso_total_equipaje_vuelo(self, id_vuelo):
        vuelo = self.vuelo_repositorio.obtener_por_id(id_vuelo)
        if vuelo is None:
            return 0.0
        return vuelo.peso_total_equipaje()
    
    def tiene_capacidad_disponible(self, id_vuelo):
        vuelo = self.vuelo_repositorio.obtener_por_id(id_vuelo)
        if vuelo is None:
            return False
        return vuelo.tiene_capacidad_disponible()
