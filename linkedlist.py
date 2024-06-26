# create linked list
#insert element in a linked list
#print linked list

class Node:
	def __init__ (self, data: str):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def insertEnd(self, newNode):
		if self.head is None: #firstnode
			self.head = newNode
			
		else:
			currentNode = self.head
			while currentNode.next!= None:
				if currentNode.next is None:
					break
				currentNode = currentNode.next
			currentNode.next = newNode

	def insertHead(self,newHead):
		tempHead = self.head
		self.head = newHead
		newHead.next = tempHead

	#def (self, )

	def print(self):
		currentNode = self.head
		while True:
			if currentNode is None:
				break
			print(currentNode.data)
			currentNode = currentNode.next

firstNode = Node ("first")
linkedlist = LinkedList()
linkedlist.insertEnd(firstNode)

secondNode = Node("second")
linkedlist.insertEnd(secondNode)

newHeadNode = Node("New first")
linkedlist.insertHead(newHeadNode)

linkedlist.print()
