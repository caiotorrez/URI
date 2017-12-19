def resposta(nomes):
    nomes = nomes.split()
    for i in xrange(n):
        
        if len(nomes[i]) == 3 and nomes[i][0] + nomes[i][1] == 'OB':
            corretor.append('OBI')
        elif len(nomes[i]) == 3 and nomes[i][0] + nomes[i][1] == 'UR':
            corretor.append('URI')
        else:
            corretor.append(nomes[i])
    return ' '.join(corretor)
corretor = []
n = int(raw_input())
print resposta(raw_input())
