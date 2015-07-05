from __future__ import print_function
import unittest
import sys

#rewrite print
__old__print__ = globals()["__builtins__"]["print"]
def __print__(objects,sep=' ', end='\n', file=sys.stdout):
    __old__print__(objects,sep=sep,end=end,file=file)
globals()["print"] = __print__

class TestMethod(unittest.TestCase):

    def tupleArgs(self):
        return ("abc",)

    def dictArgs(self):
        return { "objects":"abc", "end":""}

    def method(self):
        m = globals().get("print", None)
        if m is None:
            m = globals()["__builtins__"]["print"]
        return m

    def testPrint(self):
        m = self.method()
        args = self.tupleArgs()
        m(*args)
        kwargs = self.dictArgs()
        m(**kwargs)

