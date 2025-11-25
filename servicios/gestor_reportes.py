class GestorReportes:
    def __init__(self, vuelo_repositorio):
        self.vuelo_repositorio = vuelo_repositorio
    
    def reporte_vuelos_con_pasajeros_y_carga(self):
        vuelos = self.vuelo_repositorio.listar_todos()
        resultado = []
        for vuelo in vuelos:
            dato = {
                'id_vuelo': vuelo.id_vuelo,
                'codigo': vuelo.codigo,
                'origen': vuelo.origen,
                'destino': vuelo.destino,
                'cantidad_pasajeros': vuelo.cantidad_pasajeros(),
                'peso_total_equipaje': vuelo.peso_total_equipaje()
            }
            resultado.append(dato)
        return resultado
    
    def reporte_peso_equipaje_por_vuelo(self):
        vuelos = self.vuelo_repositorio.listar_todos()
        resultado = []
        for vuelo in vuelos:
            dato = {
                'codigo': vuelo.codigo,
                'peso_total_equipaje': vuelo.peso_total_equipaje()
            }
            resultado.append(dato)
        return resultado
