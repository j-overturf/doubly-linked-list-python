class Node:
    """
    Node object for Linked List structure.
    """

    def __init__(self, element=None, before=None, after=None):
        """
        Creates a new Node object.
        :param element: Element that is inside the Node.
        :param before: Node that comes before this Node.
        :param after: Node that comes after this Node.
        """
        # Set internal state
        self.element = element
        self.before = before
        self.after = after

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

    def get_before(self):
        """
        Gets the Node before this Node.
        :return: The Node before this Node.
        """
        return self.before

    def set_before(self, before):
        """
        Sets a New Node before this Node.
        :param before: The new Node before this Node.
        """
        self.before = before

    def get_after(self):
        """
        Gets the Node after this Node.
        :return: The Node after this Node.
        """
        return self.after

    def set_after(self, after):
        """
        Sets a new Node after this Node.
        :param after: The new Node after this Node.
        """
        self.after = after
