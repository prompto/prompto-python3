from prompto.value.IResource import IResource
from prompto.value.TextValue import TextValue
from prompto.value.NativeInstance import NativeInstance


class NativeResource(NativeInstance, IResource):

    def __init__(self, context, declaration):
        super(NativeResource, self).__init__(context, declaration)

    def isReadable(self):
        return self.instance.isReadable()

    def isWritable(self):
        return self.instance.isWritable()

    def readFully(self):
        s = self.instance.readFully()
        return TextValue(s)

    def writeFully(self, data):
        s = str(data)
        self.instance.writeFully(s)

    def readLine(self):
        s = self.instance.readLine()
        return TextValue(s)

    def writeLine(self, data):
        s = str(data)
        self.instance.writeLine(s)

    def close(self):
        self.instance.close()
