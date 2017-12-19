
def keygen(password):
    
    if len(password) < 6 or len(password) > 32:
        return 'Senha invalida.'
    
    upper = 0
    lower = 0
    number = 0
    for i in xrange(len(password)):

        if ord(password[i]) >= 97 and ord(password[i]) <= 122:
            upper += 1
        elif ord(password[i]) >= 65 and ord(password[i]) <= 90:
            lower += 1
        elif ord(password[i]) >= 48 and ord(password[i]) <= 57:
            number += 1  
        else:
            return 'Senha invalida.'

    if upper > 0 and lower > 0 and number > 0:
        return 'Senha valida.'
    else:
        return 'Senha invalida.'
    
while True:
    try:      
        print keygen(raw_input())
    except:
        break
