import sys
def verifique(letra, start, end):
    i = 0
    while i + start < len(string1) and i + end < len(string2):
        if string1[start + i] != string2[end + i]:
            return i + 1
        i += 1
    return i + 1

def res(string1, string2):
    total = 0
    obs = []
    for i in xrange(len(string1)):
        if total + i >= len(string1):
            return total
        flag = True
        if string1[i] not in obs:
            for j in xrange(len(string2)):
                if string1[i] == string2[j]:
                    flag = False
                    n = (verifique(string1[i], i+1, j+1))
                    if n > total:
                        total = n
            if flag:
                obs.append(string1[i])
    return total
           
    return
while True:
    try:
        string1 = raw_input()
        string2 = raw_input()
        sys.stdout.write('%d\n' %res(string1, string2))
    except:
        break
