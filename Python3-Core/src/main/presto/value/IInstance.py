from presto.value.IValue import IValue


class IInstance ( IValue ):

    def getType(self):
        raise Exception("You must override getType in " + type(self).__name__)
