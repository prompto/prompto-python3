from prompto.grammar.INamedInstance import INamedInstance

class Variable ( INamedInstance ):

    def __init__(self, name, type):
        self.name = name
        self.type = type

    def __str__(self):
        return self.name

    def getName(self):
        return self.name

    def getType(self, context):
        return self.type
