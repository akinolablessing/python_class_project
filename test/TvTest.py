import unittest

import my_tv
from my_tv import MyTv


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.tv = MyTv()

    def test_that_off_myTv(self):

        self.assertFalse(self.tv.on_myTv())

    def test_that_on_myTv(self):

        self.tv.on_myTv()
        self.assertTrue(self.tv.isOn)

    def test_that_increase_volume(self):

        self.tv.on_myTv()
        self.tv.inCrease_volume()
        self.tv.inCrease_volume()
        self.tv.inCrease_volume()
        self.assertEqual(self.tv.volume,3)


    def test_that_descrease_volume(self):
        self.tv.on_myTv()
        self.tv.deCrease_volume()
        self.tv.deCrease_volume()
        self.tv.deCrease_volume()
        self.assertEqual(self.tv.volume,-3)

    def test_that_channel_down(self):
        self.tv.on_myTv()
        self.tv.channel_down()
        self.assertEqual(self.tv.channel,-1)

    def test_that_channel_up(self):
        self.tv.on_myTv()
        self.tv.channel_up()
        self.assertEqual(self.tv.channel,1)

    def test_that_set_channel(self):
        self.tv.on_myTv()
        self.tv.set_channel(5)
        self.assertEqual(self.tv.channel,5)

    def test_that_mute_channel(self):
         self.tv.on_myTv()
         self.assertTrue(self.tv.mute_channell())


    def test_that_unmute_channel(self):
        self.tv.on_myTv()
        self.assertFalse(self.tv.unMute_channell())


if __name__ == '__main__':
    unittest.main()
