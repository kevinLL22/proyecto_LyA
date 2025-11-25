from repositorios.avion_repositorio import AvionRepositorio
from repositorios.vuelo_repositorio import VueloRepositorio
from repositorios.pasajero_repositorio import PasajeroRepositorio
from repositorios.equipaje_repositorio import EquipajeRepositorio
from servicios.gestor_aviones import GestorAviones
from servicios.gestor_vuelos import GestorVuelos
from servicios.gestor_pasajeros import GestorPasajeros
from servicios.gestor_equipaje import GestorEquipaje
from servicios.gestor_reportes import GestorReportes
from interfaz.consola_app import ConsolaApp


def main():
    avion_repositorio = AvionRepositorio()
    vuelo_repositorio = VueloRepositorio()
    pasajero_repositorio = PasajeroRepositorio()
    equipaje_repositorio = EquipajeRepositorio()
    
    gestor_aviones = GestorAviones(avion_repositorio)
    gestor_pasajeros = GestorPasajeros(pasajero_repositorio)
    gestor_vuelos = GestorVuelos(vuelo_repositorio, avion_repositorio, pasajero_repositorio)
    gestor_equipaje = GestorEquipaje(equipaje_repositorio, pasajero_repositorio, vuelo_repositorio)
    gestor_reportes = GestorReportes(vuelo_repositorio)
    
    app = ConsolaApp(gestor_aviones, gestor_vuelos, gestor_pasajeros, gestor_equipaje, gestor_reportes)
    app.ejecutar()


if __name__ == "__main__":
    main()
