from io import StringIO

from prompto.declaration.CategoryDeclaration import CategoryDeclaration
from prompto.declaration.GetterMethodDeclaration import GetterMethodDeclaration
from prompto.declaration.IDeclaration import IDeclaration
from prompto.declaration.SetterMethodDeclaration import SetterMethodDeclaration
from prompto.runtime.Context import MethodDeclarationMap
from prompto.value.ConcreteInstance import ConcreteInstance
from prompto.error.SyntaxError import SyntaxError

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


    def isAWidget(self, context):
        if self.derivedFrom is None or len(self.derivedFrom) != 1:
            return False
        parent = context.getRegisteredDeclaration(CategoryDeclaration, self.derivedFrom[0])
        return parent.isAWidget(context)


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
            if self.ancestorHasAttribute(ancestor, context, name):
                return True
        return False


    def ancestorHasAttribute(self, ancestor, context, name):
        actual = context.getRegisteredDeclaration(CategoryDeclaration, ancestor)
        if actual is None:
            return False
        return actual.hasAttribute(context, name)


    def getAllAttributes(self, context):
        all = set()
        more = super(ConcreteCategoryDeclaration, self).getAllAttributes(context)
        if more is not None:
            all = more
        if self.derivedFrom is not None:
            for name in self.derivedFrom:
                names = self.getAncestorAttributes(context, name)
                if names is not None:
                    all = all.union(names)
        return None if len(all)==0 else all



    def getAncestorAttributes(self, context, ancestor):
        decl = context.getRegisteredDeclaration(CategoryDeclaration, ancestor)
        return None if decl is None else decl.getAllAttributes(context)



    def hasMethod(self, context, name):
        self.registerMethods(context)
        if self.methodsMap.get(name) is not None:
            return True
        if self.hasDerivedMethod(context,name):
            return True
        return False


    def hasDerivedMethod(self, context, name):
        if self.derivedFrom is None:
            return False
        for ancestor in self.derivedFrom:
            if self.ancestorHasMethod(ancestor,context,name):
                return True
        return False


    def ancestorHasMethod(self, ancestor, context, name):
        actual = context.getRegisteredDeclaration(CategoryDeclaration, ancestor)
        if actual is None:
            return False
        return actual.hasMethod(context, name)


    def check(self, context):
        context = context.newInstanceContext(None, self.getType(context))
        self.checkDerived(context)
        self.checkMethods(context)
        return super(ConcreteCategoryDeclaration, self).check(context)


    def registerMethods(self, context):
        if self.methodsMap is None:
            self.methodsMap = dict()
            if self.methods is not None:
                for method in self.methods:
                    method.memberOf = self
                    self.registerMethodDeclaration(method,context)


    def checkMethods(self, context):
        self.registerMethods(context)
        if self.methods is not None:
            for method in self.methods:
                method.checkChild(context)


    def registerMethodDeclaration(self, method, context):
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
            actual.register(method)


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
            if ancestor==categoryType.typeName:
                return True
            if self.isAncestorDerivedFrom(ancestor,context,categoryType):
                return True
        return False


    def isAncestorDerivedFrom(self, ancestor, context, categoryType):
        actual = context.getRegisteredDeclaration(IDeclaration, ancestor)
        if actual is None and not isinstance(actual, CategoryDeclaration):
            return False
        return actual.isDerivedFrom(context, categoryType)


    def newInstance(self, context):
        return ConcreteInstance(context, self)


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


    def getMemberMethodsMap(self, context, name):
        self.registerMethods(context)
        methods = MethodDeclarationMap(name)
        self.registerMemberMethods(context, methods)
        return methods


    def registerMemberMethods(self, context, result):
        self.registerSelfMemberMethods(context, result)
        self.registerDerivedMemberMethods(context, result)


    def registerSelfMemberMethods(self, context, result):
        if self.methodsMap is None:
            return
        actual = self.methodsMap.get(result.getName(), None)
        if actual is None:
            return
        if not isinstance(actual, MethodDeclarationMap):
            raise SyntaxError("Not a member method!")
        for method in actual.values():
            result.registerIfMissing(method)

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
        self.protoToEDialect(writer, hasMethods, False) # no bindings
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
        if self.isAWidget(writer.context):
            writer.append("widget")
        else:
            writer.append("category")


    def categoryExtensionToODialect(self, writer):
        if self.derivedFrom is not None:
            writer.append(" extends ")
            self.derivedFrom.toDialect(writer, True)


    def bodyToODialect(self, writer):
        self.methodsToODialect(writer, self.methods)


    def toMDialect(self, writer):
        self.protoToMDialect(writer, self.derivedFrom)
        self.methodsToMDialect(writer)


    def categoryTypeToMDialect(self, writer):
        writer.append("class")


    def methodsToMDialect(self, writer):
        writer.indent()
        if self.methods is None or len(self.methods)==0:
            writer.append("pass\n")
        else:
            for decl in self.methods:
                if decl.comments is not None:
                    for comment in decl.comments:
                        comment.toDialect(writer)
                if decl.annotations is not None:
                    for annotation in decl.annotations:
                        annotation.toDialect(writer)
                w = writer.newMemberWriter()
                decl.toDialect(w)
                writer.newLine()
        writer.dedent()


    def getOperatorMethod(self, context, operator, type):
        methodName = "operator_" + operator.name
        methods = self.getMemberMethodsMap(context, methodName)
        if methods is None:
            return None
        # find best candidate
        candidate = None
        for method in methods.values():
            potential = method.parameters[0].getType(context)
            if not potential.isAssignableFrom(context, type):
                continue
            if candidate is None:
                candidate = method
            else:
                currentBest = candidate.arguments[0].getType(context)
                if potential.isAssignableFrom(context, currentBest):
                    candidate = method
        return candidate


    def collectCategories(self, context):
        set_ = set()
        list_ = list()
        self.doCollectCategories(context, set_, list_)
        return list_


    def doCollectCategories(self, context, set_, list_):
        if self.derivedFrom is not None:
            for cat in self.derivedFrom:
                cd = context.getRegisteredDeclaration(CategoryDeclaration, cat)
                cd.doCollectCategories(context, set_, list_)
        if not self.name in set_:
            set_.add(self.name)
            list_.append(self.name)
