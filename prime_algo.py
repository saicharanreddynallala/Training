def prime(n):
    p={True}+(n+1)
    p1=2
    while(p1*p1<=n):
        if p[p1]:
            for i in range(p1*p1,n+1,p1):
                p[i]=False
        p1+=1
    for p1 in range(2,n+1):
        if p[p1]:
            prime(p1)
n=30
print(prime(n))