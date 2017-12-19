import sys

def verify(food):
    global dieta
    for i in xrange(len(dieta)):

        if food == dieta[i]:
            dieta[i] = -1
            return -1
    return

def diet():
    dieta = list(raw_input())
    global dieta
    coffee = list(raw_input())
    lunch = list(raw_input())
    meal = coffee + lunch

    for j in xrange(len(meal)):

        if verify(meal[j]) == None:
            sys.stdout.write('CHEATER\n')
            return
    dieta.sort()
    for k in xrange(len(dieta)):
        if dieta[k] != -1:
            sys.stdout.write(dieta[k])

    sys.stdout.write('\n')
    return

for i in xrange(int(raw_input())):
    diet()
