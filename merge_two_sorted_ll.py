class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def insert(self, newNode):
		if self.head == None:
			self.head = newNode
		else:
			temp_var = self.head
			while temp_var.next != None:
				temp_var = temp_var. next
			temp_var.next = newNode

	def printList(self):
		if self.head is None:
			print("LinkedList is empty")
			return
		currentNode = self.head
		while currentNode is not None:
			print(currentNode.data)
			currentNode = currentNode.next

	#def mergeLinkedList(self,node1, node2)



firstNode = Node(2)
secondNode = Node(5)
thirdNode = Node(6)

#initialise linkedlist1 object of class LinkedList
linkedlist1 = LinkedList()

#insert elements first linked list
linkedlist1.insert(firstNode)
linkedlist1.insert(secondNode)
linkedlist1.insert(thirdNode)

firstNode2 = Node(1)
secondNode2 = Node(3)
thirdNode2 = Node(10)
fourthNode2= Node(12)

#initialise linkedlist1 object of class LinkedList
linkedlist2 = LinkedList()

#insert elements first linked list
linkedlist2.insert(firstNode)
linkedlist2.insert(secondNode)
linkedlist2.insert(thirdNode)


linkedlist1.printList()
linkedlist2.printList()