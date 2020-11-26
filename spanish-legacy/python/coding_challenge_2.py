def narcisistas(n):
    for i in range(0,n+1):
        m = len(str(i))
        s = 0
        for digitos in str(i):
            s += int(digitos)**m
        if s==i:
            print(i)
