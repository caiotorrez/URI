lista = [2432902008176640000,121645100408832000,6402373705728000,355687428096000,20922789888000,1307674368000,87178291200,6227020800,479001600,39916800,3628800,362880,40320,5040,720,120,24,6,2,1,1]

while True:

    try:
        entrada = raw_input().split()
        n1 = int(entrada[0])
        n2 = int(entrada[1])
        print lista[20 - n1] + lista[20 - n2]

    except:
        break