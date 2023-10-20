def arrsum(n,s1,s2):
    if s1==s2:
        return n[s1]
    mid=(s1+s2)//2
    return arrsum(n,s1,mid)+arrsum(n,mid+1,s2)
n=list(map(int,input().split()))
print(arrsum(n,0,len(n)-1))