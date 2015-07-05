from prompto.value.IResource import IResource

class MyResource(IResource):

    content = ""

    def __init__(self):
        self.path = None

    def isReadable(self):
        return True

    def isWritable(self):
        return True

    def close(self):
        pass

    def readFully(self):
        return MyResource.content

    def writeFully(self, data):
        MyResource.content = data
