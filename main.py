class JugadorDeFutbol:
    def __init__(self, nombre, equipo, posicion, numero_goles=0, premios=None):
        self.nombre = nombre
        self.equipo = equipo
        self.posicion = posicion
        self.numero_goles = numero_goles
        self.premios = premios if premios is not None else []

    def actualizar_informacion(self, nombre=None, equipo=None, posicion=None):
        if nombre:
            self.nombre = nombre
        if equipo:
            self.equipo = equipo
        if posicion:
            self.posicion = posicion
        self.actualizacion_estadisticas()

    def calcular_promedio_goles(self, partidos_jugados):
        return self.numero_goles / partidos_jugados if partidos_jugados > 0 else 0

    def es_goleador(self, minimo_goles):
        return self.numero_goles >= minimo_goles

    def agregar_premio(self, premio):
        self.premios.append(premio)
        self.actualizacion_estadisticas()

    def eliminar_premio(self, premio):
        if premio in self.premios:
            self.premios.remove(premio)
            self.actualizacion_estadisticas()

    def actualizacion_estadisticas(self):
        print("Estadísticas actualizadas.")

class MenuInteractivo:
    def __init__(self):
        self.jugadores = {}

    def crear_jugador(self):
        nombre = input("Ingrese el nombre del jugador: ")
        equipo = input("Ingrese el equipo del jugador: ")
        posicion = input("Ingrese la posición del jugador: ")
        jugador = JugadorDeFutbol(nombre, equipo, posicion)
        self.jugadores[nombre] = jugador
        print(f"Jugador {nombre} creado con éxito.")

    def mostrar_informacion(self, nombre):
        if nombre in self.jugadores:
            jugador = self.jugadores[nombre]
            print(f"Nombre: {jugador.nombre}")
            print(f"Equipo: {jugador.equipo}")
            print(f"Posición: {jugador.posicion}")
            print(f"Goles: {jugador.numero_goles}")
            print(f"Premios: {', '.join(jugador.premios)}")
        else:
            print("Jugador no encontrado.")



    def ejecutar(self):
        while True:
            print("\\nMenú de Jugador de Fútbol:")
            print("1. Crear un nuevo jugador de fútbol")
            print("2. Mostrar la información de un jugador existente")
            print("3. Actualizar la información de un jugador existente")
         
            print("9. Salir")
            opcion = input("Elige una opción: ")

            if opcion == '9':
                break
            elif opcion == '1':
                self.crear_jugador()
       

if __name__ == "__main__":
    menu = MenuInteractivo()
    menu.ejecutar()
