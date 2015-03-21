from presto.utils.CmdLineParser import parseCmdLine
import unittest

class TestCmdLineParser(unittest.TestCase):

    def testNone(self):
        options = parseCmdLine(None)
        self.assertIsNotNone(options)


    def testEmpty(self):
        options = parseCmdLine("")
        self.assertIsNotNone(options)


    def testKVP1(self):
        options = parseCmdLine("a=b")
        self.assertEquals("b",options.get("a"))


    def testKVP2(self):
        options = parseCmdLine("a = b")
        self.assertEquals("b",options.get("a"))


    def testKVP3(self):
        options = parseCmdLine("-a=b")
        self.assertEquals("b",options.get("a"))


    def testKVP4(self):
        options = parseCmdLine("123=444")
        self.assertEquals("444",options.get("123"))


    def testKVP5(self):
        options = parseCmdLine("-a=b c=d e=f")
        self.assertEquals("b",options.get("a"))
        self.assertEquals("d",options.get("c"))
        self.assertEquals("f",options.get("e"))


    def testKVP6(self):
        options = parseCmdLine('123="444 -qlsdkj ==22"')
        self.assertEquals("444 -qlsdkj ==22",options["123"])


