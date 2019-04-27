from prompto.value.IValue import IValue

class IInstance ( IValue ):

    def getType(self):
        raise Exception("You must override getType in " + type(self).__name__)

    def toMutable(self):
        raise Exception("You must override raise in " + type(self).__name__)

