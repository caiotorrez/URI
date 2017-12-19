import sys
def res(a,b):
    temp = ''
    for j in xrange(a,b+1):
        temp += str(j)

    sys.stdout.write(temp + temp[::-1] + '\n')
for i in xrange(int(raw_input())):
    
    a, b = map(int, raw_input().split())
    res(a,b)

