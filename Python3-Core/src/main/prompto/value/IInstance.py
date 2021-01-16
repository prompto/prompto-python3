from prompto.value.IValue import IValue

class IInstance ( IValue ):

    def getDeclaration(self):
        raise Exception("You must override getDeclaration in " + type(self).__name__)

    def getType(self):
        raise Exception("You must override getType in " + type(self).__name__)

    def toMutable(self):
        raise Exception("You must override raise in " + type(self).__name__)

