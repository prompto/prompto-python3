class MyClass(object):

    def __init__(self):
        self.test = "Test"
        self.id = None
        self.name = None
        self.display = None

    def __setattr__(self, key, value):
        super(MyClass, self).__setattr__(key, value)
        if key in ["id", "name"]:
            self.computeDisplay()

    def computeDisplay(self):
        value = "/id=" + str(getattr(self, "id", None)) + "/name=" + str(getattr(self, "name", None))
        super(MyClass, self).__setattr__("display", value)

    def printDisplay(self):
        print(self.display,end='')

    def getDisplay(self):
        return self.display

    @staticmethod
    def boolValue():
        return True

    @staticmethod
    def intObject():
        return 123

    @staticmethod
    def intValue():
        return 123

    @staticmethod
    def longObject():
        return 9876543210

    @staticmethod
    def longValue():
        return 9876543210

    @staticmethod
    def characterValue():
        return 'Z'
