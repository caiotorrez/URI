import sys
def res(string):
    frequencia = [[0, 'a'], [0, 'b'], [0, 'c'], [0, 'd'], [0, 'e'], [0, 'f'], [0, 'g'], [0, 'h'], [0, 'i'], [0, 'j'], [0, 'k'], [0, 'l'], [0, 'm'], [0, 'n'], [0, 'o'], [0, 'p'], [0, 'q'], [0, 'r'], [0, 's'], [0, 't'], [0, 'u'], [0, 'v'], [0, 'w'], [0, 'x'], [0, 'y'], [0, 'z']]
    for letter in string:

        if letter == 'a':
            frequencia[0][0] += 1
        elif letter == 'b':
            frequencia[1][0] += 1
        elif letter == 'c':
            frequencia[2][0] += 1
        elif letter == 'd':
            frequencia[3][0] += 1
        elif letter == 'e':
            frequencia[4][0] += 1
        elif letter == 'f':
            frequencia[5][0] += 1
        elif letter == 'g':
            frequencia[6][0] += 1
        elif letter == 'h':
            frequencia[7][0] += 1
        elif letter == 'i':
            frequencia[8][0] += 1
        elif letter == 'j':
            frequencia[9][0] += 1
        elif letter == 'k':
            frequencia[10][0] += 1
        elif letter == 'l':
            frequencia[11][0] += 1
        elif letter == 'm':
            frequencia[12][0] += 1
        elif letter == 'n':
            frequencia[13][0] += 1
        elif letter == 'o':
            frequencia[14][0] += 1
        elif letter == 'p':
            frequencia[15][0] += 1
        elif letter == 'q':
            frequencia[16][0] += 1
        elif letter == 'r':
            frequencia[17][0] += 1
        elif letter == 's':
            frequencia[18][0] += 1
        elif letter == 't':
            frequencia[19][0] += 1
        elif letter == 'u':
            frequencia[20][0] += 1
        elif letter == 'v':
            frequencia[21][0] += 1
        elif letter == 'w':
            frequencia[22][0] += 1
        elif letter == 'x':
            frequencia[23][0] += 1
        elif letter == 'y':
            frequencia[24][0] += 1
        elif letter == 'z':
            frequencia[25][0] += 1
            
    n = max(frequencia)
    for j in xrange(26):
        if frequencia[j][0] == n[0]:
            sys.stdout.write(frequencia[j][1])
    sys.stdout.write('\n')
    return
for i in xrange(int(raw_input())):     
    res(raw_input().lower())

