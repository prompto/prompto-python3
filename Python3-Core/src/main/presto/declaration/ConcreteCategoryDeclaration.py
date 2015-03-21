from presto.declaration.CategoryDeclaration import *
from presto.declaration.GetterMethodDeclaration import *
from presto.declaration.SetterMethodDeclaration import *
from presto.value.ConcreteInstance import *


class ConcreteCategoryDeclaration ( CategoryDeclaration ):

    def __init__(self, name, attributes=None):
        super(ConcreteCategoryDeclaration, self).__init__(name, attributes)
        self.derivedFrom = None
        self.methods = None
        self.methodsMap = None

    def setDerivedFrom(self, derivedFrom):
        self.derivedFrom = derivedFrom

    def getDerivedFrom(self):
        return self.derivedFrom

    def setMethods(self, methods):
        self.methods = methods

    def getMethods(self):
        return self.methods

    def __str__(self):
        sb = StringIO(self.getName())
        if self.derivedFrom is not None:
            sb.write('(')
            sb.write(str(self.derivedFrom))
            sb.write(')')
        if self.attributes is not None:
            sb.write(':')
            sb.write(str(self.attributes))
        return sb.getvalue()

    def hasAttribute(self, context, name):
        if super(ConcreteCategoryDeclaration, self).hasAttribute(context, name):
            return True
        if self.hasDerivedAttribute(context,name):
            return True
        return False

    def hasDerivedAttribute(self, context, name):
        if self.derivedFrom is None:
            return False
        for ancestor in self.derivedFrom:
            if self.ancestorHasAttribute(ancestor,context,name):
                return True
        return False

    def ancestorHasAttribute(self, ancestor, context, name):
        actual = context.getRegisteredDeclaration(CategoryDeclaration, ancestor)
        if actual is None:
            return False
        return actual.hasAttribute(context, name)

    def check(self, context):
        self.checkDerived(context)
        self.checkMethods(context)
        return super(ConcreteCategoryDeclaration, self).check(context)

    def checkMethods(self, context):
        if self.methodsMap is None:
            self.methodsMap = dict()
            if self.methods is not None:
                for method in self.methods:
                    self.registerMethod(method,context)

    def registerMethod(self, method, context):
        actual = None
        if isinstance(method, SetterMethodDeclaration):
            actual = self.methodsMap.get("setter:"+method.getName())
            if actual is not None:
                raise SyntaxError("Duplicate setter: \"" + method.getName() + "\"")
            self.methodsMap["setter:"+method.getName()] = method
        elif isinstance(method, GetterMethodDeclaration):
            actual = self.methodsMap.get("getter:"+method.getName())
            if actual is not None:
                raise SyntaxError("Duplicate getter: \"" + method.getName() + "\"")
            self.methodsMap["getter:"+method.getName()] = method
        else:
            actual = self.methodsMap.get(method.getName())
            if actual is None:
                actual = MethodDeclarationMap(method.getName())
                self.methodsMap[method.getName()] = actual
            actual.register(method,context)
        method.checkMember(self, context)

    def checkDerived(self, context):
        if self.derivedFrom is not None:
            for category in self.derivedFrom:
                cd = context.getRegisteredDeclaration(ConcreteCategoryDeclaration, category)
                if cd is None:
                    raise SyntaxError("Unknown category: \"" + category + "\"")

    def isDerivedFrom(self, context, categoryType):
        if self.derivedFrom is None:
            return False
        for ancestor in self.derivedFrom:
            if ancestor==categoryType.getName():
                return True
            if self.isAncestorDerivedFrom(ancestor,context,categoryType):
                return True
        return False

    def isAncestorDerivedFrom(self, ancestor, context, categoryType):
        actual = context.getRegisteredDeclaration(IDeclaration, ancestor)
        if actual is None and not isinstance(actual, CategoryDeclaration):
            return False
        return actual.isDerivedFrom(context, categoryType)

    def newInstance(self):
        return ConcreteInstance(self)

    def findGetter(self, context, attrName):
        if self.methodsMap is None:
            return None
        method = self.methodsMap.get("getter:"+attrName, None)
        if isinstance(method, GetterMethodDeclaration):
            return method
        if method is not None:
            raise SyntaxError("Not a getter method!")
        return self.findDerivedGetter(context, attrName)

    def findDerivedGetter(self, context, attrName):
        if self.derivedFrom is None:
            return None
        for ancestor in self.derivedFrom:
            method = self.findAncestorGetter(ancestor,context,attrName)
            if method is not None:
                return method
        return None

    def findAncestorGetter(self, ancestor, context, attrName):
        actual = context.getRegisteredDeclaration(IDeclaration, ancestor)
        if actual is None or not isinstance(actual, ConcreteCategoryDeclaration):
            return None
        return actual.findGetter(context, attrName)

    def findSetter(self, context, attrName):
        if self.methodsMap is None:
            return None
        method = self.methodsMap.get("setter:"+attrName, None)
        if isinstance(method, SetterMethodDeclaration):
            return method
        if method is not None:
            raise SyntaxError("Not a setter method!")
        return self.findDerivedSetter(context,attrName)

    def findDerivedSetter(self, context, attrName):
        if self.derivedFrom is None:
            return None
        for ancestor in self.derivedFrom:
            method = self.findAncestorSetter(ancestor,context,attrName)
            if method is not None:
                return method
        return None

    def findAncestorSetter(self, ancestor, context, attrName):
        actual = context.getRegisteredDeclaration(IDeclaration, ancestor)
        if actual is None or not isinstance(actual, ConcreteCategoryDeclaration):
            return None
        return actual.findSetter(context, attrName)

    def findMemberMethods(self, context, name):
        result = MethodDeclarationMap(name)
        self.registerMemberMethods(context,result)
        return result.values()

    def registerMemberMethods(self, context, result):
        self.registerSelfMemberMethods(context,result)
        self.registerDerivedMemberMethods(context,result)

    def registerSelfMemberMethods(self, context, result):
        if self.methodsMap is None:
            return
        actual = self.methodsMap.get(result.getName(), None)
        if actual is None:
            return
        if not isinstance(actual, MethodDeclarationMap):
            raise SyntaxError("Not a member method!")
        for method in actual.values():
            result.registerIfMissing(method, context)

    def registerDerivedMemberMethods(self, context, result):
        if self.derivedFrom is None:
            return
        for ancestor in self.derivedFrom:
            self.registerAncestorMemberMethods(ancestor, context, result)

    def registerAncestorMemberMethods(self, ancestor, context, result):
        actual = context.getRegisteredDeclaration(IDeclaration, ancestor)
        if actual is None or not isinstance(actual, ConcreteCategoryDeclaration):
            return
        actual.registerMemberMethods(context, result)

    def toEDialect(self, writer):
        hasMethods = self.methods is not None and len(self.methods)>0
        self.protoToEDialect(writer, hasMethods, False) # no mappings
        if hasMethods:
            self.methodsToEDialect(writer, self.methods)

    def categoryTypeToEDialect(self, writer):
        if self.derivedFrom is None:
            writer.append("category")
        else:
            self.derivedFrom.toDialect(writer, True)

    def toODialect(self, writer):
        hasMethods = self.methods is not None and len(self.methods)>0
        self.allToODialect(writer, hasMethods)

    def categoryTypeToODialect(self, writer):
        writer.append("category")

    def categoryExtensionToODialect(self, writer):
        if self.derivedFrom is not None:
            writer.append(" extends ")
            self.derivedFrom.toDialect(writer, True)

    def bodyToODialect(self, writer):
        for decl in self.methods:
            decl.toDialect(writer)
            writer.newLine()

    def toPDialect(self, writer):
        self.protoToPDialect(writer, self.derivedFrom)
        self.methodsToPDialect(writer)

    def categoryTypeToPDialect(self, writer):
        writer.append("class")

    def methodsToPDialect(self, writer):
        writer.indent()
        if self.methods is None or len(self.methods)==0:
            writer.append("pass\n")
        else:
            for decl in self.methods:
                decl.toDialect(writer)
                writer.newLine()
        writer.dedent()

    def findOperator(self, context, operator, type):
        methodName = "operator_" + operator.name
        methods = self.findMemberMethods(context, methodName)
        if methods is None:
            return None
        # find best candidate
        candidate = None
        for method in methods:
            potential = method.arguments[0].getType(context)
            if not type.isAssignableTo(context, potential):
                continue
            if candidate is None:
                candidate = method
            else:
                currentBest = candidate.arguments[0].getType(context)
                if currentBest.isAssignableTo(context, potential):
                    candidate = method
        return candidate
