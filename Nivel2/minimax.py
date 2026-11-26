
# ==========================================
# NIVEL 2 - BUSQUEDA ADVERSARIAL
# MINIMAX CON PODA ALFA-BETA
# ==========================================

from movimientos import crear_estado, estado_terminal, sucesores
from heuristica import evaluar_estado


# ==========================================
# CONFIGURACION
# ==========================================

PROFUNDIDAD_MAXIMA = 4

nodos_explorados = 0
podas_realizadas = 0
hojas_evaluadas = 0
profundidad_alcanzada = 0


def reiniciar_contadores():

    global nodos_explorados
    global podas_realizadas
    global hojas_evaluadas
    global profundidad_alcanzada

    nodos_explorados = 0
    podas_realizadas = 0
    hojas_evaluadas = 0
    profundidad_alcanzada = 0


def actualizar_profundidad(nivel):

    global profundidad_alcanzada

    profundidad_alcanzada = max(
        profundidad_alcanzada, nivel
    )


def obtener_estadisticas():

    return {
        "nodos": nodos_explorados,
        "podas": podas_realizadas,
        "hojas": hojas_evaluadas,
        "profundidad": profundidad_alcanzada
    }


# ==========================================
# EVALUACION DE HOJAS
# ==========================================

def evaluar_hoja(estado):

    global hojas_evaluadas

    hojas_evaluadas += 1

    return evaluar_estado(estado)


# ==========================================
# MAX - AGENTE PERSEGUIDOR
# ==========================================

def max_valor_ab(estado, profundidad, alfa, beta, nivel=1):

    global nodos_explorados
    global podas_realizadas

    nodos_explorados += 1
    actualizar_profundidad(nivel)

    if estado_terminal(estado) or profundidad == 0:
        return evaluar_hoja(estado)

    estados = sucesores(estado)

    if not estados:
        return evaluar_hoja(estado)

    valor = float("-inf")

    for siguiente in estados:

        valor = max(
            valor,
            min_valor_ab(
                siguiente,
                profundidad - 1,
                alfa,
                beta,
                nivel + 1
            )
        )

        alfa = max(alfa, valor)

        # Poda beta
        if alfa >= beta:
            podas_realizadas += 1
            break

    return valor


# ==========================================
# MIN - JUGADOR HUMANO
# ==========================================

def min_valor_ab(estado, profundidad, alfa, beta, nivel=1):

    global nodos_explorados
    global podas_realizadas

    nodos_explorados += 1
    actualizar_profundidad(nivel)

    if estado_terminal(estado) or profundidad == 0:
        return evaluar_hoja(estado)

    estados = sucesores(estado)

    if not estados:
        return evaluar_hoja(estado)

    valor = float("inf")

    for siguiente in estados:

        valor = min(
            valor,
            max_valor_ab(
                siguiente,
                profundidad - 1,
                alfa,
                beta,
                nivel + 1
            )
        )

        beta = min(beta, valor)

        # Poda alfa
        if alfa >= beta:
            podas_realizadas += 1
            break

    return valor


# ==========================================
# DECISION DE MAX CON ALFA-BETA
# ==========================================

def decision_alfa_beta(estado):

    global nodos_explorados

    reiniciar_contadores()

    # Contamos el estado inicial como nodo raiz
    nodos_explorados += 1

    mejor_estado = None
    mejor_valor = float("-inf")

    alfa = float("-inf")
    beta = float("inf")

    estados = sucesores(estado)

    for siguiente in estados:

        valor = min_valor_ab(
            siguiente,
            PROFUNDIDAD_MAXIMA - 1,
            alfa,
            beta,
            1
        )

        if valor > mejor_valor:

            mejor_valor = valor
            mejor_estado = siguiente

        alfa = max(alfa, mejor_valor)

    return mejor_estado, mejor_valor, nodos_explorados


# ==========================================
# MINIMAX SIN PODA
# PARA COMPARAR RESULTADOS
# ==========================================

def minimax_sin_poda(estado, profundidad, es_max, nivel, datos):

    datos["nodos"] += 1
    datos["profundidad"] = max(
        datos["profundidad"], nivel
    )

    if estado_terminal(estado) or profundidad == 0:

        datos["hojas"] += 1
        return evaluar_estado(estado)

    estados = sucesores(estado)

    if not estados:

        datos["hojas"] += 1
        return evaluar_estado(estado)

    if es_max:

        valor = float("-inf")

        for siguiente in estados:

            valor = max(
                valor,
                minimax_sin_poda(
                    siguiente,
                    profundidad - 1,
                    False,
                    nivel + 1,
                    datos
                )
            )

        return valor

    else:

        valor = float("inf")

        for siguiente in estados:

            valor = min(
                valor,
                minimax_sin_poda(
                    siguiente,
                    profundidad - 1,
                    True,
                    nivel + 1,
                    datos
                )
            )

        return valor


def decision_sin_poda(estado):

    datos = {
        "nodos": 1,
        "hojas": 0,
        "profundidad": 0
    }

    mejor_estado = None
    mejor_valor = float("-inf")

    for siguiente in sucesores(estado):

        valor = minimax_sin_poda(
            siguiente,
            PROFUNDIDAD_MAXIMA - 1,
            False,
            1,
            datos
        )

        if valor > mejor_valor:

            mejor_valor = valor
            mejor_estado = siguiente

    return mejor_estado, mejor_valor, datos


# ==========================================
# COMPARACION DE ALGORITMOS
# ==========================================

def comparar_algoritmos(estado):

    print("\n========== COMPARACION ==========")

    estado_minimax, valor_minimax, datos = (
        decision_sin_poda(estado)
    )

    estado_ab, valor_ab, nodos_ab = (
        decision_alfa_beta(estado)
    )

    estadisticas = obtener_estadisticas()

    print("\nMINIMAX SIN PODA")
    print("Mejor movimiento:", estado_minimax)
    print("Valor:", valor_minimax)
    print("Nodos explorados:", datos["nodos"])

    print("\nMINIMAX CON PODA ALFA-BETA")
    print("Mejor movimiento:", estado_ab)
    print("Valor:", valor_ab)
    print("Nodos explorados:", estadisticas["nodos"])
    print("Podas realizadas:", estadisticas["podas"])
    print("Hojas evaluadas:", estadisticas["hojas"])
    print("Profundidad alcanzada:",
          estadisticas["profundidad"])

    print("\nRESULTADO DE LA COMPARACION")

    if valor_minimax == valor_ab:

        print("CORRECTO: ambos algoritmos obtienen")
        print("el mismo valor optimo.")

    else:

        print("ERROR: los valores son diferentes.")

    return valor_minimax == valor_ab


# ==========================================
# PRUEBA DEL ALGORITMO
# ==========================================

if __name__ == "__main__":

    estado_inicial = crear_estado()

    print("================================")
    print(" NIVEL 2 - MINIMAX ALFA-BETA")
    print("================================")

    print("\nEstado inicial:")
    print(estado_inicial)

    mejor_estado, valor, nodos = decision_alfa_beta(
        estado_inicial
    )

    print("\nMEJOR DECISION DEL AGENTE MAX")

    print("Nuevo estado:", mejor_estado)
    print("Valor de evaluacion:", valor)

    estadisticas = obtener_estadisticas()

    print("\nESTADISTICAS DE BUSQUEDA")
    print("Nodos explorados:", estadisticas["nodos"])
    print("Podas realizadas:", estadisticas["podas"])
    print("Hojas evaluadas:", estadisticas["hojas"])
    print("Profundidad alcanzada:",
          estadisticas["profundidad"])

    comparar_algoritmos(estado_inicial)

    print("\n================================")
