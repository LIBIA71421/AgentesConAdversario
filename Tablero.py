VACIO = ' '

def imprimir_tablero(tablero):
    for fila in tablero:
        print('|'.join(fila))
        print('-' * 5)

def es_terminal(tablero):
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] != VACIO:
            return True
        if tablero[0][i] == tablero[1][i] == tablero[2][i] != VACIO:
            return True
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != VACIO:
        return True
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != VACIO:
        return True
    return False

def utilidad(tablero):
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] == 'X':
            return 1  # X gana
        if tablero[i][0] == tablero[i][1] == tablero[i][2] == 'O':
            return -1  # O gana
    if tablero[0][0] == tablero[1][1] == tablero[2][2] == 'X':
        return 1
    if tablero[0][2] == tablero[1][1] == tablero[2][0] == 'X':
        return 1
    if tablero[0][0] == tablero[1][1] == tablero[2][2] == 'O':
        return -1
    if tablero[0][2] == tablero[1][1] == tablero[2][0] == 'O':
        return -1
    return 0  

def sucesores(tablero):
    sucesores = []
    for i in range(3):
        for j in range(3):
            if tablero[i][j] == VACIO:
                nuevo_tablero = [fila[:] for fila in tablero]  
                nuevo_tablero[i][j] = 'X' 
                sucesores.append(nuevo_tablero)
    return sucesores
