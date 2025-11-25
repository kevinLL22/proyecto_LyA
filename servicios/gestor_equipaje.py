from dominio.equipaje import Equipaje


class GestorEquipaje:
    def __init__(self, equipaje_repositorio, pasajero_repositorio, vuelo_repositorio):
        self.equipaje_repositorio = equipaje_repositorio
        self.pasajero_repositorio = pasajero_repositorio
        self.vuelo_repositorio = vuelo_repositorio
    
    def registrar_equipaje(self, codigo_unico, peso, id_pasajero, descripcion=None):
        equipaje = Equipaje(codigo_unico, peso, id_pasajero, descripcion)
        self.equipaje_repositorio.agregar(equipaje)
        pasajero = self.pasajero_repositorio.obtener_por_id(id_pasajero)
        if pasajero is not None:
            pasajero.agregar_equipaje(equipaje)
        return equipaje
    
    def listar_equipaje_por_pasajero(self, id_pasajero):
        return self.equipaje_repositorio.listar_por_pasajero(id_pasajero)
    
    def peso_total_por_pasajero(self, id_pasajero):
        pasajero = self.pasajero_repositorio.obtener_por_id(id_pasajero)
        if pasajero is not None:
            return pasajero.peso_total_equipaje()
        return 0.0
    
    def peso_total_por_vuelo(self, id_vuelo):
        vuelo = self.vuelo_repositorio.obtener_por_id(id_vuelo)
        if vuelo is not None:
            return vuelo.peso_total_equipaje()
        return 0.0
    
    def verificar_peso_maximo_vuelo(self, id_vuelo):
        vuelo = self.vuelo_repositorio.obtener_por_id(id_vuelo)
        if vuelo is None:
            return False
        avion = vuelo.avion
        peso_total = vuelo.peso_total_equipaje()
        if peso_total <= avion.peso_max_equipaje:
            return True
        return False
    
    def generar_alerta_sobrepeso(self, id_vuelo):
        if self.verificar_peso_maximo_vuelo(id_vuelo):
            return "El peso del equipaje está dentro del límite permitido."
        vuelo = self.vuelo_repositorio.obtener_por_id(id_vuelo)
        if vuelo is None:
            return None
        peso_total = vuelo.peso_total_equipaje()
        peso_max = vuelo.avion.peso_max_equipaje
        return f"ALERTA: El peso total del equipaje ({peso_total} kg) excede el límite máximo del avión ({peso_max} kg)."
