
def bussola(seq):
        
    direcao = 0
    for i in range(len(seq)):

        if seq[i] == 'D':
            direcao += 1

        elif seq[i] == 'E':
            direcao -= 1

    total = abs(direcao)%4

    if direcao > 0:

        if total == 0:
            return 'N'

        elif total == 1:
            return 'L'

        elif total == 2:
            return 'S'

        elif total == 3:
            return 'O'

    else:
        if total == 0:
            return 'N'

        elif total == 1:
            return 'O'

        elif total == 2:
            return 'S'

        elif total == 3:
            return 'L'

while True:
    
    teste = raw_input()
    if teste == '0':
        break

    print bussola(raw_input())

