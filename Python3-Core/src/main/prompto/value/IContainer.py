from prompto.value.IValue import IValue


class IContainer ( IValue ):

    def hasItem(self, context, value):
        raise Exception("You must override hasItem in " + type(self).__name__)
