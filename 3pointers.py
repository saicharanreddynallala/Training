def find(l,target):
    for i in range (len(l)):
        a=l[i]
        if target==a:
            return  
        diff= target-a
        b=i+1
        c=len(l)-1
        while b<c:
            if l[b]+l[c]<diff:
                b+=1
            elif l[b]+l[c]>diff:
                c-=1
            else:
                return a,l[b],l[c]
l=list(map(int,input().split()))
target=int(input())
print(find(l,target))

