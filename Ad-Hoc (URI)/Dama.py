
while True:
        
    move = raw_input().split()
    if move[0] == '0' or move[1] == '0' or move[2] == '0' or move[3] == '0':
        break

    elif move[0] == move[2] and move[1] == move[3]:
        print '0'

    elif move[0] == move[1] and (int(move[2]) + int(move[3]))%2 == 0:
        print '1'

    elif move[0] == move[1] and (int(move[2]) + int(move[3]))%2 != 0:
        print '2'

    elif move[2] == move[3] and (int(move[0]) + int(move[1]))%2 == 0:
        print '1'

    elif move[2] == move[3] and (int(move[0]) + int(move[1]))%2 != 0:
        print '2'

    elif int(move[0])%2 == 0 and int(move[1])%2 == 0 and int(move[2])%2 == 0 and int(move[3])%2 == 0:
        print '1'
        
    elif (int(move[0]) + int(move[1]) + int(move[2]) + int(move[3])) % 2 != 0:
        print '2'    

    else:
        print '0'
