from Tablero import imprimir_tablero, es_terminal
from AgenteAdversario import jugar_agente
from AgenteTresEnRaya import AgenteTresEnRaya
from HumanoTresEnRaya import HumanoTresEnRaya

def main():
    agente_supervisor = AgenteTresEnRaya()
    jugador_humano = HumanoTresEnRaya('O')  
    
    tablero_inicial = [
        [' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ']
    ]

    imprimir_tablero(tablero_inicial)

    while True:
        jugador_humano.hacer_movimiento(tablero_inicial)
        imprimir_tablero(tablero_inicial)
        if es_terminal(tablero_inicial):
            agente_supervisor.supervisar_partida(tablero_inicial)
            break

        print("Turno del agente (X):")
        jugar_agente(tablero_inicial)
        imprimir_tablero(tablero_inicial)
        if es_terminal(tablero_inicial):
            agente_supervisor.supervisar_partida(tablero_inicial)
            break

    agente_supervisor.mostrar_resultados()

if __name__ == "__main__":
    main()
