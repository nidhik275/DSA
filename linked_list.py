class Node:
	def __init__(self):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def insert(self, newNode):
		if self.head == None:	
			self.head = newNode 
		else:
			temp = self.head 
			while temp.next!= None:
				temp = temp.next
			#while True:
			#	if lastNode.next is None:
			#		break
			temp = temp.next
			#temp.next = newNode

	def insertHead(self, newHead):
		newHead.next = self.head
		self.head = newNode

	def insertIndex(self, midNode, index):
		if index == 0:	#if a new headnode is inserted
			insertHead(midNode)
		else:
			i=0
			temp = self.head
			while i < index -1:
				temp = temp.next
				i= i+1
			nextnode = temp.next
			temp.next = midNode
			midNode.next = nextnode

	def printList(self):
	    """Prints the data of each node in the linked list."""
	    if self.head is None:
	    	print("List is empty")
            # return

        current = self.head
        while current is not None:
            print(current.data, end=" -> ")  # Print with arrows for better visualization
            current = current.next
        print("None")  # Indicate the end of the list

linkedlist = LinkedList()
firstNode = Node("A")

linkedlist.insertHead(firstNode)

linkedlist.printList()









 