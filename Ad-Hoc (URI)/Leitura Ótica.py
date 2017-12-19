def scan(A,B,C,D,E):
    
    resposta = [0,0,0,0,0]

    if A <= 127:
        resposta[0] = 1

    if B <= 127:
        resposta[1] = 1

    if C <= 127:
        resposta[2] = 1

    if D <= 127:
        resposta[3] = 1
            
    if E <= 127:
        resposta[4] = 1
        
    
    if resposta.count(1) == 1:
        for i in range(5):
            if resposta[i] == 1:
                if i == 0:
                    return 'A'

                elif i == 1:
                    return 'B'

                elif i == 2:
                    return 'C'

                elif i == 3:
                    return 'D'

                else:
                    return 'E'
    else:
        return '*'
                
while True:
    
    questoes = int(raw_input())
    if questoes == 0:
        break
    
    while questoes > 0:
            
        alternativas = raw_input().split()
        A = int(alternativas[0])
        B = int(alternativas[1])
        C = int(alternativas[2])
        D = int(alternativas[3])
        E = int(alternativas[4])

        print scan(A,B,C,D,E)

        questoes -= 1

            






            
