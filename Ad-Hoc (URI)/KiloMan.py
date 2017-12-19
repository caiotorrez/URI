
def KiloMan(tiros, altura, movimento):
    
    recebidos = 0
    for i in range(tiros):

        if int(altura[i]) < 3 and movimento[i] == 'S':
            recebidos += 1

        elif int(altura[i]) > 2 and movimento[i] == 'J':
            recebidos += 1

    return recebidos

lifes = int(raw_input())
while lifes > 0:
    
    tiros = int(raw_input())
    altura = raw_input().split()
    movimento = raw_input()
    print KiloMan(tiros, altura, movimento)
    lifes -= 1
