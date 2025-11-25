from repositorios.base_repositorio import BaseRepositorio


class VueloRepositorio(BaseRepositorio):
    def __init__(self):
        self._vuelos = []
    
    def agregar(self, vuelo):
        if self.obtener_por_id(vuelo.id_vuelo) is None:
            self._vuelos.append(vuelo)
    
    def obtener_por_id(self, id_vuelo):
        for vuelo in self._vuelos:
            if vuelo.id_vuelo == id_vuelo:
                return vuelo
        return None
    
    def listar_todos(self):
        return list(self._vuelos)
    
    def eliminar(self, id_vuelo):
        vuelo = self.obtener_por_id(id_vuelo)
        if vuelo is not None:
            self._vuelos.remove(vuelo)
            return True
        return False
    
    def obtener_vuelos_por_avion(self, id_avion):
        resultado = []
        for vuelo in self._vuelos:
            if vuelo.avion.id_avion == id_avion:
                resultado.append(vuelo)
        return resultado
    
    def obtener_vuelos_por_rango_fechas(self, fecha_inicio, fecha_fin):
        resultado = []
        for vuelo in self._vuelos:
            if fecha_inicio <= vuelo.horario.salida <= fecha_fin:
                resultado.append(vuelo)
        return resultado
