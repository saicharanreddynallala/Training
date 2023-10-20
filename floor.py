def bs_floor(n,l,h,target):
    mid=(l+h)//2
    if target==n[mid]:
        return n[mid]
    elif target>n[mid]:
        if n[mid+1]>target:
            return n[mid]
        return bs_floor(n,l,mid-1,target)
    else:
        return bs_floor(n,mid+1,h,target)
n=list(map(int,input().split()))
target=int(input())
print(bs_floor(n,0,len(n)-1,target))   