while True:
        
    N = int(raw_input())
    if N == 0:
        break
    
    total = 0
    while N > 1:

        total += N **2
        N -= 1

    print total+1
