class Node:
	def __init__(self,val=None,next=None):
		self.val = val
		self.next = next
	def setnext(self,nex):
		self.next = nex
	def getVal(self):
		return self.val
	def getNext(self):
		return self.next

class LinkedList:
	def __init__(self,head=None,trac=None):
		self.head=head
		self.trac = None
	def formLL(self,value):
		if self.head == None:
			obj = Node(val=value)
			self.head = obj
			self.trac = self.head
		else:
			obj = Node(val = value)
			self.trac.setnext(obj)
			self.trac = obj
	def printl(self):
		ob = self.head;
		while ob!=None:
			print ob.getVal()
			ob = ob.getNext()

a = [1,2,3,4,5,6]
obj = LinkedList()
for i in range(len(a)):
	obj.formLL(a[i])
obj.printl()