def power(power):
    base = 2
    result = 1
    while power > 0:
        if power % 2 == 1:
            result = (result * base)
        power = power / 2
        base = (base * base)
    return result
def resposta(n):
    uri = [0,0,0]
    for i in xrange(n):
        maior = [0,-1]
        data = map(int, raw_input().split())
        if data[0] in lista:
            uri[0] += 1
            if data[0] == max(data):
                uri[0] += 1
        if data[1] in lista:
            uri[1] += 1
            if data[1] == max(data):
                uri[1] += 1
        if data[2] in lista:
            uri[2] += 1
            if data[2] == max(data):
                uri[2] += 1

    if uri[0] > uri[1] and uri[0] > uri[2]:
        return 'Uilton'
    elif uri[1] > uri[2] and uri[1] > uri[0]:
        return 'Rita'
    elif uri[2] > uri[1] and uri[2] > uri[0]:
        return 'Ingred'

    else:
        return 'URI'

lista = []
for i in xrange(31):
    lista.append(power(i))
while True:        
    n = int(raw_input())
    if n == 0:
        break
    else:
        print resposta(n)
