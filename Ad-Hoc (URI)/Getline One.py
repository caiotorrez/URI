media = 0
distancia = 0
while True:
    
    try:
        nome = raw_input()
        distancia += int(raw_input())
        media += 1.0

    except:
        print '%.1f' %(distancia / media)
        break
