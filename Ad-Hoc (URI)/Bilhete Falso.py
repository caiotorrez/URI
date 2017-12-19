
while True:
    

    ingresso, pessoas = map(int, raw_input().split())
    if ingresso == 0 and pessoas == 0:
        break
    codigo = map(int, raw_input().split())
    original = []
    falso = []
    for i in range(len(codigo)):
        if codigo[i] <= ingresso and codigo[i] not in original:
            original.append(codigo[i])
        elif codigo[i] not in falso:
            falso.append(codigo[i])

    print len(falso)
