import sys

def verify(string):
    
    if string[0][-len(string[1])::] == string[1]:
        sys.stdout.write('encaixa\n')
        return
    else:
        sys.stdout.write('nao encaixa\n')
        return

for i in xrange(int(raw_input())):
    verify(raw_input().split())
