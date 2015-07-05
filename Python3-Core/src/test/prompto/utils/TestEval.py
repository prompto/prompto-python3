import unittest


class TestEval(unittest.TestCase):


    def testString(self):
        value = eval(compile("\"John\"","__no_file__",mode='eval'))
        self.assertEquals("John", value)


