
class ContextFlags(object):

    def __init__(self, isStart, isMember):
        self.isStart = isStart
        self.isMember = isMember


ContextFlags.START = ContextFlags(True, False)
ContextFlags.MEMBER = ContextFlags(False, True)
ContextFlags.NONE = ContextFlags(False, False)
