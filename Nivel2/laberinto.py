
# ==========================================
# NIVEL 2 - MINIMAX CON PODA ALFA-BETA
# Representacion del laberinto
# ==========================================

# Escenario proporcionado por el profesor
LABERINTO = [
    "......G..E",
    ".##...#...",
    "...#..#...",
    ".#.#......",
    ".#...##...",
    "...#......",
    "##.#.###..",
    "...#......",
    ".##..#..#.",
    "P....#...."
]

# Posiciones iniciales (x, y)
JUGADOR = (1, 1)
AGENTE = (7, 10)
SALIDA = (10, 10)

# Dimensiones del laberinto
FILAS = 10
COLUMNAS = 10


def mostrar_laberinto():
    """Muestra el laberinto en la terminal."""
    print("\n===== NIVEL 2 =====\n")

    for fila in LABERINTO:
        print(" ".join(fila))

    print("\n===================\n")


def obtener_celda(posicion):
    """Obtiene el contenido de una celda usando coordenadas."""
    x, y = posicion

    fila = FILAS - y
    columna = x - 1

    return LABERINTO[fila][columna]


def es_posicion_valida(posicion):
    """Comprueba que una posicion este dentro del laberinto."""
    x, y = posicion

    if x < 1 or x > COLUMNAS:
        return False

    if y < 1 or y > FILAS:
        return False

    return obtener_celda(posicion) != "#"


def movimientos_validos(posicion):
    """Devuelve los movimientos permitidos desde una posicion."""

    x, y = posicion

    posibles = [
        (x, y + 1),  # Arriba
        (x, y - 1),  # Abajo
        (x - 1, y),  # Izquierda
        (x + 1, y)   # Derecha
    ]

    return [
        movimiento
        for movimiento in posibles
        if es_posicion_valida(movimiento)
    ]


# ==========================================
# PRUEBAS
# ==========================================

if __name__ == "__main__":

    mostrar_laberinto()

    print("Posicion del jugador:", JUGADOR)
    print("Posicion del agente:", AGENTE)
    print("Posicion de la salida:", SALIDA)

    print("\nMovimientos validos del agente:")
    print(movimientos_validos(AGENTE))

    print("\nMovimientos validos del jugador:")
    print(movimientos_validos(JUGADOR))
