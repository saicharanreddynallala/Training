def mergeSort(l):
    if len(l)>1:
        mid=len(l)//2
        left=l[:mid]
        right=l[mid:]
        left=mergeSort(left)
        right=mergeSort(right)
        mergeSort(left)
        mergeSort(right)
        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                l[k]=left[i]
                i+=1
                k+=1
            else:
                l[k]=right[j]
                j+=1
                k+=1
        while i<len(left):
            l[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            l[k]=right[j]
            j+=1
            k+=1  
    return l

n=[x for x in input().split()]
print(mergeSort(n))