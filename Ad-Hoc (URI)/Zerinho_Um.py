
while True:
        
    try:
        jogada = raw_input().split()
        A = int(jogada[0])
        B = int(jogada[1])
        C = int(jogada[2])

        if A == 1 and B == 0 and C == 0:
            print 'A'
        elif A == 1 and B == 1 and C == 0:
            print 'C'
        elif A == 1 and B == 0 and C == 1:
            print 'B'
        elif A == 0 and B == 1 and C == 1:
            print 'A'
        elif A == 0 and B == 1 and C == 0:
            print 'B'
        elif A == 0 and B == 0 and C == 1:
            print 'C'
        else:
            print '*'

    except:
        break
