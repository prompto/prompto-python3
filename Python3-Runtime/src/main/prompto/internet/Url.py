from prompto.value.IResource import IResource
import urllib.request

class Url(IResource):

    def __init__(self):
        self.path = None
        self.reader = None

    def isReadable(self):
        return True

    def isWritable(self):
        return True

    def close(self):
        if self.reader is not None:
            self.reader.close()

    def readFully(self):
        with urllib.request.urlopen(self.path) as response:
            return str(response.read())

    def readLine(self):
        if self.reader is None:
            self.reader = urllib.request.urlopen(self.path)
        return str(self.reader.readLine())

    def writeFully(self, data):
        pass

    def writeLine(self, data):
        pass
