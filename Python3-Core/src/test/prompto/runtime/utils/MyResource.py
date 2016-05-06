from prompto.value.IResource import IResource

class MyResource(IResource):

    contents = dict()

    def __init__(self):
        self.path = None

    def __setattr__(self, key, value):
        if key=="content":
            MyResource.contents[self.path] = value
        else:
            self.__dict__[key] = value


    def isReadable(self):
        return True

    def isWritable(self):
        return True

    def close(self):
        pass

    def readFully(self):
        return MyResource.contents[self.path]

    def writeFully(self, data):
        MyResource.contents[self.path] = data
