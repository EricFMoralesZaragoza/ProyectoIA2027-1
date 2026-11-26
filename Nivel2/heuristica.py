
# ==========================================
# NIVEL 2 - MINIMAX CON PODA ALFA-BETA
# Funcion heuristica
# ==========================================

from collections import deque

from laberinto import SALIDA, es_posicion_valida, movimientos_validos


# ==========================================
# CALCULAR DISTANCIA REAL ENTRE DOS CELDAS
# ==========================================

def distancia_caminos(origen, destino):
    """
    Calcula la distancia minima entre dos posiciones,
    respetando las paredes del laberinto.
    """

    if origen == destino:
        return 0

    cola = deque([(origen, 0)])
    visitados = {origen}

    while cola:

        posicion, distancia = cola.popleft()

        for siguiente in movimientos_validos(posicion):

            if siguiente in visitados:
                continue

            if siguiente == destino:
                return distancia + 1

            visitados.add(siguiente)
            cola.append((siguiente, distancia + 1))

    return float("inf")


# ==========================================
# FUNCION HEURISTICA
# ==========================================

def evaluar_estado(estado):

    jugador = estado["jugador"]
    agente = estado["agente"]

    # El agente captura al jugador
    if jugador == agente:
        return 1000

    # El jugador alcanza la salida
    if jugador == SALIDA:
        return -1000

    # Distancia entre el agente y el jugador
    distancia_agente = distancia_caminos(
        agente, jugador
    )

    # Distancia entre el jugador y la salida
    distancia_salida = distancia_caminos(
        jugador, SALIDA
    )

    # MAX busca aumentar la puntuacion
    # MIN busca disminuir la puntuacion
    puntuacion = distancia_salida - distancia_agente

    return puntuacion


# ==========================================
# PRUEBAS
# ==========================================

if __name__ == "__main__":

    estado_inicial = {
        "jugador": (1, 1),
        "agente": (7, 10),
        "turno": "MAX"
    }

    print("EVALUACION DEL ESTADO INICIAL")

    print(
        "Distancia agente-jugador:",
        distancia_caminos((7, 10), (1, 1))
    )

    print(
        "Distancia jugador-salida:",
        distancia_caminos((1, 1), SALIDA)
    )

    print(
        "Valor heuristico:",
        evaluar_estado(estado_inicial)
    )
