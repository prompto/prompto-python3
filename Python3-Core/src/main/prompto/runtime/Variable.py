from prompto.grammar.INamedInstance import INamedInstance

class Variable ( INamedInstance ):

    def __init__(self, name, itype):
        self.name = name
        self.itype = itype

    def __str__(self):
        return self.name

    def getName(self):
        return self.name

    def getType(self, context):
        return self.itype
