
P = raw_input().split()
M = raw_input().split()
F = raw_input().split()
Q = raw_input().split()
B = raw_input().split()

total = []
for i in range(1,int(P[0])+1):
    for j in range(1,int(M[0])+1):
        for k in range(1,int(F[0])+1):
            for l in range(1,int(Q[0])+1):
                for m in range(1,int(B[0])+1):
                    somador = int(P[i]) + int(M[j]) + int(F[k]) + int(Q[l]) + int(B[m])
                    total.append(somador)
                    somador -= int(B[m])

somador = 0
total.sort()
conjunto = int(raw_input())
for e in range(conjunto):
    somador += total[-1-e]

print somador
