n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))
count = 0
sorted= False
while sorted == False :
    ## Track number of elements swapped during a single array traversal
    numberofSwaps = 0
    
    for j in range(n-1) :
        ##Swap adjacent elements if they are in decreasing order
        print n
        if (a[j] > a[j + 1]) : 
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
            count = count + 1
            numberofSwaps=numberofSwaps+1
        
    
    ##If no elements were swapped during a traversal, array is sorted
    if (numberofSwaps == 0) :
        sorted = True
		
print a