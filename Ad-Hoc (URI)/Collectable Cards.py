from fractions import gcd

entrada = int(raw_input())

for i in xrange(entrada):
    x,y = map(int, raw_input().split())

    print gcd(x,y)
