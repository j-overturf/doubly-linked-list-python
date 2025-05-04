import math
from node import *


class DoublyLinkedList:
    """
    An implementation of the Doubly Linked List in Python.
    A doubly linked list is a linked list which can modify the head and tail of the linked list.
    """
    def __init__(self):
        """
        Constructs a new Doubly Linked List structure.
        """
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, node):
        """
        Appends a new node to the end of the Doubly Linked List.
        :param node: The new Node to be added to the end.
        """
        # Node cannot be anything other than a node object
        if not isinstance(node, Node):
            raise TypeError("Is not a node")

        # Before appending, check the state of the list
        # If the head is None then there are no elements
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            # Ensure structure completeness, the current tail must now attach to the new tail and vice versa
            current = self.tail
            current.set_after(node)
            node.set_before(current)

            # New tail
            self.tail = node

        # Increment size of list
        self.length += 1

    def prepend(self, node):
        """
        Appends a new node to the start of the Doubly Linked List.
        :param node: The new Node to be added to the front.
        """
        # Node cannot be anything other than a node object
        if not isinstance(node, Node):
            raise TypeError("Is not a node")

        # Before appending, check the state of the list
        # If the head is None then there are no elements
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            # Ensure structure completeness, the current head must now attach to the new head and vice versa
            current = self.head
            current.set_before(node)
            node.set_after(current)

            # New tail
            self.head = node

        # Increment size of list
        self.length += 1

    def insert(self, node, index):
        """
        Inserts a node at a specific index of the Doubly Linked List.
        :param node: The node to be inserted.
        :param index: The index to insert the node at.
        """
        # Check if the index is not greater than size and is not 0
        if index < 0 or index > self.size() - 1:
            raise IndexError("Index out of bounds")

        # Node cannot be anything other than a node object
        if not isinstance(node, Node):
            raise TypeError("Is not a node")

        # If the index is at 0 then call the correct method for this action
        if index == 0:
            self.prepend(node)
        else:
            # Determine best starting place based on current size
            middle = math.floor(self.size() / 2)
            # If the middle is greater than or equal to the index then start at the head
            if middle >= index:
                current = self.head
                # Iterate through list until desired index is reached
                for i in range(index):
                    current = current.get_after()
            else:
                current = self.tail
                # Calculate index for this operation to function correctly
                new_index = (self.size() - 1) - index
                # Iterate through list until desired index is reached
                for i in range(new_index + 1):
                    current = current.get_before()

            # Add new node between current and current's after node
            node.set_before(current)
            node.set_after(current.get_after())

            current.get_after().set_before(node)
            current.set_after(node)

            # Increment size
            self.length += 1

    def size(self):
        """
        Returns the size of the Doubly Linked List.
        :return: Size of the Doubly Linked List.
        """
        return self.length

    def clear(self):
        """
        Clears the nodes of out of the Doubly Linked List.
        """
        # Clear the list by dropping the head and tail
        # The rest of the nodes will be garbage collected
        self.head = None
        self.tail = None
        self.length = 0

    def empty(self):
        """
        Checks if the Doubly Linked List is empty.
        :return: True if the Doubly Linked List is empty.
        """
        empty = False

        # True if the size is 0
        if self.size() == 0:
            empty = True

        return empty

    def contains(self, element):
        """
        Checks if the Doubly Linked List contains an element.
        :param element: The element to check for.
        :return: True if the element is inside the Doubly Linked List
        """
        contain = False

        # Iterate through Doubly Linked List starting at the head, until the current is none
        current = self.head
        while current is not None:
            # Check current's element
            if current.get_element() == element:
                contain = True
                # Turn current to None to avoid iterating through the rest of the list.
                current = None
            else:
                current = current.get_after()

        return contain

    def get(self, element):
        """
        Returns the first Node containing a specific element in the Doubly Linked List.
        :return: The first Node containing the element.
        """
        node = None

        # Iterate through Doubly Linked List starting at the head, until the current is none
        current = self.head
        while current is not None:
            # Check current's element
            if current.get_element() == element:
                node = current
                # Turn current to None to avoid iterating through the rest of the list.
                current = None
            else:
                current = current.get_after()

        return node

    def pop(self):
        """
        Removes the first Node in the Doubly Linked List.
        """
        # Pop only if the linked list is not empty
        if self.size() == 0:
            raise IndexError("Doubly linked list is empty")

        # Adjust the Node's internal state
        current = self.head
        before = current.get_after()
        current.set_after(None)

        # Check if the before exists, if it does not then we are dealing with the tail
        if before is not None:
            before.set_before(None)
        else:
            self.tail = None

        # Swap the head
        self.head = before

        # Adjust size
        self.length -= 1

    def pop_back(self):
        """
        Removes the last Node in the Doubly Linked List.
        """
        # Pop only if the linked list is not empty
        if self.size() == 0:
            raise IndexError("Doubly linked list is empty")

        # Adjust the Node's internal state
        current = self.tail
        before = current.get_before()
        current.set_before(None)

        # Check if the before exists, if it does not then we are dealing with the head
        if before is not None:
            before.set_after(None)
        else:
            self.head = None

        # Swap the tail
        self.tail = before

        # Adjust size
        self.length -= 1

    def remove(self, index):
        """
        Removes a Node of the Doubly Linked List at a specific index and returns the Node.
        :param index: The index to remove the Node at.
        :return: The removed Node.
        """
        removed = None
        # Check if the index is not greater than size and is not 0
        if index < 0 or index > self.size() - 1:
            raise IndexError("Index out of bounds")

        # If the index is at 0 or the tail then call the correct methods for this action
        if index == 0:
            removed = self.head
            self.pop()
        elif index == self.size() - 1:
            removed = self.tail
            self.pop_back()
        else:
            # Determine best starting place based on current size
            middle = math.floor(self.size() / 2)
            # If the middle is greater than or equal to the index then start at the head
            if middle >= index:
                current = self.head
                # Iterate through list until desired index is reached
                for i in range(index):
                    current = current.get_after()
            else:
                current = self.tail
                # Calculate index for this operation to function correctly
                new_index = (self.size() - 1) - index
                # Iterate through list until desired index is reached
                for i in range(new_index + 1):
                    current = current.get_before()

            # Adjust size
            self.length -= 1

            # Adjust the internal state of the current's before and after and return the current
            before = current.get_before()
            after = current.get_after()

            before.set_after(after)
            after.set_before(before)

            current.set_before(None)
            current.set_after(None)

            removed = current

        # Return the removed node
        return removed

    def get_head(self):
        """
        Returns the head of the Doubly Linked List.
        :return: The head of the Doubly Linked List.
        """
        return self.head

    def get_tail(self):
        """
        Returns the tail of the Doubly Linked List.
        :return: The tail of the Doubly Linked List.
        """
        return self.tail

    def __str__(self):
        """
        Returns a string of all the nodes based on linkage.
        :return: String of all nodes based on linkage.
        """
        output = ""
        current = self.head

        # Traverse entire list
        for i in range(self.size()-1):
            # Modify output based on after status
            if current.get_after() is not None:
                output += " - "
                output += str(current.get_element())
            else:
                output += str(current.get_element())
                output += " - "

            # Adjust current
            current = current.get_after()

        # Return the list string
        return output
    