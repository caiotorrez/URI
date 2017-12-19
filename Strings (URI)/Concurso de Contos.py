import sys
def res(linhas, char):
    texto = raw_input().split()
    lenght = []
    for i in xrange(len(texto)):

        if i > 0:
            lenght.append(' ')
            
        lenght.append(len(texto[i]))

    soma = 0
    total = 0
    i = 0
    while i < len(lenght):

        if soma == char:
            soma = 0
            total += 1

        elif soma > char:
            total += 1
            i -= 1
            soma = 0

        if lenght[i] != ' ' and lenght[i] <= char:soma += lenght[i]
        else:
            if soma != 0:
                soma += 1
        i += 1

    if soma > 0:
        if soma > char:
            total += 2
        else:
            total += 1

    n = total / linhas
    if total % linhas > 0:
        n += 1
    sys.stdout.write('%d\n' %n)
    return
while True:
    try:
        
        palavras, linhas, char = map(int, raw_input().split())
        res(linhas, char)
    except:break
