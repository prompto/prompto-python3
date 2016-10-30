from prompto.value.IIterable import IIterable


class IContainer ( IIterable ):

    def getItem(self, context, index):
        raise Exception("You must override getItem in " + type(self).__name__)


    def hasItem(self, context, index):
        raise Exception("You must override hasItem in " + type(self).__name__)


