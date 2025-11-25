from dominio.pasajero import Pasajero


class GestorPasajeros:
    def __init__(self, pasajero_repositorio):
        self.pasajero_repositorio = pasajero_repositorio
    
    def registrar_pasajero(self, id_persona, nombre, documento, email, telefono, codigo_pasajero):
        pasajero = Pasajero(id_persona, nombre, documento, email, telefono, codigo_pasajero)
        self.pasajero_repositorio.agregar(pasajero)
        return pasajero
    
    def obtener_pasajero(self, id_persona):
        return self.pasajero_repositorio.obtener_por_id(id_persona)
    
    def listar_pasajeros(self):
        return self.pasajero_repositorio.listar_todos()
    
    def buscar_por_documento(self, documento):
        return self.pasajero_repositorio.buscar_por_documento(documento)
    
    def buscar_por_nombre(self, nombre):
        return self.pasajero_repositorio.buscar_por_nombre(nombre)
