


while True:
    try:
        def paridade(entrada):
            
            pares_d = [0]*61
            pares_e = [0]*61
            total = 0
            for i in xrange(entrada):

                n, pe = raw_input().split()
                n = int(n)

                if pe == 'D':    
                    pares_d[n] += 1

                else:
                    pares_e[n] += 1

            for k in xrange(29,61):

                if pares_d[k] > 0 and pares_e[k] > 0:
                    total += min(pares_d[k],pares_e[k])

            return total

        print paridade(int(raw_input()))

    except:
        break


