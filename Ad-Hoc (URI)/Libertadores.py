


for i in xrange(int(raw_input())):
    time1 = []
    time2 = []
    placar = raw_input().split(' x ')
    time1.append(int(placar[0]))
    time2.append(int(placar[1]))
    placar = raw_input().split(' x ')
    time1.append(int(placar[1]))
    time2.append(int(placar[0]))

    if sum(time1) > sum(time2):
        print 'Time 1'

    elif sum(time2) > sum(time1):
        print 'Time 2'

    elif time1[1] > time2[0]:
        print 'Time 1'

    elif time1[1] < time2[0]:
        print 'Time 2'

    else:
        print 'Penaltis'

    
