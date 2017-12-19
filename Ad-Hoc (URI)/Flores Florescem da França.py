
def tautograma(setenca):
    for i in xrange(len(setenca)):
        if setenca[i] == ' ' and setenca[i + 1] != setenca[0]:
            return 'N'
    return 'Y'

while True:
    name = raw_input()
    if name == '*':
        break
    
    print tautograma(name.lower())
            

        
