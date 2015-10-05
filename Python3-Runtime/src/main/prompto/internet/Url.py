from prompto.value.IResource import IResource
import urllib.request

class Url(IResource):

    def __init__(self):
        self.path = None

    def isReadable(self):
        return True

    def isWritable(self):
        return True

    def close(self):
        pass

    def readFully(self):
        with urllib.request.urlopen(self.path) as response:
            return str(response.read())

    def writeFully(self, data):
        pass
