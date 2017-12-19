import sys
def res(string):
    i = 0
    j = 0
    while j < len(string):
        if string[j] != 32:
            if i % 2 == 0:
                if string[j] >= 65 and string[j] <= 90:
                    sys.stdout.write(chr(string[j]))
                else:  
                    sys.stdout.write(chr(string[j] -32))
                i += 1
            else:
                if string[j] >= 97 and string[j] <= 122:
                    sys.stdout.write(chr(string[j]))
                else:
                    sys.stdout.write(chr(string[j] + 32))
                i += 1
        else:
            sys.stdout.write(' ')    
        j += 1
    sys.stdout.write('\n')

while True:
    try:
        res(map(ord, raw_input()))
        
    except:
        break
