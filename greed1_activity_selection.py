def partition(arr,start,end):
    l=len(arr)
    pivot=arr[end]
    #print 'Before Partition : ',arr
    i=start-1
    j=start
    while j < l:
        if arr[j]>=pivot :
            pass
        else :
            i=i+1
            arr[i],arr[j]=arr[j],arr[i]
        j=j+1
    arr[i+1],arr[end]=arr[end],arr[i+1]
    #print 'After partition :',arr
    #print 'index : ',i+1
    return i+1



def Quicksort(arr,low,high):
    #print "Our array is : ", arr
    if low < high or len(arr)<=1 :
        l=len(arr)
        index=partition(arr,low,high)
        #print index,arr,'1'
        Quicksort(arr,low,index-1)
        #l=len(arr)
        #print index,arr,'2'
        Quicksort(arr,index+1,high)


def Activity_Select(start,finish):
    l=len(start)   # This gives the total number of activities
    d={}
    for i in range(l):
        d[finish[i]]=start[i]           # Dictionary containing mapping of start and finish times 'finish:start'
    arr=finish
    Quicksort(arr,0,l-1)               # Sort the finish array in ascending order
    finish=arr
    #print finish
    print d
    final_arr=[]
    final_arr.append(0)                     # In Greedy approach we choose the first activity and greedily select next activities, so we add first activity i.e. index 0
    current=0                           # Current is the index which is already added to our final activity list and where its finishing time  to be compared to next activity starting times
    for i in range(1,l):
        if d[finish[i]]>finish[current]:
            final_arr.append(i)
            current=i
    return final_arr



# Our main function
start=[1,3,0,5,8,5]
finish=[2,4,6,7,9,10]
print Activity_Select(start,finish)