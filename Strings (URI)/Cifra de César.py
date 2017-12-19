import sys
def cesar(name, switch):
    for i in xrange(len(name)):
        letter = name[i] - switch
        if letter < 65:letter += 26

        sys.stdout.write(chr(letter))
    sys.stdout.write('\n')
for k in xrange(int(raw_input())):

    name = map(ord, raw_input())
    switch = int(raw_input()) % 26
    cesar(name, switch)
