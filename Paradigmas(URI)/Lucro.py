
def solve(index, lista):
    memo = [lista[index] - custo]
    if len(lista) == index + 1:
        return lista[index] - custo
    
    try:
        for i in xrange(len(lista) - (index + 1)):
            soma = memo[i] + lista[index + i + 1] - custo

            if soma > 0:
                memo.append(soma)
    except:
        pass
    return max(memo)
    
while True:
    try:       
        dias = int(raw_input())
        custo = int(raw_input())

        if dias == 0:
            print 0

        else:
            lucro = []
            for i in xrange(dias):
                lucro.append(int(raw_input()))

            total = []
            cache = [0]*dias
            for i in xrange(dias):

                if lucro[i] > custo:
                    cache[i] = solve(i, lucro)

                else:
                    cache[i] = 0

            cache.sort()
            print cache[-1]
    except:
        break
