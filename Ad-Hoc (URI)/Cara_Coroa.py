
def cara_coroa(resultado):
    
    john = 0
    mary = 0
    for e in resultado:
        if e == '1':
            john += 1
        elif e == '0':
            mary += 1
    return "Mary won %d times and John won %d times" %(mary,john)

while True:
    jogadas = int(raw_input())
    if jogadas == 0:
        break
    resultado = raw_input().split()
    print cara_coroa(resultado)
