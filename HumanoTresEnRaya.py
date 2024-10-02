class HumanoTresEnRaya:
    def __init__(self, simbolo):
        self.simbolo = simbolo

    def hacer_movimiento(self, tablero):
        while True:
            try:
                movimiento = input(f"Jugador {self.simbolo}, ingresa tu movimiento (fila, columna): ")
                fila, columna = map(int, movimiento.split(','))
                if tablero[fila][columna] == ' ':
                    tablero[fila][columna] = self.simbolo
                    break
                else:
                    print("Esa posición ya está ocupada. Intenta de nuevo.")
            except (ValueError, IndexError):
                print("Movimiento inválido. Asegúrate de ingresar fila y columna como números entre 0 y 2.")
