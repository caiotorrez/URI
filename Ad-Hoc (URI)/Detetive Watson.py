def index(lista):
    assassin = 0
    for k in xrange(len(lista)):
        if lista[k] > assassin:
            assassin = lista[k]
            pos = k + 1
    return pos

def remove(lista):
    maior = max(lista)
    for i in xrange(len(lista)):
        if lista[i] == maior:
            lista[i] = -1
            return lista
        elif lista[-i-1] == maior:
            lista[-i-1] = -1
            return lista

while True:
    enfeite = raw_input()
    if enfeite == '0':
        break
    lista = map(int, raw_input().split())
    print index(remove(lista))
        
