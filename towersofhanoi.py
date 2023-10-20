def toh(n,s,a,d):
    if n == 1:
        return 1
    count1 = toh(n-1,s,d,a)
    count2 = 1
    count3 = toh(n-1,a,s,d)
    return count1+count2+count3

n = int(input())
print(toh(n,'A','B','C'))