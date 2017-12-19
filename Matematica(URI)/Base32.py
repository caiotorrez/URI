total = []
def conv(n):

    if n <= 31:
        if n < 10:
            total.append(str(n))
        else:
            total.append(dic[n])
        return

    temp = n%32
    if temp < 32 and temp >= 10:
        total.append(dic[temp])
    else:
        total.append(str(temp))
    conv(n/32)
        
lista = ['ABCDEFGHIJKLMNOPQRSTUV']
mirror = [i for i in xrange(10,32)]
dic = {}
for i in xrange(22):
    dic[10 + i] = lista[0][i]


while True:
    n = int(raw_input())
    if n == 0:
        print 0
        break
    total = []
    conv(n)
    print "".join(total[::-1])

