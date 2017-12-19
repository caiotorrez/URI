import math

while True:
    try:
        r1, x1, y1, r2, x2, y2 = map(int, raw_input().split())
        
        d = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
        
        if d + r2 > r1:
            print 'MORTO'
        else:
            print 'RICO'
    except:
        break
