class IValue(object):

    def GetType(self, context):
        raise Exception("You must override GetType in " + type(self).__name__)

    def IntDivide(self, context, value):
        raise Exception("You must override IntDivide in " + type(self).__name__)

    def getMember(self, context, attrName):
        raise Exception("You must override getMember in " + type(self).__name__)

    def Roughly(self, context, value):
        return self==value
