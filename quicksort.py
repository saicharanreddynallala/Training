#quick sort
def quicksort(l,start,end):
    pi=l[end]
    i=start-1
    for j in range(start,end):
        if l[j]<pi:
            i=i+1
            l[i],l[j]=l[j],l[i]
    l[i+1],l[end]=l[end],l[i+1]
    return i+1

def quick(l,start,end):
    if start<end:
        pi=quicksort(l,start,end)
        quick(l,start,pi-1)
        quick(l,pi+1,end)


l=list(map(int,input().split()))
quick(l,0,len(l)-1)
print(l)



# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     pivot = arr[len(arr) // 2]
#     left = [x for x in arr if x < pivot]
#     middle = [x for x in arr if x == pivot]
#     right = [x for x in arr if x > pivot]

#     return quick_sort(left) + middle + quick_sort(right)

# # Example usage:
# my_list = [3, 6, 8, 10, 1, 2, 1]
# sorted_list = quick_sort(my_list)
# print(sorted_list)  # Output: [1, 1, 2, 3, 6, 8, 10













