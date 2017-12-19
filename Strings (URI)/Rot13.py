import sys
def res(string):
        
    for i in xrange(len(string)):

        if string[i] >= 65 and string[i] <= 90:
            letter = string[i] + 13
            if letter > 90:
                letter = letter - 26

            sys.stdout.write(chr(letter))

        elif string[i] >= 97 and string[i] <= 122:
            letter = string[i] + 13
            if letter > 122:
                letter = letter - 26

            sys.stdout.write(chr(letter))

        else:
            sys.stdout.write(chr(string[i]))
    sys.stdout.write('\n')
    return

while True:
    try:res(map(ord, raw_input()))
    except:break
