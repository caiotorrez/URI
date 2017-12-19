def leitura(string):
    direita = []
    esquerda = []
    for i in xrange(len(string)):
        if string[i] == '(':
            direita.append(('(',i))

        elif string[i] == ')':
            esquerda.append((')',i))
    return direita, esquerda

def resposta((direita,esquerda)):
    erro = False
    cont = 0
    if len(direita) == len(esquerda):
        for j in xrange(len(direita)):
            if direita[j][0] != esquerda[j][0] and direita[j][1] > esquerda[j][1]:
                erro = True
                return 'incorrect'
        if erro == False:
                    return 'correct'
    else:
        return 'incorrect'
N = 0
while N < 10000:
    try:    
        print resposta(leitura(raw_input()))
        N += 1
    except:
        break
