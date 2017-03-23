""" Method which returns partition index for each part
 For each time the partition sorts according to it's pivote value
 i.e numbers less than pivoe will be arranges on left to the pivote
 numbers grater than pivote will be arrange on right to the pivote
 since for each time pivote placed at sorted index hence partition index exactly the pivote position"""

def partitionndex(a,start,end):
	pivote = end
	tracker = start
	for i in range(start,end):          #iteration should be in between start and end, not to range(len(a)) 
		if a[i] < a[pivote]:
			a[tracker],a[i] = a[i], a[tracker]
			tracker += 1
	a[tracker],a[pivote] = a[pivote],a[tracker]
	return tracker
""" Recursive method to call each remaining part after pivote has set to its position"""
def sortQuick(a,start,end):
	if start < end:
		value = partitionndex(a,start,end)
		sortQuick(a,start, value-1)
		sortQuick(a,value+1, end)
a = [5,2,78,11,3,1,15,19,39]
sortQuick(a,0,len(a)-1)
print a
