from repositorios.base_repositorio import BaseRepositorio


class PasajeroRepositorio(BaseRepositorio):
    def __init__(self):
        self._pasajeros = []
    
    def agregar(self, pasajero):
        if self.obtener_por_id(pasajero.id_persona) is None:
            self._pasajeros.append(pasajero)
    
    def obtener_por_id(self, id_persona):
        for pasajero in self._pasajeros:
            if pasajero.id_persona == id_persona:
                return pasajero
        return None
    
    def listar_todos(self):
        return list(self._pasajeros)
    
    def eliminar(self, id_persona):
        pasajero = self.obtener_por_id(id_persona)
        if pasajero is not None:
            self._pasajeros.remove(pasajero)
            return True
        return False
    
    def buscar_por_documento(self, documento):
        for pasajero in self._pasajeros:
            if pasajero.documento == documento:
                return pasajero
        return None
    
    def buscar_por_nombre(self, nombre):
        resultado = []
        nombre_lower = nombre.lower()
        for pasajero in self._pasajeros:
            if nombre_lower in pasajero.nombre.lower():
                resultado.append(pasajero)
        return resultado
