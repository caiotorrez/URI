def contagem(primos):
    cont = [0]
    for i in xrange(1, 10**6 + 1):
        if primos[i] and primos[i+2] or primos[i] and primos[i-2]:
            cont.append(1+(cont[i-1]))
        else:
            cont.append(cont[i-1])
                    
    return cont

def crivo():   
    n = 10**6 + 1
    primos = [True] * (n + 1)
    primos[0] = False
    primos[1] = False
    for i in xrange(2, n + 1):
            if primos[i]:
                    for j in xrange(i+i, n + 1, i):
                            primos[j] = False
    return primos

lista = crivo()
entrada = int(raw_input())
cont = contagem(lista)
for k in xrange(entrada):
    
    x, y = raw_input().split()
    x = int(x)
    y = int(y)

    if x > 2 and x == y and lista[x] and lista[x+2] or x > 2 and x == y and lista[x] and lista[x-2]:
        print '1'
    elif x > y:
        print cont[x] - cont[y-1]
    else:
        print cont[y] - cont[x-1]
