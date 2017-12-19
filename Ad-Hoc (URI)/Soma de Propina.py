

def valores(lista1, lista2):
    cpf = ''
    valor1 = ''
    valor2 = ''
    ponto = False
    cont = 0
    for e in lista1: 
        if e == '.' or e == '1' or e == '2' or e == '3' or e == '4' or e == '5' or e == '6' or e == '7' or e == '8' or e == '9' or e == '0':
            if e == '.' and ponto == True:
                pass   
            elif len(valor1) == 17:
                break
            elif len(cpf) < 11:
                cpf += e
            elif len(valor1) < 17 and cont < 2:
                if e == '.':
                    ponto = True
                elif ponto == True:
                    cont += 1  
                valor1 += e
    cont = 0
    ponto = False
    for e in lista2:   
        if e == '.' or e == '1' or e == '2' or e == '3' or e == '4' or e == '5' or e == '6' or e == '7' or e == '8' or e == '9' or e == '0':
            if e == '.' and ponto == True:
                pass
            elif len(valor2) == 17:
                break
            elif len(cpf) < 11:
                cpf += e
            elif len(valor2) < 17 and cont < 2:
                if e == '.':
                    ponto = True    
                elif ponto == True:
                    cont += 1  
                valor2 += e

    return cpf, float(valor1) + float(valor2)

lista1 = raw_input()
lista2 = raw_input()

print 'cpf %s\n%.2f' %(valores(lista1, lista2))
















                
