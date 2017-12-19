

def alarme(H1,M1,H2,M2):
    
    total = 0
    while H1 != H2 or M1 != M2:

        total += 1

        M1 += 1

        if M1 == 60:
            M1 = 0
            H1 += 1
            if H1 == 24:
                H1 = 0

    return total

while True:
    
    H1,M1,H2,M2 = raw_input().split()
    
    if H1 == '0' and M1 == '0' and H2 == '0' and M2 == '0': break
    
    H1 = int(H1)
    M1 = int(M1)
    H2 = int(H2)
    M2 = int(M2)

    print alarme(H1,M1,H2,M2)
