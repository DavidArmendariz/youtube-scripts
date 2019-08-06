def eratostenes(n):
    primos = [True for i in range(n+1)]
    #primos[0] = False
    #primos[1] = False
    for m in range(2,n+1):
        k = 2
        while m*k <= n:
            primos[m*k] = False
            k += 1
    primos_val = []
    for m in range(2,n+1):
        if primos[m] == True:
            primos_val.append(m)
    N = len(primos_val)
    tuplas1 = []
    for i in range(N-1):
        for j in range(i+1,N):
            if primos_val[j]-primos_val[i] == 6:
                tuplas1.append((primos_val[i],primos_val[j]))
    tuplas2 = []
    for i in range(N-2):
        for j in range(i+1,N-1):
            for k in range(j+1,N):
                cond1 = primos_val[j]-primos_val[i] == 6
                cond2 = primos_val[k]-primos_val[j] == 6
                if cond1 and cond2:
                    tuplas2.append((primos_val[i],primos_val[j],primos_val[k]))
    return tuplas1,tuplas2
        