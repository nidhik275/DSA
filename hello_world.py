class Node:
		def __init__(self, data):
			self.data = data 
			self.next = None


class LinkedList:
		def __init__(self):
			self.head = None

		def insertNode(self, newNode):
			#newNode = Node(newNode)
			if self.head is None:
				self.head = newNode
			else:
				lastNode = self.head
				while True:
					if lastNode.next is None:
						break
					lastNode = lastNode.next 
				lastNode.next = newNode

		def printList(self):
			if self.head is None:
				print("List is empty")
				return

			currentNode = self.head
			while True:
				if currentNode is None:
					break
				print(currentNode.data)
				currentNode = currentNode.next

firstNode = Node("A")
linkedList = LinkedList() # initially empty linkedlist

linkedList.insertNode(firstNode)

#first, create a node 
#second, insert that node to Linked list 
secondNode = Node("B")
linkedList.insertNode(secondNode)

thirdNode = Node("C")
linkedList.insertNode(thirdNode)

linkedList.printList()