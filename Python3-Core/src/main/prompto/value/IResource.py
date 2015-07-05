class IResource ( object ):

    def isWritable(self):
        raise Exception("You must override isWritable in " + type(self).__name__)

    def writeFully(self, s):
        raise Exception("You must override writeFully in " + type(self).__name__)
