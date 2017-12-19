
dias = int(raw_input())
total = 0
resultado = []
variedade = 0.0
for i in range(dias):

    valor = float(raw_input())
    frutas = raw_input().split()
    resultado.append(len(frutas))
    total += valor
    variedade += len(frutas)

for j in range(len(resultado)):

    print 'day %d: %s kg' %(j+1,resultado[j])

print '%.2f kg by day' %(variedade/len(resultado))
print 'R$ %.2f by day' %(total/len(resultado))
