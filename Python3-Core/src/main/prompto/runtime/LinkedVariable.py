# used for downcast
from prompto.grammar.INamedValue import INamedValue


class LinkedVariable (INamedValue):

    def __init__(self, type, linked):
        self.type = type
        self.linked = linked

    def getName(self):
        return self.linked.getName()

    def getType(self, context):
        return self.type
