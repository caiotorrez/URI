def braile(digito, sequencia):
    output = []
    b0 = '.***..'
    b1 = '*.....'
    b2 = '*.*...'
    b3 = '**....'
    b4 = '**.*..'
    b5 = '*..*..'
    b6 = '***...'
    b7 = '****..'
    b8 = '*.**..'
    b9 = '.**...'
    for i in range(digitos):
        if sequencia[i] == '0':
            output.append(b0)
        elif sequencia[i] == '1':
            output.append(b1)
        elif sequencia[i] == '2':
            output.append(b2)
        elif sequencia[i] == '3':
            output.append(b3)
        elif sequencia[i] == '4':
            output.append(b4)
        elif sequencia[i] == '5':
            output.append(b5)
        elif sequencia[i] == '6':
            output.append(b6)
        elif sequencia[i] == '7':
            output.append(b7)
        elif sequencia[i] == '8':
            output.append(b8)
        elif sequencia[i] == '9':
            output.append(b9)
    return output

while True:
    digitos = int(raw_input())

    if digitos == 0:
        break
    
    mode = raw_input()
    
    
    if mode == 'S':
        sequencia = raw_input()
        output = braile(digitos, sequencia)
        a = ''
        b = ''
        c = ''
        for i in range(len(output)):
            if i < len(output)-1:
                a += output[i][0:2] + ' '
                b += output[i][2:4] + ' '
                c += output[i][4:6] + ' '
            else:
                a += output[i][0:2] 
                b += output[i][2:4] 
                c += output[i][4:6]
        print a + '\n' + b + '\n' +  c
                
            
    
        
    else:
        b0 = '.***..'
        b1 = '*.....'
        b2 = '*.*...'
        b3 = '**....'
        b4 = '**.*..'
        b5 = '*..*..'
        b6 = '***...'
        b7 = '****..'
        b8 = '*.**..'
        b9 = '.**...'
        
        a = raw_input().split()
        b = raw_input().split()
        c = raw_input().split()
        resultado = ''
        for i in range(digitos):
            if a[i] + b[i] + c[i] == '.***..':
                resultado += '0'

            elif a[i] + b[i] + c[i] == '*.....':
                resultado += '1'

            elif a[i] + b[i] + c[i] == '*.*...':
                resultado += '2'

            elif a[i] + b[i] + c[i] == '**....':
                resultado += '3'

            elif a[i] + b[i] + c[i] == '**.*..':
                resultado += '4'

            elif a[i] + b[i] + c[i] == '*..*..':
                resultado += '5'

            elif a[i] + b[i] + c[i] == '***...':
                resultado += '6'

            elif a[i] + b[i] + c[i] == '****..':
                resultado += '7'

            elif a[i] + b[i] + c[i] == '*.**..':
                resultado += '8'
                
            elif a[i] + b[i] + c[i] == '.**...':
                resultado += '9'
        print resultado
            
        
        
        


