class Node:
    """
    Node object for Doubly Linked List structure.
    """

    def __init__(self, element=None, previous=None, next=None):
        """
        Creates a new Node object.
        :param element: Element that is inside the Node.
        :param previous: Node that comes before this Node.
        :param next: Node that comes after this Node.
        """
        # Set internal state
        self.element = element
        self.previous = previous
        self.next = next

    def get_element(self):
        """
        Gets the element in the Node.
        :return: Element in the Node.
        """
        return self.element

    def set_element(self, element):
        """
        Sets the element in the Node.
        :param element: New element to put in the Node.
        """
        self.element = element

    def get_previous(self):
        """
        Gets the Node before this Node.
        :return: The Node before this Node.
        """
        return self.previous

    def set_previous(self, previous):
        """
        Sets a New Node before this Node.
        :param previous: The new Node before this Node.
        """
        self.previous = previous

    def get_next(self):
        """
        Gets the Node after this Node.
        :return: The Node after this Node.
        """
        return self.next

    def set_next(self, next):
        """
        Sets a new Node after this Node.
        :param next: The new Node after this Node.
        """
        self.next = next
