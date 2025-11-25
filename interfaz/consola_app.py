import datetime
from dominio.horario import Horario


class ConsolaApp:
    def __init__(self, gestor_aviones, gestor_vuelos, gestor_pasajeros, gestor_equipaje, gestor_reportes):
        self.gestor_aviones = gestor_aviones
        self.gestor_vuelos = gestor_vuelos
        self.gestor_pasajeros = gestor_pasajeros
        self.gestor_equipaje = gestor_equipaje
        self.gestor_reportes = gestor_reportes
    
    def ejecutar(self):
        while True:
            opcion = self.mostrar_menu_principal()
            if opcion == "0":
                print("Saliendo del sistema...")
                break
            elif opcion == "1":
                self._menu_gestion_aviones()
            elif opcion == "2":
                self._menu_gestion_pasajeros()
            elif opcion == "3":
                self._menu_gestion_vuelos()
            elif opcion == "4":
                self._menu_gestion_equipaje()
            elif opcion == "5":
                self._menu_reportes()
            else:
                print("Opción inválida. Intente nuevamente.")
    
    def mostrar_menu_principal(self):
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Gestión de aviones")
        print("2. Gestión de pasajeros")
        print("3. Gestión de vuelos")
        print("4. Gestión de equipaje")
        print("5. Reportes")
        print("0. Salir")
        opcion = input("Seleccione una opción: ")
        return opcion
    
    def _menu_gestion_aviones(self):
        while True:
            print("\n=== GESTIÓN DE AVIONES ===")
            print("1. Registrar avión")
            print("2. Listar aviones")
            print("3. Buscar avión por matrícula")
            print("0. Volver al menú principal")
            opcion = input("Seleccione una opción: ")
            
            if opcion == "0":
                break
            elif opcion == "1":
                id_avion = input("ID del avión: ")
                modelo = input("Modelo: ")
                matricula = input("Matrícula: ")
                msn = input("MSN: ")
                capacidad = int(input("Capacidad de pasajeros: "))
                peso_max = float(input("Peso máximo de equipaje (kg): "))
                avion = self.gestor_aviones.registrar_avion(id_avion, modelo, matricula, msn, capacidad, peso_max)
                if avion:
                    print(f"Avión {avion.matricula} registrado correctamente.")
            elif opcion == "2":
                aviones = self.gestor_aviones.listar_aviones()
                if aviones:
                    print("\nLista de aviones:")
                    for avion in aviones:
                        print(f"ID: {avion.id_avion}, Modelo: {avion.modelo}, Matrícula: {avion.matricula}, "
                              f"Capacidad: {avion.capacidad_pasajeros}, Peso máx: {avion.peso_max_equipaje} kg")
                else:
                    print("No hay aviones registrados.")
            elif opcion == "3":
                matricula = input("Ingrese la matrícula: ")
                avion = self.gestor_aviones.buscar_por_matricula(matricula)
                if avion:
                    print(f"Avión encontrado: {avion.modelo} - {avion.matricula}")
                else:
                    print("Avión no encontrado.")
            else:
                print("Opción inválida.")
    
    def _menu_gestion_pasajeros(self):
        while True:
            print("\n=== GESTIÓN DE PASAJEROS ===")
            print("1. Registrar pasajero")
            print("2. Listar pasajeros")
            print("3. Buscar pasajero por documento")
            print("0. Volver al menú principal")
            opcion = input("Seleccione una opción: ")
            
            if opcion == "0":
                break
            elif opcion == "1":
                id_persona = input("ID de persona: ")
                nombre = input("Nombre: ")
                documento = input("Documento: ")
                email = input("Email: ")
                telefono = input("Teléfono: ")
                codigo_pasajero = input("Código de pasajero: ")
                pasajero = self.gestor_pasajeros.registrar_pasajero(id_persona, nombre, documento, email, telefono, codigo_pasajero)
                if pasajero:
                    print(f"Pasajero {pasajero.nombre} registrado correctamente.")
            elif opcion == "2":
                pasajeros = self.gestor_pasajeros.listar_pasajeros()
                if pasajeros:
                    print("\nLista de pasajeros:")
                    for pasajero in pasajeros:
                        print(f"ID: {pasajero.id_persona}, Nombre: {pasajero.nombre}, "
                              f"Documento: {pasajero.documento}, Código: {pasajero.codigo_pasajero}")
                else:
                    print("No hay pasajeros registrados.")
            elif opcion == "3":
                documento = input("Ingrese el documento: ")
                pasajero = self.gestor_pasajeros.buscar_por_documento(documento)
                if pasajero:
                    print(f"Pasajero encontrado: {pasajero.nombre} - {pasajero.documento}")
                else:
                    print("Pasajero no encontrado.")
            else:
                print("Opción inválida.")
    
    def _menu_gestion_vuelos(self):
        while True:
            print("\n=== GESTIÓN DE VUELOS ===")
            print("1. Programar vuelo")
            print("2. Listar vuelos")
            print("3. Asignar pasajero a vuelo")
            print("0. Volver al menú principal")
            opcion = input("Seleccione una opción: ")
            
            if opcion == "0":
                break
            elif opcion == "1":
                id_vuelo = input("ID del vuelo: ")
                codigo = input("Código del vuelo: ")
                origen = input("Origen: ")
                destino = input("Destino: ")
                print("Fecha y hora de salida (formato: YYYY-MM-DD HH:MM):")
                salida_str = input("Salida: ")
                print("Fecha y hora de llegada (formato: YYYY-MM-DD HH:MM):")
                llegada_str = input("Llegada: ")
                try:
                    salida = datetime.datetime.strptime(salida_str, "%Y-%m-%d %H:%M")
                    llegada = datetime.datetime.strptime(llegada_str, "%Y-%m-%d %H:%M")
                    horario = Horario(salida, llegada)
                    id_avion = input("ID del avión: ")
                    vuelo = self.gestor_vuelos.programar_vuelo(id_vuelo, codigo, origen, destino, horario, id_avion)
                    if vuelo:
                        print(f"Vuelo {vuelo.codigo} programado correctamente.")
                    else:
                        print("Error: No se pudo programar el vuelo. Verifique que el avión exista.")
                except ValueError:
                    print("Error: Formato de fecha inválido. Use YYYY-MM-DD HH:MM")
            elif opcion == "2":
                vuelos = self.gestor_vuelos.listar_vuelos()
                if vuelos:
                    print("\nLista de vuelos:")
                    for vuelo in vuelos:
                        print(f"ID: {vuelo.id_vuelo}, Código: {vuelo.codigo}, "
                              f"Origen: {vuelo.origen}, Destino: {vuelo.destino}, "
                              f"Pasajeros: {vuelo.cantidad_pasajeros()}")
                else:
                    print("No hay vuelos programados.")
            elif opcion == "3":
                id_vuelo = input("ID del vuelo: ")
                id_pasajero = input("ID del pasajero: ")
                vuelo = self.gestor_vuelos.asignar_pasajero_a_vuelo(id_vuelo, id_pasajero)
                if vuelo:
                    print(f"Pasajero asignado al vuelo {vuelo.codigo} correctamente.")
                else:
                    print("Error: No se pudo asignar el pasajero. Verifique que el vuelo y el pasajero existan.")
            else:
                print("Opción inválida.")
    
    def _menu_gestion_equipaje(self):
        while True:
            print("\n=== GESTIÓN DE EQUIPAJE ===")
            print("1. Registrar equipaje para un pasajero")
            print("2. Listar equipaje por pasajero")
            print("3. Consultar peso total de equipaje de un pasajero")
            print("0. Volver al menú principal")
            opcion = input("Seleccione una opción: ")
            
            if opcion == "0":
                break
            elif opcion == "1":
                codigo_unico = input("Código único del equipaje: ")
                peso = float(input("Peso (kg): "))
                id_pasajero = input("ID del pasajero: ")
                descripcion = input("Descripción (opcional, presione Enter para omitir): ")
                if descripcion == "":
                    descripcion = None
                equipaje = self.gestor_equipaje.registrar_equipaje(codigo_unico, peso, id_pasajero, descripcion)
                if equipaje:
                    print(f"Equipaje {equipaje.codigo_unico} registrado correctamente.")
                else:
                    print("Error: No se pudo registrar el equipaje.")
            elif opcion == "2":
                id_pasajero = input("ID del pasajero: ")
                equipajes = self.gestor_equipaje.listar_equipaje_por_pasajero(id_pasajero)
                if equipajes:
                    print(f"\nEquipaje del pasajero {id_pasajero}:")
                    for equipaje in equipajes:
                        print(f"Código: {equipaje.codigo_unico}, Peso: {equipaje.peso} kg, "
                              f"Descripción: {equipaje.descripcion or 'N/A'}")
                else:
                    print("No se encontró equipaje para este pasajero.")
            elif opcion == "3":
                id_pasajero = input("ID del pasajero: ")
                peso_total = self.gestor_equipaje.peso_total_por_pasajero(id_pasajero)
                print(f"Peso total del equipaje: {peso_total} kg")
            else:
                print("Opción inválida.")
    
    def _menu_reportes(self):
        while True:
            print("\n=== REPORTES ===")
            print("1. Reporte de vuelos con pasajeros y carga")
            print("2. Reporte de peso de equipaje por vuelo")
            print("0. Volver al menú principal")
            opcion = input("Seleccione una opción: ")
            
            if opcion == "0":
                break
            elif opcion == "1":
                reporte = self.gestor_reportes.reporte_vuelos_con_pasajeros_y_carga()
                if reporte:
                    print("\n=== REPORTE DE VUELOS ===")
                    for item in reporte:
                        print(f"Vuelo: {item['codigo']} ({item['id_vuelo']})")
                        print(f"  Ruta: {item['origen']} -> {item['destino']}")
                        print(f"  Pasajeros: {item['cantidad_pasajeros']}")
                        print(f"  Peso total equipaje: {item['peso_total_equipaje']} kg")
                        print()
                else:
                    print("No hay vuelos para mostrar.")
            elif opcion == "2":
                reporte = self.gestor_reportes.reporte_peso_equipaje_por_vuelo()
                if reporte:
                    print("\n=== REPORTE DE PESO DE EQUIPAJE POR VUELO ===")
                    for item in reporte:
                        print(f"Vuelo {item['codigo']}: {item['peso_total_equipaje']} kg")
                else:
                    print("No hay vuelos para mostrar.")
            else:
                print("Opción inválida.")
