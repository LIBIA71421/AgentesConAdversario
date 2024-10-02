from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from Tablero import imprimir_tablero, es_terminal
from AgenteAdversario import jugar_agente
from AgenteTresEnRaya import AgenteTresEnRaya
from HumanoTresEnRaya import HumanoTresEnRaya

app = Flask(__name__)
socketio = SocketIO(app)

tablero_inicial = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

agente_supervisor = AgenteTresEnRaya()
jugador_humano = HumanoTresEnRaya('O')  
turno = 'O'  

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('jugador_humano_move')
def handle_humano_move(data):
    print(f"Movimiento recibido: fila {data['fila']}, columna {data['columna']}")
# @socketio.on('jugador_humano_move')
# def handle_humano_move(data):
#    global tablero_inicial, turno

    if turno == 'O':
        fila = data['fila']
        columna = data['columna']
        
        if tablero_inicial[fila][columna] == ' ':
            jugador_humano.hacer_movimiento(tablero_inicial, fila, columna)
            imprimir_tablero(tablero_inicial)
            turno = 'X'

            if es_terminal(tablero_inicial):
                agente_supervisor.supervisar_partida(tablero_inicial)
                emit('game_over', {'winner': 'O'}, broadcast=True)
            else:
                jugar_agente(tablero_inicial)
                imprimir_tablero(tablero_inicial)
                turno = 'O'
                
                if es_terminal(tablero_inicial):
                    agente_supervisor.supervisar_partida(tablero_inicial)
                    emit('game_over', {'winner': 'X'}, broadcast=True)
                else:
                    emit('game_state', {'tablero': tablero_inicial}, broadcast=True)
        else:
            emit('invalid_move', {'message': 'Movimiento inválido'}, broadcast=False)

@socketio.on('reset_game')
def reset_game():
    global tablero_inicial, turno
    tablero_inicial = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]
    turno = 'O'  
    emit('game_state', {'tablero': tablero_inicial}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)