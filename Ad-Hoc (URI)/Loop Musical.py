
def loop(lista):
        
    cont = 0
    for i in range(1,len(lista)-1):

        if int(lista[i]) < int(lista[i-1]) and int(lista[i]) < int(lista[i+1]):
            cont += 1

        elif int(lista[i]) > int(lista[i-1]) and int(lista[i]) > int(lista[i+1]):
            cont += 1
    
    if int(lista[-1]) > int(lista[-2]) and int(lista[-1]) > int(lista[0]):
        cont += 1

    if int(lista[-1]) < int(lista[-2]) and int(lista[-1]) < int(lista[0]):
        cont += 1

    if int(lista[0]) > int(lista[-1]) and int(lista[0]) > int(lista[1]):
        cont += 1

    if int(lista[0]) < int(lista[-1]) and int(lista[0]) < int(lista[1]):
        cont += 1

    return cont

while True:
    entrada = raw_input()
    if entrada == '0':
        break

    lista = raw_input().split()
    if len(lista) > 3:
        print loop(lista)

    else:
        print '2'
