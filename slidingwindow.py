def sliding(n,target):
    i=0
    j=1
    while j<len(n):
        if n[i]+n[j]==target:
            return (n[i],n[j])
        i+=1
        j+=1
n=list(map(int,input().split()))
target=int(input())
print(sliding(n,target))