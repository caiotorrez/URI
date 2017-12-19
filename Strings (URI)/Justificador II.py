import sys

n = int(raw_input())
while n != 0:

    lista = ['']*n
    total = 0
    for i in xrange(int(n)):
        frase = raw_input().strip()
        for j in xrange(len(frase)):
            if frase[j] == ' ' and frase[j-1] != ' ':
                lista[i] += ' '
            elif frase[j] != ' ':
                lista[i] += frase[j]
        if len(lista[i]) > total:
            total = len(lista[i])
    for i in xrange(len(lista)):
        
        sys.stdout.write(' ' * (total - len(lista[i])) + lista[i] + '\n')

    n = int(raw_input())
    if n != 0:
        sys.stdout.write('\n')
