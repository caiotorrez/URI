import sys
def verifica(word):
    
    for i in xrange(10):
        if str(i) in word:
            return 0
        
    if '..' in word:
        return 0

    if '.' in word:
        if word[-1] != '.':
            return 0
        else:
            return len(word)-1

    return len(word)    
def res(words):
    validas = 0
    total = 0
    for i in xrange(len(words)):
        n = verifica(words[i])
        if n > 0:
            validas += 1
            total += n
    if validas > 0:
        total = total / validas
    if total > 5:
        sys.stdout.write('1000\n')
        return
    elif total > 3:
        sys.stdout.write('500\n')
        return
    else:
        sys.stdout.write('250\n')
        return
while True:
    try:res(raw_input().split())
    except:break
