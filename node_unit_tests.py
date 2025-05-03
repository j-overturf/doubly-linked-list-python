import unittest
from node import *


class NodeUnitTests(unittest.TestCase):
    """
    Unit test cases for the Node object in node.py
    """

    def test_ctor_noParams(self):
        """
        Creates a new node with nothing provided.
        :return: True if the internal state of the Node is none.
        """
        new = Node()

        # Check internal state
        self.assertIsNone(new.get_element(), None)
        self.assertIsNone(new.get_before(), None)
        self.assertIsNone(new.get_after(), None)

    def test_ctor_elementParam(self):
        """
        Creates a new node with only the element provided.
        :return: True if the internal state of the Node matches the constructor.
        """
        new = Node("hello")

        # Check internal state
        self.assertTrue(new.get_element(), "hello")
        self.assertIsNone(new.get_before(), None)
        self.assertIsNone(new.get_after(), None)

    def test_ctor_elementAndBeforeParam(self):
        """
        Creates a new node with the element and before provided.
        :return: True if the internal state of the Node matches the constructor.
        """
        before = Node(0)
        new = Node("hello", before)

        # Check internal state
        self.assertTrue(new.get_element(), "hello")
        self.assertTrue(new.get_before(), before)
        self.assertIsNone(new.get_after(), None)

    def test_ctor_allParams(self):
        """
        Creates a new node with all parameters provided.
        :return: True if the internal state of the Node matches the constructor.
        """
        before = Node(0)
        after = Node(100)
        new = Node("hello", before, after)

        # Check internal state
        self.assertTrue(new.get_element(), "hello")
        self.assertTrue(new.get_before(), before)
        self.assertTrue(new.get_after(), after)

    def test_get_element(self):
        """
        Returns the correct element from the Node provided.
        :return: True if the element returned is correct.
        """
        # Create node
        new = Node(10)

        # Check assertion
        self.assertTrue(new.get_element(), 10)

    def test_set_element(self):
        """
        Sets a new element for the Node object.
        :return: True if the new element is returned.
        """
        # Create node
        new = Node(10)

        new.set_element(100)

        # Check assertion
        self.assertTrue(new.get_element(), 100)

    def test_get_before(self):
        """
        Returns the correct before Node from the Node provided.
        :return: True if the Node returned is correct.
        """
        # Create node
        new = Node(10)
        before = Node(8, new)

        # Check assertion
        self.assertTrue(before.get_before(), new)

    def test_set_before(self):
        """
        Sets a new element for the Node object.
        :return: True if the new element is returned.
        """
        # Create node
        new = Node(10)
        before = Node(8)

        before.set_before(new)

        # Check assertion
        self.assertTrue(before.get_before(), new)

    def test_get_after(self):
        """
        Returns the correct after Node from the Node provided.
        :return: True if the Node returned is correct.
        """
        # Create node
        new = Node(10)
        before = Node(8)

        before.set_after(new)

        # Check assertion
        self.assertTrue(before.get_after(), new)

    def test_set_after(self):
        """
        Sets a new element for the Node object.
        :return: True if the new element is returned.
        """
        # Create node
        new = Node(10)
        before = Node(8)

        before.set_after(new)

        # Check assertion
        self.assertTrue(before.get_after(), new)


if __name__ == '__main__':
    unittest.main()
