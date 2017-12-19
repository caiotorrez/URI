import sys
for e in xrange(int(raw_input())):
    
    entrada = map(ord, raw_input())
    mid = ((len(entrada)+1)) / 2
    for i in xrange(len(entrada)):

        if entrada[i] >= 65 and entrada[i] <= 90 or entrada[i] >= 97 and entrada[i] <= 122:
            entrada[i] += 3
        if i < mid:
            entrada[i] -= 1
        entrada[i] = chr(entrada[i])

    sys.stdout.write(''.join(entrada[::-1]) + '\n')
