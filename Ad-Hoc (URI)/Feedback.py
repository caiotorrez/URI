

entrada = int(raw_input())

while entrada > 0:

    testes = int(raw_input())

    while testes > 0:

        setor = raw_input()

        if setor == '1':
            print 'Rolien'

        elif setor == '2':
            print 'Naej'

        elif setor == '3':
            print 'Elehcim'

        elif setor == '4':
            print 'Odranoel'

        testes -= 1
    entrada -= 1
