from presto.value.IResource import IResource
from presto.value.Text import Text
from presto.value.NativeInstance import NativeInstance


class NativeResource(NativeInstance, IResource):

    def __init__(self, declaration):
        super(NativeResource, self).__init__(declaration)

    def isReadable(self):
        return self.instance.isReadable()

    def isWritable(self):
        return self.instance.isWritable()

    def readFully(self):
        s = self.instance.readFully()
        return Text(s)

    def writeFully(self, data):
        s = str(data)
        self.instance.writeFully(s)

    def close(self):
        self.instance.close()
