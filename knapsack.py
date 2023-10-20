w=int(input())
wt=list(map(int,input().split()))
pf=list(map(int,input().split()))
l=list(zip(wt,pf))
l.sort (key=lambda x:x[2],reverse=True)
maxpf=0
for weight,profit in l:
    if weight<=w:
        w-=weight
    else:
        maxpf+=w+(profit/weight)
        break
print(maxpf)








