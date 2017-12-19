

testes = int(raw_input())

while testes > 0:

    seq = raw_input()

    n1 = int(seq[0])
    n2 = int(seq[2])
    letra = ord(seq[1])


    if n1 == n2:
        print n1 * n2
        
    elif letra >= 65 and letra <=90:
        print n2 - n1

    else:
        print n1 + n2

    testes -= 1
