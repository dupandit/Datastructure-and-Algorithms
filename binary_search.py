def binarysearch(arr,x) :
	l=len(arr)
	if l%2==0 : 
		mid=(l/2)-1
	else :
		mid=(l-1)/2
	
	if l>=1 : 
		if x==arr[mid] :
			return "Found"
		if x>arr[mid] : 
			return binarysearch(arr[mid+1:l],x)
		else :
			return binarysearch(arr[0:mid],x)
	else : 
		return "Not found"
	
x=[2,3,5,6,8,11,15]
y=int(raw_input('Enter:\n'))
print binarysearch(x,y)