import sys
def res(x1,y1,x2,y2):

    if y1 == y2 and x1 == x2:
        return 0
        
    elif y1 == y2 or x1 == x2:
        return 1

    t1 = x1
    t2 = y1
    for i in xrange(8):
        if x1 == x2 and y1 == y2:
            return 1
        else:
            x1 += 1
            y1 -= 1
    x1 = t1
    y1 = t2
    for j in xrange(8):
        if x1 == x2 and y1 == y2:
            return 1
        else:
            x1 -= 1
            y1 -= 1

    x1 = t1
    y1 = t2
    for k in xrange(8):
        if x1 == x2 and y1 == y2:
            return 1
        else:
            x1 -= 1
            y1 += 1
    x1 = t1
    y1 = t2
    for l in xrange(8):
        if x1 == x2 and y1 == y2:
            return 1
        else:
            x1 += 1
            y1 += 1
            
    return 2
while True:
    
    x1,y1,x2,y2 = map(int, raw_input().split())
    if x1 == 0:
        break
    sys.stdout.write('%d\n' %res(x1,y1,x2,y2))
