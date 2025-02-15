import unittest
from list import List


class myList(unittest.TestCase):



    def test_isEmpty(self):
        list = List([])
        self.assertTrue(list.isEmpty())

    def test_isFull(self):
        list = List(3)
        self.assertFalse(list.isFull())

    def test_to_appemd_element(self):
        list = List(3)
        list.append(1)
        list.append(2)
        self.assertFalse(list.isFull())

    def test_the_list_isFull(self):
        list = List(3)
        list.append(1)
        list.append(2)
        list.append(3)
        self.assertTrue(list.isFull())

    def test_to_remove_element(self):
        list = List(3)
        list.append(1)
        list.append(2)
        list.append(3)
        list.remove(1)
        self.assertTrue(list.size == 2)

    def test_to_pop_element(self):
        list = List(3)
        list.append(1)
        list.append(2)
        list.append(3)
        list.pop(1)
        self.assertFalse(list.isFull())

    def test_insert_element(self):
        list = List(3)
        list.append(1)
        list.append(2)
        list.append(3)
        list.insert(3,4)
        self.assertTrue(list.size == 3)
        list.insert(3,5)
        self.assertTrue(list.size == 3)





if __name__ == '__main__':
    unittest.main()
