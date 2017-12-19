def binario(decimal):
        
    vetor = [0]*32
    i = 0
    while decimal > 0:

        if decimal % 2 == 0:
            vetor[-i-1] = 0
            decimal = decimal/2
            i += 1

        elif decimal %2 == 1:
            vetor[-i-1] = 1
            decimal = decimal/2
            i += 1

    return vetor

def somador(bin1, bin2):
        
    somador = 0
    for i in range(32):
        if binario1[-i-1] != binario2[-i-1]:
            somador += 2**i

    return somador

while True:
    try:
        decimal = raw_input().split()
        binario1 = binario(int(decimal[0]))
        binario2 = binario(int(decimal[1]))
        print somador(binario1, binario2)

    except:
        break

    


