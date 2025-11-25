from repositorios.base_repositorio import BaseRepositorio


class EquipajeRepositorio(BaseRepositorio):
    def __init__(self):
        self._equipajes = []
    
    def agregar(self, equipaje):
        if self.obtener_por_id(equipaje.codigo_unico) is None:
            self._equipajes.append(equipaje)
    
    def obtener_por_id(self, codigo_unico):
        for equipaje in self._equipajes:
            if equipaje.codigo_unico == codigo_unico:
                return equipaje
        return None
    
    def listar_todos(self):
        return list(self._equipajes)
    
    def eliminar(self, codigo_unico):
        equipaje = self.obtener_por_id(codigo_unico)
        if equipaje is not None:
            self._equipajes.remove(equipaje)
            return True
        return False
    
    def listar_por_pasajero(self, id_pasajero):
        resultado = []
        for equipaje in self._equipajes:
            if equipaje.id_pasajero == id_pasajero:
                resultado.append(equipaje)
        return resultado
    
    def peso_total_por_pasajero(self, id_pasajero):
        total = 0.0
        for equipaje in self._equipajes:
            if equipaje.id_pasajero == id_pasajero:
                total += equipaje.peso
        return total
