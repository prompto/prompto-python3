from prompto.value.IValue import IValue


class IIterable ( IValue ):

    def getIterator(self, context):
        raise Exception("You must override getIterator in " + type(self).__name__)

