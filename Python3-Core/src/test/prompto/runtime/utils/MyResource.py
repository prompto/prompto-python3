from prompto.value.IResource import IResource

class MyResource(IResource):

    contents = dict()

    def __init__(self):
        self.path = None
        self.lines = None


    def __setattr__(self, key, value):
        if key=="content":
            MyResource.contents[self.path] = value
        else:
            object.__setattr__(self, key, value)


    def __getattr__(self, key):
        if key=="content":
            return MyResource.contents.get(self.path, "")
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
        if self.lines is None:
            if self.content is None:
                self.lines = []
            else:
                self.lines = self.content.split('\n')
        if len(self.lines) > 0:
            return self.lines.pop(0)
        else:
            return None


    def writeFully(self, data, callback = None):
        self.content = data
        if callback is not None:
            callback("accepted: " + self.content)


    def writeLine(self, data):
        # for testing, don't append LF to last line
        if len(self.content) > 0:
            self.content += '\n'
        self.content += data
