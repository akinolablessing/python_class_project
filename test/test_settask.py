import unittest
from settask import sort_numbers
from unittest import expectedFailure

import settask


#class TestTask(unittest.TestCase):
   # def test_that_function_(self):




#class TestSimpleRotCipher(unittest.TestCase):
   # def test_that_simple_rot_cipher(self):
       # assert(settask.cipher("Uryyb, jbeyq!"))

#ArrayListInPython

#class Test
#class TestTask2(unittest.TestCase):
    #def test_that_simple_rot_cipher_function_(self):
       # actual = change_char_values('hello')
        #expected = 'uryyb'
        #self.assertEqual(actual, expected)




class TestThatSortNumbers(unittest.TestCase):
    def test_sort_numbers(self):
        elements = [2,6,7,10]
        actual = settask.sort_numbers(elements)
        expected = [2,6,7,10]
        self.assertEqual(actual, expected)

class TestThatSortletter(unittest.TestCase):
    def test_sort_letter(self):
        elements = ['a', 'd', 'b', 'c']
        actual = settask.sort_letter(elements)
        expected = ['a', 'b', 'c', 'd']
        self.assertEqual(actual,expected)

if __name__ == '__main__':
    unittest.main()
