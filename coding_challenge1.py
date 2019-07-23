def coding_challenge1(x):
    y = []
    s = []
    n = len(x)
    print("Secuencias")
    for i in range(n-1):
        if x[i] < x[i+1]:
            y.append(x[i])
            if i==n-2:
                y.append(x[i+1])
                s.append(sum(y))
                print(y)
            continue
        elif x[i] >= x[i+1] and x[i] > x[i-1]:
            y.append(x[i])
            s.append(sum(y))
            print(y)
            y = []
    print("Sumas de las secuencias")
    for e in s:
        print(e)
    print("Suma máxima ", max(s))