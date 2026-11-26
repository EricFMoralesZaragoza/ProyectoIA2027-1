
# ==========================================
# PROYECTO: ESCAPE DEL LABERINTO
# NIVEL 2 - MINIMAX CON PODA ALFA-BETA
# ==========================================

from laberinto import LABERINTO, FILAS, COLUMNAS
from movimientos import crear_estado, estado_terminal, sucesores
from minimax import decision_alfa_beta


# ==========================================
# MOSTRAR LABERINTO
# ==========================================

def mostrar_tablero(estado):

    jugador = estado["jugador"]
    agente = estado["agente"]

    print("\n========== NIVEL 2: LABERINTO ==========\n")

    for fila in range(FILAS, 0, -1):

        linea = ""

        for columna in range(1, COLUMNAS + 1):

            posicion = (columna, fila)

            if posicion == jugador and posicion == agente:
                simbolo = "X"

            elif posicion == jugador:
                simbolo = "P"

            elif posicion == agente:
                simbolo = "G"

            else:
                simbolo = LABERINTO[FILAS - fila][columna - 1]

            linea += simbolo + " "

        print(linea)

    print("\nP = Jugador")
    print("G = Agente perseguidor")
    print("E = Salida")
    print("# = Pared")
    print("X = Captura")


# ==========================================
# TURNO DEL JUGADOR HUMANO (MIN)
# ==========================================

def turno_jugador(estado):

    opciones = sucesores(estado)

    if not opciones:

        print("El jugador no tiene movimientos disponibles.")
        return None

    print("\n--- TURNO DEL JUGADOR (MIN) ---")

    for i, siguiente in enumerate(opciones, 1):

        print(f"{i}. Moverse a {siguiente['jugador']}")

    while True:

        try:

            opcion = int(input("\nSelecciona tu movimiento: "))

            if 1 <= opcion <= len(opciones):

                return opciones[opcion - 1]

            print("Selecciona una opcion valida.")

        except ValueError:

            print("Debes introducir un numero.")


# ==========================================
# TURNO DEL AGENTE (MAX)
# ==========================================

def turno_agente(estado):

    print("\n--- TURNO DEL AGENTE (MAX) ---")
    print("El agente esta calculando su movimiento...")

    mejor_estado, valor, nodos = decision_alfa_beta(estado)

    if mejor_estado is None:

        print("El agente no tiene movimientos disponibles.")
        return None

    print("\nMovimiento seleccionado:", mejor_estado["agente"])
    print("Valor de evaluacion:", valor)
    print("Nodos explorados:", nodos)

    return mejor_estado


# ==========================================
# RESULTADO FINAL
# ==========================================

def mostrar_resultado(estado):

    jugador = estado["jugador"]
    agente = estado["agente"]

    if jugador == agente:

        print("\n¡EL AGENTE HA CAPTURADO AL JUGADOR!")

    elif jugador == (10, 10):

        print("\n¡EL JUGADOR HA LLEGADO A LA SALIDA!")

    else:

        print("\nEl juego ha terminado.")


# ==========================================
# INICIAR NIVEL 2
# ==========================================

def iniciar_nivel2():

    estado = crear_estado()

    # El jugador humano siempre comienza
    estado["turno"] = "MIN"

    print("\n====================================")
    print("       ESCAPE DEL LABERINTO")
    print("             NIVEL 2")
    print("       MINIMAX ALFA-BETA")
    print("====================================")

    print("\nObjetivo: llegar a la salida sin ser capturado.")

    print("\nEl jugador humano realiza el primer movimiento.")

    while not estado_terminal(estado):

        mostrar_tablero(estado)

        # Turno del jugador humano
        if estado["turno"] == "MIN":

            nuevo_estado = turno_jugador(estado)

            if nuevo_estado is None:
                print("El jugador no puede continuar.")
                break

            estado = nuevo_estado

        # Turno del agente perseguidor
        elif estado["turno"] == "MAX":

            nuevo_estado = turno_agente(estado)

            if nuevo_estado is None:
                print("El agente no puede continuar.")
                break

            estado = nuevo_estado

    mostrar_tablero(estado)
    mostrar_resultado(estado)


# ==========================================
# EJECUCION
# ==========================================

if __name__ == "__main__":

    iniciar_nivel2()
