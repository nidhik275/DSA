class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, newNode):
        """Inserts a new node at the end of the linked list."""
        if self.head is None:
            self.head = newNode
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = newNode

    def insertHead(self, newHead):
        """Inserts a new node at the beginning of the linked list."""
        newHead.next = self.head
        self.head = newHead

    def insertIndex(self, midNode, index):
        """Inserts a new node at a specific index in the linked list.

        Args:
            midNode: The node to be inserted.
            index: The index at which to insert the node (0-based).

        Raises:
            ValueError: If the index is out of bounds.
        """
        if index < 0:
            raise ValueError("Index cannot be negative")

        if index == 0:
            self.insertHead(midNode)  # Efficiently use insertHead for index 0
        else:
            i = 0
            temp = self.head
            while i < index - 1 and temp is not None:  # Handle potential out-of-bounds errors
                temp = temp.next
                i += 1

            if temp is None:  # Index out of bounds
                raise ValueError("Index out of range")

            nextnode = temp.next
            temp.next = midNode
            midNode.next = nextnode

    def printList(self):
        """Prints the data of each node in the linked list."""
        if self.head is None:
            print("List is empty")
            return

        current = self.head
        while current is not None:
            print(current.data, end=" -> ")  # Print with arrows for better visualization
            current = current.next
        print("None")  # Indicate the end of the list

linkedlist = LinkedList()
firstNode = Node("A")
secondNode = Node("B")
thirdNode = Node("C")

linkedlist.insertHead(firstNode)
linkedlist.insertHead(secondNode)
linkedlist.insertHead(thirdNode)

linkedlist.printList()