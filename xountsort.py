def countsort(n):
    res=[0]*len(n)
    count=[0]*(max(n)+1)
    for i in n:
        count[i]+=1
    for i in range(1,len(count)):
        count[i]+=count[i-1]
    print(count)
    for i in n:
        res[count[i]-1]=i
        count[i]-=1
    print(res)
n=list(map(int,input().split()))
countsort(n)
