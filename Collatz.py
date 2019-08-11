import random
def collatz(n,maxiter):
    def f(m):
        if m%2==0:
            return int(m/2)
        else:
            return 3*m+1
    l = [random.randint(1,1000) for i in range(n)]
    for i in l:
        c = 1
        num = [i]
        r = i
        while c <= maxiter:
            r = f(r)
            num.append(r)
            c += 1
            if r == 1:
                break
        print(str(i)+":\n")
        print(num)
        print("\n\n")
