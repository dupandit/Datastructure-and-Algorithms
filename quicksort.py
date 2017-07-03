import sys
sys.setrecursionlimit(1500)

def partition(arr,start,end):
    pivot=arr[end]
    print 'Before Partition : ',arr
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
    print 'After partition :',arr
    print 'index : ',i+1
    return i+1



def Quicksort(arr,low,high):
    print "Our array is : ", arr
    if low < high or len(arr)<=1 :
        l=len(arr)
        index=partition(arr,low,high)
        #print index,arr,'1'
        Quicksort(arr,low,index-1)
        #l=len(arr)
        #print index,arr,'2'
        Quicksort(arr,index+1,high)






#while True :
#    x=raw_input('Enter number and type done at the end\n')
#    if x == 'done':
#        break
#    else :
#       arr.append(int(x))
#l=len(arr)
arr=[60,75,30,80,40,90,120,70]
l=len(arr)
Quicksort(arr,0,l-1)
print arr
#partition(arr,arr[l-1])
