# coding: utf-8


caracteres = ['`','1','2','3','4','5','6','7','8','9','0','-','=','~','Q','W','E','R','T','Y','U','I','O','P','[',']',"\",'A','S','D','F','G','H','J','K','L',';',"'",'Z','X','C','V','B','N','M',',','.','/']
while True:
    try:  
        entrada = raw_input()
        palavra = ''
        for i in range(len(entrada)):
            if entrada[i] != ' ':
                    

                for j in range(len(caracteres)):

                    if entrada[i] == caracteres[j]:
                        palavra += caracteres[j-1]
            else:
                palavra += ' '

        print palavra

    except:
        break
