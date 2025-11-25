from dominio.avion import Avion


class GestorAviones:
    def __init__(self, avion_repositorio):
        self.avion_repositorio = avion_repositorio
    
    def registrar_avion(self, id_avion, modelo, matricula, msn, capacidad_pasajeros, peso_max_equipaje):
        avion = Avion(id_avion, modelo, matricula, msn, capacidad_pasajeros, peso_max_equipaje)
        self.avion_repositorio.agregar(avion)
        return avion
    
    def obtener_avion(self, id_avion):
        return self.avion_repositorio.obtener_por_id(id_avion)
    
    def listar_aviones(self):
        return self.avion_repositorio.listar_todos()
    
    def buscar_por_matricula(self, matricula):
        return self.avion_repositorio.buscar_por_matricula(matricula)
    
    def buscar_por_msn(self, msn):
        return self.avion_repositorio.buscar_por_msn(msn)
