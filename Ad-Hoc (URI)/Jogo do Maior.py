
def jogo_do_maior(fichas):
        
    p1 = 0
    p2 = 0
    while fichas > 0:
        
        jogada = raw_input().split()
        if int(jogada[0]) > int(jogada[1]):
            p1 += 1
        elif int(jogada[0]) < int(jogada[1]):
            p2 += 1
        fichas -= 1
        
    return "%d %d" %(p1,p2)

while True:
        
    fichas = int(raw_input())
    if fichas > 0:
        print jogo_do_maior(fichas)
    else:
        break
