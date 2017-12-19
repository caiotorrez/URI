
while True:
    try:
        stack = 0
        queue = 0
        priority = 0
        lista = []
        comandos = 0
        st = -1
        fila = 0
        impossivel = False
        for i in xrange(int(raw_input())):
            comando,value = raw_input().split()
            value = int(value)
            if comando == '1':
                lista.append(value)

            else:
                comandos += 1
                if value == lista[st] and queue == 0 or value == lista[-1] and queue == 0:
                    stack += 1
                    st -= 1

                if value == max(lista):
                    priority += 1
                    
                    if value == lista[fila] and stack == 0:
                        queue += 1
                        fila += 1
                    lista[lista.index(max(lista))] = -1

                elif value == lista[fila] and stack == 0:
                    queue += 1
                    fila += 1

                else:
                    if value not in lista:    
                        impossivel = True

        if stack > 0 and priority < stack and queue == 0:
            print 'stack'

        elif priority > stack + queue:
            print 'priority queue'

        elif queue > priority and queue == comandos:
            print 'queue'

        elif impossivel:
            print 'impossible'

        else:
            print 'not sure'
    except:
        break
