import unittest
from my_array import MyArray

class MyTestCase(unittest.TestCase):
    def test_my_array_isEmpty(self):
        my_array = MyArray([])
        self.assertTrue(my_array.is_empty())

    def test_my_array_is_full(self):
        my_array = MyArray(5)
        self.assertTrue(my_array.is_full())




if __name__ == '__main__':
    unittest.main()
