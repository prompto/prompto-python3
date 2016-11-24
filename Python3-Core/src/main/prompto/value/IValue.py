class IValue(object):

    def collectStorables(self, list):
        pass

    def GetType(self, context):
        raise Exception("You must override GetType in " + type(self).__name__)

    def IntDivide(self, context, value):
        raise Exception("You must override IntDivide in " + type(self).__name__)

    def getMemberValue(self, context, attrName, autoCreate=False):
        raise Exception("You must override GetMember in " + type(self).__name__)

    def setMember(self, context, attrName, value):
        raise Exception("You must override SetMember in " + type(self).__name__)

    def Roughly(self, context, value):
        return self==value
