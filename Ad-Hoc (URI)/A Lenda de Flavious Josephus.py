
def search(n, kill):
    
    array = [True]*n
    i = 0
    k = 0
    cont = 0
    while cont < len(array)-1:

        if array[i]:
            pos = i - kill
            k += 1
            
        if k == kill:
            array[i] = False
            cont += 1
            k = 0
        if i == len(array)-1:
            i = -1

        i += 1

    for k in xrange(len(array)):

        if array[k]:
            return k+1

entrada = int(raw_input())
for i in xrange(entrada):
    n, kill = map(int, raw_input().split())
    print "Case %d: %d" %(i+1,search(n, kill))
    
