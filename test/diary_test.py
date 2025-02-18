import unittest
from diary import Diary

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.diary = Diary()

    def test_that_add_to_an_array(self):
        diary = "I love java"
        self.diary.addEntry(diary)
        self.assertEqual([diary],self.diary.getEntries())

    def test_that_delete_diary(self):
        diary = "I love java"
        self.diary.addEntry(diary)
        self.diary.deleteDiary(diary)
        self.assertEqual([diary],self.diary.getEntries())


if __name__ == '__main__':
    unittest.main()
