import unittest
from html.parser import unescape
from html import escape

class TestHtml(unittest.TestCase):


    def testEncode(self):
        value = escape("a<b")
        self.assertEquals("a&lt;b", value)



    def testDecode(self):
        value = unescape("a&lt;b")
        self.assertEquals("a<b", value)

