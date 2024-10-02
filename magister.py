J = { 'a' :['b', 'c', 'd'],
      'b': ['e', 'f'],
      'c': ['g', 'h'],
      'd': ['i', 'j'],
      'e': ['k', 'l'],
      'f': ['m', 'n'],
      'g': ['o', 'p'],
      'h': ['q', 'r'],
      'i': ['s', 't'],
      'j': ['u', 'v'],
      'k':[],
      'l':[],
      'm':[],
      'n':[],
      'o':[],
      'p':[],
      'q':[],
      'r':[],
      's':[],
      't':[],
      'u':[],
      'v':[]
      }

utilidades = {'k':-1, 'l':3, 'm':5, 'n':1, 'o':6, 'p':4, 'q':2, 'r':10, 's':3, 't':1, 'u':18, 'v':9}
    
def get_utilidad(e):
    utilidades[e]

def es_terminal(e):
    J[e]==[]

def get_sucesor(e):
    return J[e]

def valor_max(estado):
    v = -100
    for h in get_sucesor(estado):
        v = max(v, minimax(h, 'min'))
    return v

def valor_min(estado):
    v = 100
    for h in get_sucesor(estado):
        v = min(v, minimax(h, "max"))
    return v

def minimax(estado, jugador):
    if es_terminal(estado):
        return get_utilidad(estado)
    if jugador == 'max':
        valor_max(estado)
    else:
        valor_min(estado)
        
        
if __name__ == "__main__":
    print(minimax('a','min'))