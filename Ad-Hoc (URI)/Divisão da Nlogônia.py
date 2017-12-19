
def mapeamento(x,y):

    pontos = raw_input().split()
    x1 = int(pontos[0])
    y1 = int(pontos[1])
    if x1 == x or y1 == y:
        return 'divisa'

    elif x1 > x and y1 > y:
        return 'NE'

    elif x1 < x and y1 > y:
        return 'NO'

    elif x1 < x and y1 < y:
        return 'SO'

    elif x1 > x and y1 < y:
        return 'SE'

while True:

    testes = int(raw_input())
    if testes > 0:
        cordenadas = raw_input().split()
        x = int(cordenadas[0])
        y = int(cordenadas[1])

        while testes > 0:

            print mapeamento(x,y)
            testes -= 1
    else:
        break
