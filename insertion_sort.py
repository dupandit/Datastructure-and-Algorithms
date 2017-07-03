def Insertion_sort(arr):
    l=len(arr)
    for i in range(l):
        for j in range(i):
            if arr[i]<=arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
    return arr


x=[9,9,9,9,9,9,0]
print Insertion_sort(x)