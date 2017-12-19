import sys
def res():
    while True:
        p, q = raw_input().split()
        if p == '0' and q == '0':
            break
        result = str(int(p) + int(q))

        for i in xrange(len(result)):

            if result[i] != '0':
                sys.stdout.write(result[i])
        sys.stdout.write('\n')
res()
