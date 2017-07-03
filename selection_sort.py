def Selection_Sort(unsorted_arr):
    sorted_arr=[]
    l=len(unsorted_arr)
    while l!=len(sorted_arr) :
        temp = 999999999999
        t=0
        for i in unsorted_arr :
            if i < temp :
                temp = i
                index=t
            t=t+1
        sorted_arr.append(temp)
        del unsorted_arr[index]
    return sorted_arr

arr=[]
while True :
    x=raw_input('Enter number and type done at the end\n')
    if x == 'done':
        break
    else :
        arr.append(int(x))
print arr,Selection_Sort(arr)