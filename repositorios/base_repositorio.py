class BaseRepositorio:
    def agregar(self, entidad):
        raise NotImplementedError()
    
    def obtener_por_id(self, id_entidad):
        raise NotImplementedError()
    
    def listar_todos(self):
        raise NotImplementedError()
    
    def eliminar(self, id_entidad):
        raise NotImplementedError()
