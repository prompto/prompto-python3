import threading

from prompto.error.NotMutableError import NotMutableError
from prompto.type.CategoryType import *
from prompto.value.BaseValue import *
from prompto.value.IInstance import *
from prompto.store.StorableDocument import StorableDocument
from prompto.python.PythonClassType import PythonClassType

# don't call getters from getters, so register them
activeGetters = threading.local()
# don't call setters from setters, so register them
activeSetters = threading.local()

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

    def GetMember(self, context, attrName, autoCreate=False):
        stacked = activeGetters.__dict__.get(attrName, None)
        first = stacked is None
        if first:
            activeGetters.__dict__[attrName] = context
        try:
            return self.doGetMember(context, attrName, first)
        finally:
            if first:
                del activeGetters.__dict__[attrName]

    def doGetMember(self, context, attrName, allowGetter):
        getter = self.declaration.findGetter(context, attrName) if allowGetter else None
        if getter != None:
            context = context.newInstanceContext(self, None).newChildContext()
            return getter.interpret(context)
        else:
            value = getattr(self.instance, attrName)
            ct = PythonClassType(type(value))
            return ct.convertPythonValueToPromptoValue(context, value, None) # TODO use attribute declaration

    def SetMember(self, context, attrName, value):
        if not self.mutable:
            raise NotMutableError()
        stacked = activeSetters.__dict__.get(attrName, None)
        first = stacked is None
        if first:
            activeSetters.__dict__[attrName] = context
        try:
            self.doSetMember(context, attrName, value, first)
        finally:
            if first:
                del activeSetters.__dict__[attrName]


    def doSetMember(self, context, attrName, value, allowSetter):
        decl = context.getRegisteredDeclaration(AttributeDeclaration, attrName)
        setter = self.declaration.findSetter(context, attrName) if allowSetter else None
        if setter != None:
            activeSetters.__dict__[attrName] = context
            # use attribute name as parameter name for incoming value
            context = context.newInstanceContext(self, None).newChildContext()
            context.registerValue(Variable(attrName, decl.getType()))
            context.setValue(attrName, value)
            value = setter.interpret(context)
        value = self.autocast(decl, value)
        setattr(self.instance, attrName, value.convertToPython())
        if self.storable is not None:
            decl = context.getRegisteredDeclaration(AttributeDeclaration, attrName)
            if decl.storable:
                # TODO convert object graph if(value instanceof IInstance)
                self.storable.setMember(context, attrName, value)

    def __getattr__(self, item):
        return getattr(self.instance,item)