import sys
from io import StringIO


class Out(object):

    oldOut = None

    @staticmethod
    def init():
        Out.oldOut = sys.stdout
        sys.stdout = StringIO()

    @staticmethod
    def read():
        return sys.stdout.getvalue()

    @staticmethod
    def reset():
        sys.stdout = StringIO()

    @staticmethod
    def restore():
        sys.stdout = Out.oldOut
        Out.oldOut = None
