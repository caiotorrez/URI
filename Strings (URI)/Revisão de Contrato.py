import sys
def resposta(falha, numero):
    aux = ''
    for e in numero:
        if falha != e:
            aux += e
    i = 0
    while i < len(aux):

        if aux[i] != '0':
            sys.stdout.write(aux[i::] + '\n')
            return
        i += 1
    sys.stdout.write('0\n')

while True:
    
    falha, numero = raw_input().split()
    if falha == '0' and numero == '0':
        break
    resposta(falha, numero)
