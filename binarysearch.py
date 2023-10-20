def binarysearch(n,low,high,key):
    if low>high:
        return -1
    mid=(low+high)//2
    if key==n[mid]:
        return mid
    if n[mid]<key:
        return binarysearch(n,mid+1,high,key)
    if n[mid]>key:
        return binarysearch(n,low,mid-1,key)
n=list(map(int,input().split()))
key=int(input())
print(binarysearch(n,0,len(n)-1,key)+1)   
    

