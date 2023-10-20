l={10,9,12,4,5,2,8,5,3,1}
maxele=max(l)
for i in range(maxele,0,-1):
    print(f"{i:2d} | ",end="")
    for j in l:
        if j>=i:
            print("*",end="")
        else:
            print(" ",end="")
    print()
    