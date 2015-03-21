import unittest


class TestLimits(unittest.TestCase):

    def testParseMaxLong(self):
        l1 = 0x7FFFFFFFFFFFFFFF
        s = str(l1)
        l2 = int(s)
        self.assertEquals(l1, l2)

    def testParseMinLong(self):
        l1 = 0x8000000000000000
        s = str(l1)
        l2 = int(s)
        self.assertEquals(l1, l2)
