from prompto.value.IValue import IValue

class BaseValue(IValue):

    def __init__(self, itype):
        self.itype = itype
        self.mutable = False

    def GetType(self, context):
        return self.itype

    def Add(self, context, value):
        raise Exception("Add not supported by " + type(self).__name__)

    def Subtract(self, context, value):
        raise Exception("Subtract not supported by " + type(self).__name__)

    def Multiply(self, context, value):
        raise Exception("Multiply not supported by " + type(self).__name__)

    def Divide(self, context, value):
        raise Exception("Divide not supported by " + type(self).__name__)

    def IntDivide(self, context, value):
        raise Exception("Integer divide not supported by " + type(self).__name__)

    def Modulo(self, context, value):
        raise Exception("Integer divide not supported by " + type(self).__name__)

    def CompareTo(self, context, value):
        raise Exception("Compare not supported by " + type(self).__name__)

    def Contains(self, context, value):
        raise Exception("Contains not supported by " + type(self).__name__)

    def getMemberValue(self, context, name, autoCreate=False):
        from prompto.value.Text import Text
        if "text" == name:
            return Text(str(self))
        else:
            raise Exception("No member support for " + type(self).__name__)

    def setMember(self, context, name, value):
        raise Exception("No member support for " + type(self).__name__)

    def ConvertTo(self, itype):
        return self
