

nome, bonus = map(int, raw_input().split())
lista = []
for i in xrange(nome):
    dados = raw_input()
    lista.append((dados[0], dados))

lista.sort()
print lista[bonus - 1][1]
