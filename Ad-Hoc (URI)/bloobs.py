
def dias(x):
    
    cont = 0
    while x > 1:
         x = x/2.0
         cont += 1

    return cont

  
entrada = int(raw_input())
  
while entrada > 0:
    cont = 0
    x = float(raw_input())

    if x > 1:
        print "%d dias" %(dias(x))

    else:
        print '0 dias'

    entrada -= 1

