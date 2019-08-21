def coding_challenge3(x):
    count = 0
    for i in range(1,len(x)-1):
        if x[i-1] == 1 and x[i] == 1 and x[i+1] == 0:
            count += 1
        if i == len(x)-2 and x[i] == 1 and x[i+1] == 1:
            count += 1
    return count