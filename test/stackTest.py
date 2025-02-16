import unittest
from stack import Stack

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.my_stack = Stack()

    def test_that_is_empthy(self):
        self.assertTrue(self.my_stack.isEmpty())

    def test_that_push_element(self):
        item = 1
        self.my_stack.push(item)
        self.assertEqual(self.my_stack.items, [item])

    def test_that_push_multiple_elements(self):
        items = [1,2,3,4]
        for item in items:
            self.my_stack.push(item)
        self.assertEqual(self.my_stack.items, items)

    def test_that_pop_element(self):
        item = 1
        self.my_stack.push(item)
        self.assertEqual(self.my_stack.pop(), item)

    def test_that_pop_multiple_elements(self):
        items = [1,2,3,4]
        for item in items:
            self.my_stack.push(item)
            self.assertEqual(self.my_stack.pop(), item)


if __name__ == '__main__':
    unittest.main()
