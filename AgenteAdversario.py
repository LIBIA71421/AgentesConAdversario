from Agente import minimax

def jugar_agente(tablero):
    mejor_valor = float('-inf')
    mejor_movimiento = None

    for i in range(3):
        for j in range(3):
            if tablero[i][j] == ' ':
                tablero[i][j] = 'X' 
                valor = minimax(tablero, 'min')
                tablero[i][j] = ' '  
                if valor > mejor_valor:
                    mejor_valor = valor
                    mejor_movimiento = (i, j)

    if mejor_movimiento:
        tablero[mejor_movimiento[0]][mejor_movimiento[1]] = 'X'  


'''from Agente import minimax_alpha_beta

def jugar_agente(tablero):
    mejor_valor = float('-inf')
    mejor_movimiento = None

    for i in range(3):
        for j in range(3):
            if tablero[i][j] == ' ':
                tablero[i][j] = 'X' 
                valor = minimax_alpha_beta(tablero, 0, float('-inf'), float('inf'), 'O')
                tablero[i][j] = ' '  
                if valor > mejor_valor:
                    mejor_valor = valor
                    mejor_movimiento = (i, j)

    if mejor_movimiento:
        tablero[mejor_movimiento[0]][mejor_movimiento[1]] = 'X' 

'''
