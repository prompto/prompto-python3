class IResource ( object ):

    def close(self):
        raise Exception("You must override close in " + type(self).__name__)

    def isReadable(self):
        raise Exception("You must override isReadable in " + type(self).__name__)

    def isWritable(self):
        raise Exception("You must override isWritable in " + type(self).__name__)

    def readLine(self):
        raise Exception("You must override readLine in " + type(self).__name__)

    def writeLine(self, s):
        raise Exception("You must override writeLine in " + type(self).__name__)

    def readFully(self):
        raise Exception("You must override readFully in " + type(self).__name__)

    def writeFully(self, s, callback = None):
        raise Exception("You must override writeFully in " + type(self).__name__)

    def readBinary(self):
        raise Exception("You must override readBinary in " + type(self).__name__)
