"""
Versión consolidada del proyecto FBO On Earth en un solo archivo.
Este archivo contiene toda la lógica del proyecto sin modificaciones.
"""

import datetime


# ============================================================================
# DOMINIO - Clases de Entidad
# ============================================================================

class Persona:
    def __init__(self, id_persona, nombre, documento, email, telefono):
        self.id_persona = id_persona
        self.nombre = nombre
        self.documento = documento
        self.email = email
        self.telefono = telefono


class Avion:
    def __init__(self, id_avion, modelo, matricula, msn, capacidad_pasajeros, peso_max_equipaje):
        self.id_avion = id_avion
        self.modelo = modelo
        self.matricula = matricula
        self.msn = msn
        self.capacidad_pasajeros = capacidad_pasajeros
        self.peso_max_equipaje = peso_max_equipaje
    
    def tiene_capacidad(self, cantidad_pasajeros, peso_equipaje_total):
        if cantidad_pasajeros <= self.capacidad_pasajeros and peso_equipaje_total <= self.peso_max_equipaje:
            return True
        return False


class Horario:
    def __init__(self, salida, llegada):
        self.salida = salida
        self.llegada = llegada
    
    def duracion_minutos(self):
        diferencia = self.llegada - self.salida
        return int(diferencia.total_seconds() / 60)


class Equipaje:
    def __init__(self, codigo_unico, peso, id_pasajero, descripcion=None):
        self.codigo_unico = codigo_unico
        self.peso = peso
        self.id_pasajero = id_pasajero
        self.descripcion = descripcion


class Pasajero(Persona):
    def __init__(self, id_persona, nombre, documento, email, telefono, codigo_pasajero):
        super().__init__(id_persona, nombre, documento, email, telefono)
        self.codigo_pasajero = codigo_pasajero
        self.equipajes = []
    
    def agregar_equipaje(self, equipaje):
        if equipaje not in self.equipajes:
            self.equipajes.append(equipaje)
    
    def peso_total_equipaje(self):
        total = 0.0
        for equipaje in self.equipajes:
            total += equipaje.peso
        return total


class Tripulante(Persona):
    def __init__(self, id_persona, nombre, documento, email, telefono, rol_tripulacion, licencia):
        super().__init__(id_persona, nombre, documento, email, telefono)
        self.rol_tripulacion = rol_tripulacion
        self.licencia = licencia


class Usuario(Persona):
    def __init__(self, id_persona, nombre, documento, email, telefono, nombre_usuario, password, rol):
        super().__init__(id_persona, nombre, documento, email, telefono)
        self.nombre_usuario = nombre_usuario
        self.password = password
        self.rol = rol


class Vuelo:
    def __init__(self, id_vuelo, codigo, origen, destino, horario, avion):
        self.id_vuelo = id_vuelo
        self.codigo = codigo
        self.origen = origen
        self.destino = destino
        self.horario = horario
        self.avion = avion
        self.tripulacion = []
        self.pasajeros = []
    
    def agregar_pasajero(self, pasajero):
        if pasajero not in self.pasajeros:
            self.pasajeros.append(pasajero)
    
    def eliminar_pasajero(self, pasajero):
        if pasajero in self.pasajeros:
            self.pasajeros.remove(pasajero)
    
    def agregar_tripulante(self, tripulante):
        if tripulante not in self.tripulacion:
            self.tripulacion.append(tripulante)
    
    def cantidad_pasajeros(self):
        return len(self.pasajeros)
    
    def peso_total_equipaje(self):
        total = 0.0
        for pasajero in self.pasajeros:
            total += pasajero.peso_total_equipaje()
        return total
    
    def tiene_capacidad_disponible(self):
        cantidad = self.cantidad_pasajeros()
        peso = self.peso_total_equipaje()
        return self.avion.tiene_capacidad(cantidad, peso)


# ============================================================================
# REPOSITORIOS
# ============================================================================

class BaseRepositorio:
    def agregar(self, entidad):
        raise NotImplementedError()
    
    def obtener_por_id(self, id_entidad):
        raise NotImplementedError()
    
    def listar_todos(self):
        raise NotImplementedError()
    
    def eliminar(self, id_entidad):
        raise NotImplementedError()


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


# ============================================================================
# SERVICIOS - Gestores
# ============================================================================

class GestorAviones:
    def __init__(self, avion_repositorio):
        self.avion_repositorio = avion_repositorio
    
    def registrar_avion(self, id_avion, modelo, matricula, msn, capacidad_pasajeros, peso_max_equipaje):
        avion = Avion(id_avion, modelo, matricula, msn, capacidad_pasajeros, peso_max_equipaje)
        self.avion_repositorio.agregar(avion)
        return avion
    
    def obtener_avion(self, id_avion):
        return self.avion_repositorio.obtener_por_id(id_avion)
    
    def listar_aviones(self):
        return self.avion_repositorio.listar_todos()
    
    def buscar_por_matricula(self, matricula):
        return self.avion_repositorio.buscar_por_matricula(matricula)
    
    def buscar_por_msn(self, msn):
        return self.avion_repositorio.buscar_por_msn(msn)


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


class GestorVuelos:
    def __init__(self, vuelo_repositorio, avion_repositorio, pasajero_repositorio):
        self.vuelo_repositorio = vuelo_repositorio
        self.avion_repositorio = avion_repositorio
        self.pasajero_repositorio = pasajero_repositorio
    
    def programar_vuelo(self, id_vuelo, codigo, origen, destino, horario, id_avion):
        avion = self.avion_repositorio.obtener_por_id(id_avion)
        if avion is None:
            return None
        vuelo = Vuelo(id_vuelo, codigo, origen, destino, horario, avion)
        self.vuelo_repositorio.agregar(vuelo)
        return vuelo
    
    def obtener_vuelo(self, id_vuelo):
        return self.vuelo_repositorio.obtener_por_id(id_vuelo)
    
    def listar_vuelos(self):
        return self.vuelo_repositorio.listar_todos()
    
    def asignar_pasajero_a_vuelo(self, id_vuelo, id_pasajero):
        vuelo = self.vuelo_repositorio.obtener_por_id(id_vuelo)
        if vuelo is None:
            return None
        pasajero = self.pasajero_repositorio.obtener_por_id(id_pasajero)
        if pasajero is None:
            return None
        vuelo.agregar_pasajero(pasajero)
        return vuelo
    
    def eliminar_pasajero_de_vuelo(self, id_vuelo, id_pasajero):
        vuelo = self.vuelo_repositorio.obtener_por_id(id_vuelo)
        if vuelo is None:
            return None
        pasajero = self.pasajero_repositorio.obtener_por_id(id_pasajero)
        if pasajero is None:
            return None
        vuelo.eliminar_pasajero(pasajero)
        return vuelo
    
    def cantidad_pasajeros_vuelo(self, id_vuelo):
        vuelo = self.vuelo_repositorio.obtener_por_id(id_vuelo)
        if vuelo is None:
            return 0
        return vuelo.cantidad_pasajeros()
    
    def peso_total_equipaje_vuelo(self, id_vuelo):
        vuelo = self.vuelo_repositorio.obtener_por_id(id_vuelo)
        if vuelo is None:
            return 0.0
        return vuelo.peso_total_equipaje()
    
    def tiene_capacidad_disponible(self, id_vuelo):
        vuelo = self.vuelo_repositorio.obtener_por_id(id_vuelo)
        if vuelo is None:
            return False
        return vuelo.tiene_capacidad_disponible()


class GestorEquipaje:
    def __init__(self, equipaje_repositorio, pasajero_repositorio, vuelo_repositorio):
        self.equipaje_repositorio = equipaje_repositorio
        self.pasajero_repositorio = pasajero_repositorio
        self.vuelo_repositorio = vuelo_repositorio
    
    def registrar_equipaje(self, codigo_unico, peso, id_pasajero, descripcion=None):
        equipaje = Equipaje(codigo_unico, peso, id_pasajero, descripcion)
        self.equipaje_repositorio.agregar(equipaje)
        pasajero = self.pasajero_repositorio.obtener_por_id(id_pasajero)
        if pasajero is not None:
            pasajero.agregar_equipaje(equipaje)
        return equipaje
    
    def listar_equipaje_por_pasajero(self, id_pasajero):
        return self.equipaje_repositorio.listar_por_pasajero(id_pasajero)
    
    def peso_total_por_pasajero(self, id_pasajero):
        pasajero = self.pasajero_repositorio.obtener_por_id(id_pasajero)
        if pasajero is not None:
            return pasajero.peso_total_equipaje()
        return 0.0
    
    def peso_total_por_vuelo(self, id_vuelo):
        vuelo = self.vuelo_repositorio.obtener_por_id(id_vuelo)
        if vuelo is not None:
            return vuelo.peso_total_equipaje()
        return 0.0
    
    def verificar_peso_maximo_vuelo(self, id_vuelo):
        vuelo = self.vuelo_repositorio.obtener_por_id(id_vuelo)
        if vuelo is None:
            return False
        avion = vuelo.avion
        peso_total = vuelo.peso_total_equipaje()
        if peso_total <= avion.peso_max_equipaje:
            return True
        return False
    
    def generar_alerta_sobrepeso(self, id_vuelo):
        if self.verificar_peso_maximo_vuelo(id_vuelo):
            return "El peso del equipaje está dentro del límite permitido."
        vuelo = self.vuelo_repositorio.obtener_por_id(id_vuelo)
        if vuelo is None:
            return None
        peso_total = vuelo.peso_total_equipaje()
        peso_max = vuelo.avion.peso_max_equipaje
        return f"ALERTA: El peso total del equipaje ({peso_total} kg) excede el límite máximo del avión ({peso_max} kg)."


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


# ============================================================================
# INTERFAZ
# ============================================================================

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


# ============================================================================
# MAIN
# ============================================================================

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

