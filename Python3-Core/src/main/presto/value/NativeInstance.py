from presto.type.CategoryType import *
from presto.value.BaseValue import *
from presto.value.IInstance import *
from presto.python.PythonClassType import PythonClassType

class NativeInstance(BaseValue, IInstance):

    def __init__(self, declaration):
        super(NativeInstance, self).__init__(CategoryType(declaration.name))
        self.declaration = declaration
        self.instance = self.makeInstance()

    def getInstance(self):
        return self.instance

    def makeInstance(self):
        mapped = self.declaration.getMappedClass()
        return mapped()

    def getType(self):
        return self.type

    def getMember(self, context, attrName):
        value = getattr(self.instance, attrName)
        ct = PythonClassType(type(value))
        return ct.convertPythonValueToPrestoValue(value)

    def set(self, context, attrName, value):
        setattr(self.instance, attrName, value.convertToPython())

    def __getattr__(self, item):
        return getattr(self.instance,item)