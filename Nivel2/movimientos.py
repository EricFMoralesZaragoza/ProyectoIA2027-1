
# ==========================================
# NIVEL 2 - MINIMAX CON PODA ALFA-BETA
# Generacion de estados sucesores
# ==========================================

from laberinto import (
    JUGADOR,
    AGENTE,
    SALIDA,
    movimientos_validos
)


# Representacion de un estado:
# jugador, agente y turno correspondiente

def crear_estado(jugador=JUGADOR, agente=AGENTE, turno="MAX"):

    return {
        "jugador": jugador,
        "agente": agente,
        "turno": turno
    }


# ==========================================
# COMPROBAR ESTADOS TERMINALES
# ==========================================

def estado_terminal(estado):

    jugador = estado["jugador"]
    agente = estado["agente"]

    # El agente captura al jugador
    if jugador == agente:
        return True

    # El jugador llega a la salida
    if jugador == SALIDA:
        return True

    return False


# ==========================================
# GENERAR ESTADOS SUCESORES
# ==========================================

def sucesores(estado):

    nuevos_estados = []

    jugador = estado["jugador"]
    agente = estado["agente"]
    turno = estado["turno"]

    # Turno del agente MAX
    if turno == "MAX":

        opciones = movimientos_validos(agente)

        for movimiento in opciones:

            nuevo_estado = crear_estado(
                jugador,
                movimiento,
                "MIN"
            )

            nuevos_estados.append(nuevo_estado)

    # Turno del jugador MIN
    else:

        opciones = movimientos_validos(jugador)

        for movimiento in opciones:

            nuevo_estado = crear_estado(
                movimiento,
                agente,
                "MAX"
            )

            nuevos_estados.append(nuevo_estado)

    return nuevos_estados


# ==========================================
# PRUEBAS
# ==========================================

if __name__ == "__main__":

    estado_inicial = crear_estado()

    print("ESTADO INICIAL")
    print(estado_inicial)

    print("\nESTADOS SUCESORES DEL AGENTE MAX:")

    estados = sucesores(estado_inicial)

    for i, estado in enumerate(estados, 1):

        print(f"\nOpcion {i}:")
        print(estado)

    print("\n¿Es terminal el estado inicial?")
    print(estado_terminal(estado_inicial))
