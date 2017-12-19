import sys

def combinador(entrada):
    
    if len(entrada[0]) > len(entrada[1]):
        lenght = len(entrada[1])
        flag = True
    else:
        lenght = len(entrada[0])
        flag = False
    for j in xrange(lenght):
        sys.stdout.write(entrada[0][j])
        sys.stdout.write(entrada[1][j])

    if flag:
        sys.stdout.write(entrada[0][j+1::] + '\n')

    else:
        sys.stdout.write(entrada[1][j+1::] + '\n')


for i in xrange(int(raw_input())):

    combinador(raw_input().split())
