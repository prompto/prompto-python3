# used for downcast
from prompto.grammar.INamedInstance import INamedInstance


class LinkedVariable (INamedInstance):

    def __init__(self, type, linked):
        self.type = type
        self.linked = linked

    def getName(self):
        return self.linked.getName()

    def getType(self, context):
        return self.type
