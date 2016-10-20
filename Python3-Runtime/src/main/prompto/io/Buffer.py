from prompto.value.IResource import IResource
from io import StringIO

class Buffer(IResource):

    def __init__(self):
        self.data = StringIO()

    def isReadable(self):
        return True

    def isWritable(self):
        return True

    def close(self):
        self.data.close()

    def __getattr__(self, item):
        if item == "text":
            return self.data.getvalue()
        else:
            return object.__getattribute__(self, item)

    def readFully(self):
        return self.data.getvalue()

    def readLine(self):
        return self.data.readLine()

    def writeFully(self, data):
        self.data = StringIO(data)

    def writeLine(self, data):
        if len(self.data.getvalue()) > 0:
            self.data.write('\n')
        self.data.write(data)
