for i in xrange(int(raw_input())):
    string = raw_input()
    print string[len(string)/2-1::-1] + string[len(string)/2:len(string)][::-1]
