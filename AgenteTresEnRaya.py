from Tablero import es_terminal, utilidad

class AgenteTresEnRaya:
    def __init__(self):
        self.resultados = []

    def supervisar_partida(self, tablero):
        resultado = utilidad(tablero)
        if resultado == 1:
            self.resultados.append("X gana")
            print("Resultado: X gana")
        elif resultado == -1:
            self.resultados.append("O gana")
            print("Resultado: O gana")
        elif all(c != ' ' for fila in tablero for c in fila):
            self.resultados.append("Empate")
            print("Resultado: Empate")

    def mostrar_resultados(self):
        print("Resultados de las partidas:")
        for resultado in self.resultados:
            print(resultado)