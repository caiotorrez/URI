import sys
for t in xrange(int(raw_input())):

    total = 0
    for k in xrange(int(raw_input())):
        letter = map(ord, raw_input())
        for i in xrange(len(letter)):
            n = letter[i] - 65 + k + i
            total += n
    sys.stdout.write('%d\n' %total)

        
