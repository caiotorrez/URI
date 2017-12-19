
entrada = int(raw_input())
par = 1
while entrada > 0:
    S = int(raw_input(),2)
    L = int(raw_input(),2)
    
    if S%2 == 0 and L%2 == 0:
        print "Pair #%d: All you need is love!" %(par)
    elif S%3 == 0 and L%3 == 0:
        print "Pair #%d: All you need is love!" %(par)
    elif S%5 == 0 and L%5 == 0:
        print "Pair #%d: All you need is love!" %(par)
    elif S%7 == 0 and L%7 == 0:
        print "Pair #%d: All you need is love!" %(par)
    elif S%23 == 0 and L%23 == 0:
        print "Pair #%d: All you need is love!" %(par)
    else:
        print "Pair #%d: Love is not all you need!" %(par)
    entrada -= 1
    par += 1
