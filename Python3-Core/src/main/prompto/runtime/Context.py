from io import StringIO

from prompto.declaration.AttributeDeclaration import AttributeDeclaration
from prompto.declaration.IDeclaration import IDeclaration
from prompto.error.InternalError import InternalError
from prompto.expression.IExpression import IExpression
from prompto.runtime.IContext import IContext
from prompto.runtime.LinkedValue import LinkedValue
from prompto.runtime.Variable import Variable
from prompto.type.DecimalType import DecimalType
from prompto.value.ContextualExpression import ContextualExpression
from prompto.value.Decimal import Decimal
from prompto.value.ExpressionValue import ExpressionValue
from prompto.value.ConcreteInstance import ConcreteInstance
from prompto.error.SyntaxError import SyntaxError
from prompto.value.Integer import Integer


class Context(IContext):

    @staticmethod
    def newGlobalContext():
        context = Context()
        context.globals = context
        context.calling = None
        context.parent = None
        context.debugger = None
        return context

    def __init__(self):
        self.globals = None
        self.calling = None
        self.parent = None  # for inner methods
        self.debugger = None
        self.declarations = dict()
        self.tests = dict()
        self.instances = dict()
        self.values = dict()
        self.nativeBindings = dict()

    def isGlobalContext(self):
        return id(self) == id(self.globals)

    def setDebugger(self, debugger):
        self.debugger = debugger

    def getDebugger(self):
        return self.debugger

    def __str__(self):
        with StringIO() as sb:
            sb.write("{")
            if id(self) != id(self.globals):
                sb.write("globals:")
                sb.write(globals)
            sb.write(",calling:")
            sb.write(self.calling)
            sb.write(",parent:")
            sb.write(self.parent)
            sb.write(",declarations:")
            sb.write(self.declarations)
            sb.write(",instances:")
            sb.write(self.instances)
            sb.write(",values:")
            sb.write(self.values)
            sb.write("}")
            return sb.getvalue()

    def getCallingContext(self):
        return self.calling

    def getParentMostContext(self):
        if self.parent is None:
            return self
        else:
            return self.parent.getParentMostContext()

    def getParentContext(self):
        return self.parent

    def setParentContext(self, parent):
        self.parent = parent

    def newResourceContext(self):
        context = ResourceContext()
        context.globals = self.globals
        context.calling = self.calling
        context.parent = self
        context.debugger = self.debugger
        return context

    def newLocalContext(self):
        context = Context()
        context.globals = self.globals
        context.calling = self
        context.parent = None
        context.debugger = self.debugger
        return context

    def newDocumentContext(self, doc, isChild:bool):
        context = DocumentContext(doc)
        context.globals = self.globals
        context.calling = self.calling if isChild else self
        context.parent = self if isChild else None
        context.debugger = self.debugger
        return context

    def newInstanceContext(self, instance, typ, isChild:bool = False):
        context = InstanceContext(instance, typ)
        context.globals = self.globals
        context.calling = self.calling if isChild else self
        context.parent = self if isChild else None
        context.debugger = self.debugger
        return context


    def newBuiltInContext(self, value):
        context = BuiltInContext(value)
        context.globals = self.globals
        context.calling = self
        context.parent = None
        context.debugger = self.debugger
        return context


    def newChildContext(self):
        context = Context()
        context.globals = self.globals
        context.calling = self.calling
        context.parent = self
        context.debugger = self.debugger
        return context

    def findAttribute(self, name):
        return self.getRegisteredDeclaration(AttributeDeclaration, name)

    def getAllAttributes(self):
        if id(self) != id(self.globals):
            return self.globals.getAllAttributes()
        else:
            # need a real list here
            list = []
            for decl in self.declarations.values():
                if isinstance(decl, AttributeDeclaration):
                    list.append(decl)
            return list

    def getRegistered(self, name):
        # resolve upwards, since local names override global ones
        actual = self.declarations.get(name, None)
        if actual is not None:
            return actual
        actual = self.instances.get(name, None)
        if actual is not None:
            return actual
        if self.parent is not None:
            return self.parent.getRegistered(name)
        if id(self) != id(self.globals):
            return self.globals.getRegistered(name)
        return None

    def getRegisteredDeclaration(self, klass, name):
        # resolve upwards, since local names override global ones
        actual = self.declarations.get(name, None)
        if actual is None and self.parent is not None:
            actual = self.parent.getRegisteredDeclaration(klass, name)
        if actual is None and id(self) != id(self.globals):
            actual = self.globals.getRegisteredDeclaration(klass, name)
        if isinstance(actual, klass):
            return actual
        else:
            return None

    def registerDeclaration(self, declaration):
        actual = self.getRegistered(declaration.getName())
        if actual is not None:
            raise SyntaxError("Duplicate name: \"" + declaration.getName() + "\"")
        self.declarations[declaration.getName()] = declaration

    def registerMethodDeclaration(self, declaration):
        actual = self.getRegistered(declaration.getName())
        if actual is not None and not isinstance(actual, MethodDeclarationMap):
            raise SyntaxError("Duplicate name: \"" + declaration.name + "\"")
        if actual is None:
            actual = MethodDeclarationMap(declaration.getName())
            self.declarations[declaration.getName()] = actual
        actual.register(declaration, self)

    def registerTestDeclaration(self, declaration):
        actual = self.tests.get(declaration.name, None)
        if actual is not None:
            raise SyntaxError("Duplicate test: \"" + declaration.name + "\"")
        self.tests[declaration.name] = declaration

    def hasTests(self):
        return len(self.tests)>0

    def getRegisteredValue(self, klass, name):
        context = self.contextForValue(name)
        if context is None:
            return None
        else:
            return context.readRegisteredValue(klass, name)

    def readRegisteredValue(self, klass, name):
        actual = self.instances.get(name, None)
        if isinstance(actual, klass):
            return actual
        else:
            return None

    def registerValue(self, value, checkDuplicate = True):
        if checkDuplicate:
            # only explore current context
            if self.instances.get(value.getName(), None) is not None:
                raise SyntaxError("Duplicate name: \"" + value.getName() + "\"")
        self.instances[value.getName()] = value

    def registerNativeBinding(self, klass, decl):
        if self is self.globals:
            # use id since klass may change between register and get
            self.nativeBindings[id(klass)] = decl
        else:
            self.globals.registerNativeBinding(klass, decl)

    def getNativeBinding(self, klass):
        if self is self.globals:
            # use id since klass may change between register and get
            return self.nativeBindings.get(id(klass), None)
        else:
            return self.globals.getNativeBinding(klass)


    def hasValue(self, name):
        return self.contextForValue(name) is not None



    def getValue(self, name):
        context = self.contextForValue(name)
        if context is None:
            # context = self.contextForValue(name)
            raise SyntaxError(name + " is not defined")
        return context.readValue(name)



    def readValue(self, name):
        value = self.values.get(name, None)
        if value is None:
            raise SyntaxError(name + " has no value")
        if isinstance(value, LinkedValue):
            return value.context.getValue(name)
        else:
            return value

    def setValue(self, name, value):
        context = self.contextForValue(name)
        if context is None:
            raise SyntaxError(name + " is not defined")
        context.writeValue(name, value)

    def writeValue(self, name, value):
        value = self.autocast(name, value)
        current = self.values.get(name, None)
        if isinstance(current, LinkedValue):
            current.context.setValue(name, value)
        else:
            self.values[name] = value

    def autocast(self, name, value):
        if isinstance(value, Integer):
            actual = self.instances.get(name)
            if actual.getType(self) is DecimalType.instance:
                value = Decimal(value.DecimalValue())
        return value

    def contextForValue(self, name):
        # resolve upwards, since local names override global ones
        actual = self.instances.get(name, None)
        if not actual is None:
            return self
        if not self.parent is None:
            return self.parent.contextForValue(name)
        if id(self) != id(self.globals):
            return self.globals.contextForValue(name)
        return None

    def loadSingleton(self, type):
        if self is self.globals:
            value = self.values.get(type.typeName, None)
            if value is None:
                from prompto.declaration.ConcreteCategoryDeclaration import ConcreteCategoryDeclaration
                decl = self.declarations.get(type.typeName, None)
                if not isinstance(decl, ConcreteCategoryDeclaration):
                    raise InternalError("No such singleton:" + type.typeName)
                value = ConcreteInstance(self, decl)
                value.mutable = True # a singleton is protected by "with x do", so always mutable in that context
                self.values[type.typeName] = value
            if isinstance(value, ConcreteInstance):
                return value
            else:
                raise InternalError("Not a concrete instance:" + str(value))
        else:
            return self.globals.loadSingleton(type)

    def enterMethod(self, method):
        if self.debugger is not None:
            self.debugger.enterMethod(self, method)

    def leaveMethod(self, method):
        if self.debugger is not None:
            self.debugger.leaveMethod(self, method)

    def enterStatement(self, statement):
        if self.debugger is not None:
            self.debugger.enterStatement(self, statement)

    def leaveStatement(self, statement):
        if self.debugger is not None:
            self.debugger.leaveStatement(self, statement)

    def terminated(self):
        if self.debugger is not None:
            self.debugger.terminated()


class ResourceContext(Context):
    def __init__(self):
        super(ResourceContext, self).__init__()


class DocumentContext(Context):

    def __init__(self, document):
        super(DocumentContext, self).__init__()
        self.document = document

    def contextForValue(self, name):
        # params and variables have precedence over members
        # so first look in context values
        context = super(DocumentContext, self).contextForValue(name)
        if context is not None:
            return context
        # since any name is valid in the context of a document
        # simply return this document context
        else:
            return self



    def readValue(self, name):
        return self.document.getMemberValue(self.calling, name)



    def writeValue(self, name, value):
        self.document.setMember(self.calling, name, value)



class BuiltInContext(Context):

    def __init__(self, value):
        super().__init__()
        self.value = value



class InstanceContext(Context):

    def __init__(self, instance, type):
        super().__init__()
        self.instance = instance
        self.instanceType = type if type is not None else instance.type

    def readRegisteredValue(self, klass, name):
        actual = self.instances.get(name, None)
        # not very pure, but avoids a lot of complexity when registering a value
        if actual is None:
            attr = self.getRegisteredDeclaration(AttributeDeclaration, name)
            typ = attr.getType()
            actual = Variable(name, typ)
            self.instances[name] = actual
        return actual

    def contextForValue(self, name):
        # params and variables have precedence over members
        # so first look in context values
        context = super(InstanceContext, self).contextForValue(name)
        if context is not None:
            return context
        elif self.getDeclaration().hasAttribute(self, name):
            return self
        else:
            return None

    def getDeclaration(self):
        if self.instance is not None:
            return self.instance.getDeclaration()
        else:
            from prompto.declaration.ConcreteCategoryDeclaration import ConcreteCategoryDeclaration
            return self.getRegisteredDeclaration(ConcreteCategoryDeclaration, self.instanceType.typeName)

    def readValue(self, name):
        value = self.instance.getMemberValue(self.calling, name)
        if value is None:
            return None
        if isinstance(value, IExpression):
            return ContextualExpression(self, value)
        else:
            decl = self.getRegisteredDeclaration(AttributeDeclaration, name)
            return ExpressionValue(decl.getType(), value)



    def writeValue(self, name, value):
        self.instance.setMember(self.calling, name, value)




class MethodDeclarationMap(dict, IDeclaration):

    def __init__(self, name):
        super().__init__()
        self.name = name



    def getName(self):
        return self.name



    def getFirst(self):
        for method in self.values():
            return method



    def register(self, declaration, context):
        proto = declaration.getProto()
        if self.get(proto, None) is not None:
            raise SyntaxError("Duplicate prototype for name: \"" + declaration.name + "\"")
        self[proto] = declaration



    def registerIfMissing(self, declaration, context):
        proto = declaration.getProto()
        if self.get(proto, None) is None:
            self[proto] = declaration


