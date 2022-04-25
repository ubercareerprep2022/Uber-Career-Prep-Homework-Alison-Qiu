def cut(L,i,j,l,r):
    if l==r:
        return (0,[])
    min_cost = 1000
    for ind in range(i,j):
        k = ind
        if l+r+ cut(L,i,k,l,L[k]) + cut(L,k, j,L[k],j)<min_cost:
            min_cost = r-l+cut(L,i,k,l,L[k])+cut(L,k+1, j,L[k],j)
        return (min_cost,[])

L = [2,8,10]
