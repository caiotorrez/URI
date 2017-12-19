import sys

lista = []
total = []
while True:
    try:
        n = raw_input()
        m = n.lower()
        lista.append((m,n))
    except:
        break
lista.sort()
sys.stdout.write(lista[-1][1] + '\n')
