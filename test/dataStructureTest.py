import unittest
from dataStructure import DataStructure


class myList(unittest.TestCase):



    def test_isEmpty(self):
        dataStructure= DataStructure([])
        self.assertTrue(dataStructure.isEmpty())

    def test_isFull(self):
        dataStructure= DataStructure(3)
        self.assertFalse(dataStructure.isFull())

    def test_to_appemd_element(self):
        dataStructure= DataStructure(3)
        dataStructure.append(1)
        dataStructure.append(2)
        self.assertFalse(dataStructure.isFull())

    def test_the_list_isFull(self):
        dataStructure= DataStructure(3)
        dataStructure.append(1)
        dataStructure.append(2)
        dataStructure.append(3)
        self.assertTrue(dataStructure.isFull())

    def test_to_remove_element(self):
        dataStructure= DataStructure(3)
        dataStructure.append(1)
        dataStructure.append(2)
        dataStructure.append(3)
        dataStructure.remove(1)
        self.assertTrue(dataStructure.size == 2)

    def test_to_pop_element(self):
        dataStructure= DataStructure(3)
        dataStructure.append(1)
        dataStructure.append(2)
        dataStructure.append(3)
        dataStructure.pop(1)
        self.assertFalse(dataStructure.isFull())

    def test_insert_element(self):
        dataStructure= DataStructure(3)
        dataStructure.append(1)
        dataStructure.append(2)
        dataStructure.append(3)
        dataStructure.insert(3,4)
        self.assertTrue(dataStructure.size == 3)
        dataStructure.insert(3,5)
        self.assertTrue(dataStructure.size == 3)





if __name__ == '__main__':
    unittest.main()
