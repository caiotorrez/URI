
def search(lista, string):
    cont = 0
    lenght = len(string)
    for i in xrange(len(lista)):
        for j in xrange(len(lista[0]) - (lenght - 1)):
            if lista[i][j:lenght+j] == string:
                cont += 1
    return cont

case = int(raw_input())
for i in xrange(case):
    l, c = map(int, raw_input().split())
    
    lista = [None]*l
    inv_lista = ['']*c
    for k in xrange(l):
        lista[k] = raw_input()
        for j in xrange(c):
            inv_lista[j] += lista[k][j]

    for i in xrange(int(raw_input())):
        string = raw_input()
        if len(string) == 1:
            print search(inv_lista, string)

        else:
            print search(inv_lista, string) + search(lista, string)
