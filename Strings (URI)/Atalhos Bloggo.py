import sys
def html(texto):
    italic = False
    bold = False
    for i in xrange(len(texto)):
        if texto[i] == '_':
            if italic:
                sys.stdout.write('</i>')
                italic = False
            else:     
                sys.stdout.write('<i>')
                italic = True

        elif texto[i] == '*':
            if bold:
                sys.stdout.write('</b>')
                bold = False
            else:                
                sys.stdout.write('<b>')
                bold = True

        else:
            sys.stdout.write(texto[i])
    sys.stdout.write('\n')
    return
            
while True:
    try:    
        html(raw_input())
        
    except:
        break
