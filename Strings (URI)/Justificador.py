import sys

n = raw_input()
while n != '0':

    lista = []
    total = 0
    for i in xrange(int(n)):
        lista.append(raw_input())
        if len(lista[i]) > total:
            total = len(lista[i])
    for i in xrange(len(lista)):
        
        sys.stdout.write(' ' * (total - len(lista[i])) + lista[i] + '\n')

    n = raw_input()
    if n != '0':
        sys.stdout.write('\n')
