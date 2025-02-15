import unittest


import unittest
from my_set import My_Set



class MySet(unittest.TestCase):

    def test_is_empty(self):
        my_set = My_Set()
        self.assertTrue(my_set.is_Empthy())

    def test_is_full(self):
        my_set = My_Set()
        self.assertFalse(my_set.isFull())

    def test_to_add_element(self):
        my_set = My_Set()
        my_set.add(1)
        my_set.add(2)
        self.assertEqual(my_set.getElement(), {1,2})

    def test_that_add_duplicate_element(self):
        my_set = My_Set()
        my_set.add("fish")
        my_set.add("fish")
        self.assertEqual(my_set.getElement(), {"fish"})

    def test_that_update_element(self):
        my_set = My_Set()
        my_set.add(1)
        my_set.add(2)
        my_set.add("fish")
        new_element = (1,2,2,"fish","Chicken")
        my_set.update( new_element)
        self.assertEqual(my_set.getElement(), {1, 2, "fish", "Chicken"})

    def test_intersection_element(self):
       my_set = My_Set()
       my_set.add(1)
       my_set.add(2)
       # my_set.add("fish")
       my_set.add("fish")
       new_element = My_Set()
       new_element.add("fish")
       new_element.add(1)
       new_element.add(2)
       result = my_set.intersection(new_element)
       self.assertEqual(result, {"fish",1,2})



if __name__ == '__main__':
    unittest.main()
