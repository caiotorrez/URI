import sys
lista = []

for i  in xrange(int(raw_input())):
    lista.append(raw_input())


sys.stdout.write('Falta(m) %d pomekon(s).\n' %(151 - len(set(lista))))
