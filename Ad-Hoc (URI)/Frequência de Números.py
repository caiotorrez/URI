
def repetidos(n,lista):

    somador = 0
    for i in range(len(lista)-1,-1,-1):
        if n == lista[i]:
            somador += 1
            lista.pop(i)
            
    return "%d aparece %d vez(es)" %(n,somador)

    
entrada = int(raw_input())
total = []
for i in range(entrada):

    valor = int(raw_input())
    total.append(valor)

while len(total) != 0:

    n = total[0]

    for k in total:
        if k < n:
            n = k
            
    print repetidos(n,total)
