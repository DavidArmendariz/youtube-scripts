function eratostenes(n)
    primos = [true for i in 1:n]
    #primos[0] = False
    #primos[1] = False
    for m = 2:n
        k = 2
        while m*k <= n
            primos[m*k] = false
            k += 1
        end
    end
    primos_val = []
    for m = 2:n
        if primos[m] == true
            push!(primos_val,m)
        end
    end
    N = length(primos_val)
    tuplas1 = []
    for i = 1:(N-1)
        for j = (i+1):N
            if primos_val[j]-primos_val[i] == 6
                push!(tuplas1,(primos_val[i],primos_val[j]))
            end
        end
    end
    tuplas2 = []
    for i = 1:(N-2)
        for j = (i+1):(N-1)
            for k = (j+1):N
                cond1 = primos_val[j]-primos_val[i] == 6
                cond2 = primos_val[k]-primos_val[j] == 6
                if cond1 & cond2
                    push!(tuplas2,(primos_val[i],primos_val[j],primos_val[k]))
                end
            end
        end
    end
    return tuplas1,tuplas2
end
