from prompto.type.CategoryType import *
from prompto.value.BaseValue import *
from prompto.value.IInstance import *
from prompto.store.StorableDocument import StorableDocument
from prompto.python.PythonClassType import PythonClassType

class NativeInstance(BaseValue, IInstance):

    def __init__(self, declaration, instance=None):
        super(NativeInstance, self).__init__(CategoryType(declaration.name))
        self.declaration = declaration
        self.storable = StorableDocument() if declaration.storable else None
        self.instance = self.makeInstance() if instance is None else instance

    def convertToPython(self):
        return self.instance

    def getInstance(self):
        return self.instance

    def makeInstance(self):
        mapped = self.declaration.getBoundedClass(True)
        return mapped()

    def getType(self):
        return self.type

    def GetMember(self, context, attrName):
        value = getattr(self.instance, attrName)
        ct = PythonClassType(type(value))
        return ct.convertPythonValueToPromptoValue(context, value, None) # TODO use attribute declaration

    def SetMember(self, context, attrName, value):
        setattr(self.instance, attrName, value.convertToPython())
        if self.storable is not None:
            decl = context.getRegisteredDeclaration(AttributeDeclaration, attrName)
            if self.declaration.storable:
                # TODO convert object graph if(value instanceof IInstance)
                self.storable.setMember(context, attrName, value)

    def __getattr__(self, item):
        return getattr(self.instance,item)