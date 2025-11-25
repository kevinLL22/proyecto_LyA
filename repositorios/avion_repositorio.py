from repositorios.base_repositorio import BaseRepositorio


class AvionRepositorio(BaseRepositorio):
    def __init__(self):
        self._aviones = []
    
    def agregar(self, avion):
        if self.obtener_por_id(avion.id_avion) is None:
            self._aviones.append(avion)
    
    def obtener_por_id(self, id_avion):
        for avion in self._aviones:
            if avion.id_avion == id_avion:
                return avion
        return None
    
    def listar_todos(self):
        return list(self._aviones)
    
    def eliminar(self, id_avion):
        avion = self.obtener_por_id(id_avion)
        if avion is not None:
            self._aviones.remove(avion)
            return True
        return False
    
    def buscar_por_matricula(self, matricula):
        for avion in self._aviones:
            if avion.matricula == matricula:
                return avion
        return None
    
    def buscar_por_msn(self, msn):
        for avion in self._aviones:
            if avion.msn == msn:
                return avion
        return None
