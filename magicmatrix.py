# n=int(input())
# sq=[[0]*n for i in range(n)]
# num=1  
# i=n//2
# j=n-1
# while num<=(n*n):
#     if i<0 and j==n:
#         i=0
#         j=n-2
#     else:
#         if j==n:
#             j=0
#         if i<0:
#             i=n-1
#         if sq[i][j]:
#             i=i+1
#             j=j-2
#             continue
#     sq[i][j]=num
#     num+=1
#     i-=1
#     j=j+1
# for i in sq:
#     print(*i)


#using recursion 
def generate_matrix(n):
    m=[[0]*n for i in range(n)]
    def fill(i,j,x):
        if x>n*n:
            return m
        if i<0 and j==n:
            i=0
            j=n-2
        else:
            if j==n:
                j=0
            if i<0:
                i=n-1
            if m[i][j]:
                return fill(i+1,j-2,x)
        m[i][j]=x
        return fill(i-1,j+1,x+1)
    return fill(n//2,n-1,1)
n=int(input())
if n%2==0:
    print("Invalid")
    exit()
a=generate_matrix(n)

for i in a:
    print(*i)