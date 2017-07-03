def Merge(arr,start,m,end):
    L1=[]
    L2=[]
    print 'Original array  :', arr
    for i in range(start,m+1):
        L1.append(arr[i])
    for i in range(m+1,end+1):
        L2.append(arr[i])

    len1=len(L1)
    len2=len(L2)

    print 'L1 : ',L1
    print 'L2 : ',L2

    i=0 #counter of 1st subarray
    j=0 #counter of 2nd subarray
    k=start #count of merged array

    while i<len1 and j<len2 :
        if L1[i]<=L2[j] :
            arr[k]=L1[i]
            i=i+1
        else :
            arr[k]=L2[j]
            j=j+1
        k=k+1

    while i < len1 :
        arr[k]=L1[i]
        i=i+1
        k=k+1

    while j< len2 :
        arr[k]=L2[j]
        j=j+1
        k=k+1


def Mergesort(arr,start,end):
    m=(start+(end-1))/2
    if start < end :
        Mergesort(arr,start,m)
        Mergesort(arr,m+1,end)
        Merge(arr,start,m,end)





arr=[60,75,30,80,40,90,120,70]
l=len(arr)
Mergesort(arr,0,l-1)
print arr