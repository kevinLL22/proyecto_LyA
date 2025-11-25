import datetime


class Horario:
    def __init__(self, salida, llegada):
        self.salida = salida
        self.llegada = llegada
    
    def duracion_minutos(self):
        diferencia = self.llegada - self.salida
        return int(diferencia.total_seconds() / 60)

