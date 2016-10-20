from io import StringIO

from prompto.value.IResource import IResource

class MyResource(IResource):

    contents = dict()

    def __init__(self):
        self.path = None
        self.reader = None

    def __setattr__(self, key, value):
        if key=="content":
            MyResource.contents[self.path] = value
        else:
            object.__setattr__(self, key, value)

    def __getattr__(self, key):
        if key=="content":
            getattr(MyResource.contents, self.path, "")
        else:
            return object.__getattribute__(self, key)

    def isReadable(self):
        return True

    def isWritable(self):
        return True

    def close(self):
        pass

    def readFully(self):
        return self.content

    def readLine(self):
        if self.reader is None:
            self.reader = StringIO.StringIO(self.content)
        return self.reader.readLine()

    def writeFully(self, data):
        self.content = data

    def writeLine(self, data):
        if len(self.content) > 0:
            self.content += '\n'
        self.content += data
