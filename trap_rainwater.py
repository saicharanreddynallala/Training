
def trap( height):
    n=len(height)
    if n==0:
        return 0
        
    l=0
    r=n-1
    lmax=height[l]
    rmax=height[r]
    res=0
    while l<r:
        if lmax<rmax:
            l+=1
            if lmax<height[l]:
                lmax=height[l]
            res+=lmax-height[l]
        else:
            r-=1
            if rmax<height[r]:
                rmax=height[r]
            res+=rmax-height[r]
    return res
height=list(map(int,input().split()))
print(trap(height))
    