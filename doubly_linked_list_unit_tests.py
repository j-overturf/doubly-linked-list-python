import unittest
from doubly_linked_list import *
from node import *


class DoublyLinkedListUnitTests(unittest.TestCase):
    """
    Unit test cases for the Doubly Linked List structure in doubly_linked_list.py
    """

    def test_ctor(self):
        """
        Test constructing a new Doubly Linked List.
        """
        linked_list = DoublyLinkedList()

    def test_append_empty(self):
        """
        Appends a new node to an empty doubly linked list.
        :return: True if the node was appended correctly.
        """
        # Node
        new_node = Node(10)

        # List
        linked_list = DoublyLinkedList()

        # Append
        linked_list.append(new_node)

        # Check if the node was appended correctly
        self.assertEqual(linked_list.size(), 1)
        self.assertEqual(linked_list.get_head(), new_node)
        self.assertEqual(linked_list.get_tail(), new_node)

    def test_append_notEmpty(self):
        """
        Appends a new node to a non-empty doubly linked list.
        :return: True if the node was appended correctly.
        """
        # Node
        first_node = Node(30)
        new_node = Node(10)

        # List
        linked_list = DoublyLinkedList()

        # Append
        linked_list.append(first_node)
        linked_list.append(new_node)

        # Check if the node was appended correctly
        self.assertEqual(linked_list.size(), 2)
        self.assertEqual(linked_list.get_head(), first_node)
        self.assertEqual(linked_list.get_tail(), new_node)

    def test_append_invalidNode(self):
        """
        Appends an invalid node to a doubly linked list.
        :return: True if the node was appended correctly.
        """
        # Node
        first_node = Node(30)
        new_node = None

        # List
        linked_list = DoublyLinkedList()

        # Append
        linked_list.append(first_node)

        # Error raised because the node is none
        with self.assertRaises(TypeError):
            linked_list.append(new_node)

    def test_prepend_empty(self):
        """
        Prepends a new node to an empty doubly linked list.
        :return: True if the node was prepended correctly.
        """
        # Node
        new_node = Node(10)

        # List
        linked_list = DoublyLinkedList()

        # Append
        linked_list.prepend(new_node)

        # Check if the node was appended correctly
        self.assertEqual(linked_list.size(), 1)
        self.assertEqual(linked_list.get_head(), new_node)
        self.assertEqual(linked_list.get_tail(), new_node)

    def test_prepend_notEmpty(self):
        """
        Prepends a new node to a non-empty doubly linked list.
        :return: True if the node was prepended correctly.
        """
        # Node
        first_node = Node(30)
        new_node = Node(10)

        # List
        linked_list = DoublyLinkedList()

        # Append
        linked_list.prepend(first_node)
        linked_list.prepend(new_node)

        # Check if the node was appended correctly
        self.assertEqual(linked_list.size(), 2)
        self.assertEqual(linked_list.get_head(), new_node)
        self.assertEqual(linked_list.get_tail(), first_node)

    def test_prepend_invalidNode(self):
        """
        Prepends an invalid node to a doubly linked list.
        :return: Error because the value cannot be prepended.
        """
        # Node
        first_node = Node(30)
        new_node = None

        # List
        linked_list = DoublyLinkedList()

        # Append
        linked_list.append(first_node)

        # Error raised because the node is none
        with self.assertRaises(TypeError):
            linked_list.prepend(new_node)

    def test_insert(self):
        """
        Inserts a new node to a non-empty doubly linked list.
        :return: Passes if the node was inserted correctly.
        """
        # Node
        first_node = Node(30)
        second_node = Node(60)
        third_node = Node("hello")
        fourth_node = Node("foo")
        fifth_node = Node("124")
        new_node = Node(10)

        # List
        linked_list = DoublyLinkedList()

        # Append
        linked_list.append(first_node)
        linked_list.append(second_node)
        linked_list.append(third_node)
        linked_list.append(fourth_node)
        linked_list.append(fifth_node)
        linked_list.insert(new_node, 1)

        # Check if the node was appended correctly
        self.assertEqual(linked_list.size(), 6)
        self.assertEqual(linked_list.get_head(), first_node)
        self.assertEqual(linked_list.get_tail(), fifth_node)

    def test_insert_invalidIndex(self):
        """
        Inserts a new node with an invalid index to a non-empty doubly linked list.
        :return: An error because the index is invalid.
        """
        # Node
        first_node = Node(30)
        second_node = Node(60)
        third_node = Node("hello")
        new_node = Node(10)

        # List
        linked_list = DoublyLinkedList()

        # Append
        linked_list.append(first_node)
        linked_list.append(second_node)
        linked_list.append(third_node)

        # Error raised because the index is too high
        with self.assertRaises(IndexError):
            linked_list.insert(new_node, 10)

    def test_insert_negativeIndex(self):
        """
        Inserts a new node with a negative index to a non-empty doubly linked list.
        :return: An error because the index is negative.
        """
        # Node
        first_node = Node(30)
        second_node = Node(60)
        third_node = Node("hello")
        new_node = Node(10)

        # List
        linked_list = DoublyLinkedList()

        # Append
        linked_list.append(first_node)
        linked_list.append(second_node)
        linked_list.append(third_node)

        # Error raised because the index is negative
        with self.assertRaises(IndexError):
            linked_list.insert(new_node, -5)

    def test_insert_invalidNode(self):
        """
        Inserts a new node with a negative index to a non-empty doubly linked list.
        :return: An error because the index is negative.
        """
        # Node
        first_node = Node(30)
        second_node = Node(60)
        third_node = Node("hello")

        # List
        linked_list = DoublyLinkedList()

        # Append
        linked_list.append(first_node)
        linked_list.append(second_node)
        linked_list.append(third_node)

        # Error raised because the node is not valid
        with self.assertRaises(TypeError):
            linked_list.insert(10, 1)

    def test_size(self):
        """
        Get the size of the non-empty doubly linked list.
        """
        # Node
        first_node = Node(30)
        second_node = Node(60)
        third_node = Node("hello")

        # List
        linked_list = DoublyLinkedList()

        # Append
        linked_list.append(first_node)
        linked_list.append(second_node)
        linked_list.append(third_node)

        self.assertEqual(linked_list.size(), 3)

    def test_size_empty(self):
        """
        Get the size of the empty doubly linked list.
        """
        # List
        linked_list = DoublyLinkedList()

        self.assertEqual(linked_list.size(), 0)

    def test_clear(self):
        """
        Clear the non-empty doubly linked list.
        """
        # Node
        first_node = Node(30)
        second_node = Node(60)
        third_node = Node("hello")

        # List
        linked_list = DoublyLinkedList()

        # Append
        linked_list.append(first_node)
        linked_list.append(second_node)
        linked_list.append(third_node)

        linked_list.clear()

        self.assertEqual(linked_list.size(), 0)
        self.assertEqual(linked_list.get_head(), None)
        self.assertEqual(linked_list.get_tail(), None)

    def test_empty_isEmpty(self):
        """
        Check if the empty doubly linked list is empty.
        """
        # List
        linked_list = DoublyLinkedList()

        self.assertTrue(linked_list.empty())

    def test_empty_notEmpty(self):
        """
        Check if the not empty doubly linked list is not empty.
        """
        # Node
        first_node = Node(30)
        second_node = Node(60)
        third_node = Node("hello")

        # List
        linked_list = DoublyLinkedList()

        # Append
        linked_list.append(first_node)
        linked_list.append(second_node)
        linked_list.append(third_node)

        self.assertFalse(linked_list.empty())

    def test_contains_doesContain(self):
        """
        Check if the doubly linked list contains the element.
        """
        # Node
        first_node = Node(30)
        second_node = Node(60)
        third_node = Node("hello")

        # List
        linked_list = DoublyLinkedList()

        # Append
        linked_list.append(first_node)
        linked_list.append(second_node)
        linked_list.append(third_node)

        self.assertTrue(linked_list.contains(60))

    def test_contains_doesNotContain(self):
        """
        Check if the doubly linked list does not contain the element.
        """
        # Node
        first_node = Node(30)
        second_node = Node(60)
        third_node = Node("hello")

        # List
        linked_list = DoublyLinkedList()

        # Append
        linked_list.append(first_node)
        linked_list.append(second_node)
        linked_list.append(third_node)

        self.assertFalse(linked_list.contains(10))

    def test_get_canGet(self):
        """
        Gets the first node in the doubly linked list that has a specific element.
        """
        # Node
        first_node = Node(30)
        second_node = Node(60)
        third_node = Node("hello")

        # List
        linked_list = DoublyLinkedList()

        # Append
        linked_list.append(first_node)
        linked_list.append(second_node)
        linked_list.append(third_node)

        self.assertEqual(linked_list.get(60), second_node)

    def test_get_cannotGet(self):
        """
        Gets the first node in the doubly linked list that has a specific element.
        """
        # Node
        first_node = Node(30)
        second_node = Node(60)
        third_node = Node("hello")

        # List
        linked_list = DoublyLinkedList()

        # Append
        linked_list.append(first_node)
        linked_list.append(second_node)
        linked_list.append(third_node)

        self.assertEqual(linked_list.get(10), None)

    def test_pop(self):
        """
        Removes the first node from doubly linked list.
        """
        # Node
        first_node = Node(30)
        second_node = Node(60)
        third_node = Node("hello")

        # List
        linked_list = DoublyLinkedList()

        # Append
        linked_list.append(first_node)
        linked_list.append(second_node)
        linked_list.append(third_node)

        linked_list.pop()

        self.assertEqual(linked_list.get_head(), second_node)
        self.assertEqual(linked_list.size(), 2)

    def test_pop_empty(self):
        """
        Removes the first node from an empty doubly linked list.
        """
        # List
        linked_list = DoublyLinkedList()

        with self.assertRaises(IndexError):
            linked_list.pop()

    def test_pop_back(self):
        """
        Removes the last node from a doubly linked list.
        """
        # Node
        first_node = Node(30)
        second_node = Node(60)
        third_node = Node("hello")

        # List
        linked_list = DoublyLinkedList()

        # Append
        linked_list.append(first_node)
        linked_list.append(second_node)
        linked_list.append(third_node)

        linked_list.pop_back()

        self.assertEqual(linked_list.get_tail(), second_node)
        self.assertEqual(linked_list.size(), 2)

    def test_pop_back_empty(self):
        """
        Removes the last node from an empty doubly linked list.
        """
        # List
        linked_list = DoublyLinkedList()

        with self.assertRaises(IndexError):
            linked_list.pop_back()

    def test_remove_head(self):
        """
        Removes the head from the doubly linked list.
        """
        # Node
        first_node = Node(30)
        second_node = Node(60)
        third_node = Node("hello")

        # List
        linked_list = DoublyLinkedList()

        # Append
        linked_list.append(first_node)
        linked_list.append(second_node)
        linked_list.append(third_node)

        self.assertEqual(linked_list.remove(0), first_node)
        self.assertEqual(linked_list.size(), 2)
        self.assertEqual(linked_list.get_head(), second_node)

    def test_remove_tail(self):
        """
        Removes the tail from the doubly linked list.
        """
        # Node
        first_node = Node(30)
        second_node = Node(60)
        third_node = Node("hello")

        # List
        linked_list = DoublyLinkedList()

        # Append
        linked_list.append(first_node)
        linked_list.append(second_node)
        linked_list.append(third_node)

        self.assertEqual(linked_list.remove(2), third_node)
        self.assertEqual(linked_list.size(), 2)
        self.assertEqual(linked_list.get_tail(), second_node)

    def test_remove(self):
        """
        Removes a node from a specific index in doubly linked list.
        """
        # Node
        first_node = Node(30)
        second_node = Node(60)
        third_node = Node("hello")

        # List
        linked_list = DoublyLinkedList()

        # Append
        linked_list.append(first_node)
        linked_list.append(second_node)
        linked_list.append(third_node)

        self.assertEqual(linked_list.remove(1), second_node)
        self.assertEqual(linked_list.size(), 2)
        self.assertEqual(linked_list.get_head(), first_node)
        self.assertEqual(linked_list.get_tail(), third_node)

    def test_remove_invalidIndex(self):
        """
        Removes a node at an invalid index from the doubly linked list.
        """
        # Node
        first_node = Node(30)
        second_node = Node(60)
        third_node = Node("hello")

        # List
        linked_list = DoublyLinkedList()

        # Append
        linked_list.append(first_node)
        linked_list.append(second_node)
        linked_list.append(third_node)

        with self.assertRaises(IndexError):
            linked_list.remove(5)

    def test_remove_negativeIndex(self):
        """
        Removes a node at a negative index from the doubly linked list.
        """
        # Node
        first_node = Node(30)
        second_node = Node(60)
        third_node = Node("hello")

        # List
        linked_list = DoublyLinkedList()

        # Append
        linked_list.append(first_node)
        linked_list.append(second_node)
        linked_list.append(third_node)

        with self.assertRaises(IndexError):
            linked_list.remove(-4)

    def test_get_head(self):
        """
        Gets the head of the doubly linked list.
        """
        # Node
        first_node = Node(30)
        second_node = Node(60)
        third_node = Node("hello")

        # List
        linked_list = DoublyLinkedList()

        # Append
        linked_list.append(first_node)
        linked_list.append(second_node)
        linked_list.append(third_node)

        self.assertEqual(linked_list.get_head(), first_node)

    def test_get_tail(self):
        """
        Gets the tail of the doubly linked list.
        """
        # List
        linked_list = DoublyLinkedList()

        # Node
        first_node = Node(30)
        second_node = Node(60)
        third_node = Node("hello")

        # List
        linked_list = DoublyLinkedList()

        # Append
        linked_list.append(first_node)
        linked_list.append(second_node)
        linked_list.append(third_node)

        self.assertEqual(linked_list.get_tail(), third_node)

    def test_str(self):
        """
        Gets the string output of the doubly linked list.
        """
        # List
        linked_list = DoublyLinkedList()

        # Node
        first_node = Node(30)
        second_node = Node(60)
        third_node = Node("hello")

        # List
        linked_list = DoublyLinkedList()

        # Append
        linked_list.append(first_node)
        linked_list.append(second_node)
        linked_list.append(third_node)

        self.assertEqual(linked_list.__str__(), "30 - 60 - hello")


if __name__ == '__main__':
    unittest.main()
