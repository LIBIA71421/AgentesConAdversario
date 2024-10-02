from Tablero import es_terminal, utilidad, sucesores

def valor_max(estado):
    v = float('-inf')
    for h in sucesores(estado):
        v = max(v, minimax(h, 'min'))
    return v

def valor_min(estado):
    v = float('inf')
    for h in sucesores(estado):
        v = min(v, minimax(h, 'max'))
    return v

def minimax(estado, jugador):
    if es_terminal(estado):
        return utilidad(estado)
    if jugador == 'max':
        return valor_max(estado)
    else: 
        return valor_min(estado)


'''from Tablero import es_terminal, utilidad, sucesores

def minimax_alpha_beta(tablero, profundidad, alpha, beta, jugador):
    if es_terminal(tablero):
        return utilidad(tablero)
    
    if jugador == 'X':
        valor_max = float('-inf')
        for hijo in sucesores(tablero):
            valor_max = max(valor_max, minimax_alpha_beta(hijo, profundidad + 1, alpha, beta, 'O'))
            alpha = max(alpha, valor_max)
            if beta <= alpha:
                break  # Poda
        return valor_max
    else:  # jugador == 'O'
        valor_min = float('inf')
        for hijo in sucesores(tablero):
            valor_min = min(valor_min, minimax_alpha_beta(hijo, profundidad + 1, alpha, beta, 'X'))
            beta = min(beta, valor_min)
            if beta <= alpha:
                break  # Poda
        return valor_min
'''