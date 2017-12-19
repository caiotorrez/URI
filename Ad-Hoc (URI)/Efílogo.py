import sys
import string

texto = ''
while True:
    try: texto += raw_input() + '\n'
    except(EOFError): break

texto = texto.translate(string.maketrans('sjbzpvxSJBZPVX', 'fffffffFFFFFFF'))

sys.stdout.write(texto[0])
for i in xrange(1,len(texto)):
    
    if texto[i] == 'f' or texto[i] == 'F':
        if texto[i-1] != 'f' and texto[i-1] != 'F':
            sys.stdout.write(texto[i])
        else:
            continue
    else:
        sys.stdout.write(texto[i])
