from prompto.declaration.IEnumeratedDeclaration import IEnumeratedDeclaration
from prompto.error.PromptoError import PromptoError
from prompto.error.SyntaxError import SyntaxError
from prompto.expression.ArrowExpression import ArrowExpression
from prompto.expression.ValueExpression import ValueExpression
from prompto.expression.MethodSelector import MethodSelector
from prompto.expression.Symbol import Symbol
from prompto.expression.UnresolvedIdentifier import UnresolvedIdentifier
from prompto.grammar.Argument import Argument
from prompto.grammar.ArgumentList import ArgumentList
from prompto.grammar.Operator import Operator
from prompto.parser.Dialect import Dialect
from prompto.runtime.Context import MethodDeclarationMap
from prompto.runtime.Score import Score
from prompto.store.DataStore import DataStore
from prompto.store.Store import IStored
from prompto.store.TypeFamily import TypeFamily
from prompto.type.MethodType import MethodType
from prompto.type.NativeType import NativeType
from prompto.type.TextType import TextType
from prompto.type.BaseType import BaseType
from prompto.type.IType import IType
from prompto.type.NullType import NullType
from prompto.type.AnyType import AnyType
from prompto.type.MissingType import MissingType
from prompto.declaration.IDeclaration import IDeclaration
from prompto.declaration.AttributeDeclaration import AttributeDeclaration

class CategoryType(BaseType):

    def __init__(self, typeName, family = TypeFamily.CATEGORY, mutable = False):
        super(CategoryType, self).__init__(family)
        self.typeName = typeName
        self.mutable = mutable
        self.resolved = None

    def __eq__(self, obj):
        if obj is None:
            return False
        if id(obj) == id(self):
            return True
        if not isinstance(obj, CategoryType):
            return False
        return self.typeName == obj.typeName


    def isMutable(self, context):
        return self.mutable


    def asMutable(self, context, mutable):
        if self.mutable == mutable:
            return self
        else:
            return CategoryType(self.typeName, mutable = mutable)


    def anyfy(self):
        if self.typeName == "Any":
            return AnyType.instance
        else:
            return self


    def resolve(self, context, onError = None):
        if self.resolved is None:
            typ = self.anyfy()
            if isinstance(typ, NativeType):
                self.resolved = typ
            else:
                if(isinstance(context, CategoryType)):
                    raise SyntaxError("what!!")
                decl = context.getRegisteredDeclaration(IDeclaration, typ.typeName)
                if decl is None:
                    if onError is not None:
                        onError(typ)
                        return None
                    else:
                        raise SyntaxError("Unknown type:" + typ.typeName)
                elif isinstance(decl, MethodDeclarationMap):
                    self.resolved = MethodType(decl.getFirst())
                else:
                    found = decl.getType(context)
                    self.resolved = typ if type(found)==type(typ) else found
        return self.resolved


    def toDialect(self, writer, skipMutable=False):
        if self.mutable and not skipMutable:
            writer.append("mutable ")
        writer.append(self.typeName)


    def getSuperType(self, context):
        from prompto.declaration.CategoryDeclaration import CategoryDeclaration
        decl = self.getDeclaration(context)
        if isinstance(decl, CategoryDeclaration):
            derived = decl.getDerivedFrom()
            if derived is not None and len(derived) > 0:
                return CategoryType(derived[0])
        raise SyntaxError("No super type for:" + self.typeName)


    def newInstanceFromStored(self, context, document):
        decl = self.getDeclaration(context)
        inst = decl.newInstanceFromStored(context, document)
        inst.mutable = self.mutable
        return inst


    def checkUnique(self, context):
        actual = context.getRegisteredDeclaration(IDeclaration, self.typeName)
        if actual is not None:
            raise SyntaxError("Duplicate name: \"" + self.typeName + "\"")


    def getDeclaration(self, context):
        from prompto.declaration.CategoryDeclaration import CategoryDeclaration
        from prompto.declaration.EnumeratedNativeDeclaration import EnumeratedNativeDeclaration
        decl = context.getRegisteredDeclaration(CategoryDeclaration, self.typeName)
        if decl is None:
            decl = context.getRegisteredDeclaration(EnumeratedNativeDeclaration, self.typeName)
        if decl is None:
            raise SyntaxError("Unknown category: \"" + self.typeName + "\"")
        return decl


    def checkMultiply(self, context, other, tryReverse):
        typ = self.checkOperator(context, other, tryReverse, Operator.MULTIPLY)
        if typ is not None:
            return typ
        else:
            return super().checkMultiply(context, other, tryReverse)


    def checkDivide(self, context, other):
        typ = self.checkOperator(context, other, False, Operator.DIVIDE)
        if typ is not None:
            return typ
        else:
            return super().checkDivide(context, other)


    def checkIntDivide(self, context, other):
        typ = self.checkOperator(context, other, False, Operator.IDIVIDE)
        if typ is not None:
            return typ
        else:
            return super().checkIntDivide(context, other)


    def checkModulo(self, context, other):
        typ = self.checkOperator(context, other, False, Operator.MODULO)
        if typ is not None:
            return typ
        else:
            return super().checkModulo(context, other)


    def checkAdd(self, context, other, tryReverse):
        typ = self.checkOperator(context, other, tryReverse, Operator.PLUS)
        if typ is not None:
            return typ
        else:
            return super().checkAdd(context, other, tryReverse)


    def checkSubstract(self, context, other):
        typ = self.checkOperator(context, other, False, Operator.MINUS)
        if typ is not None:
            return typ
        else:
            return super().checkSubstract(context, other)


    def checkOperator(self, context, other, tryReverse, operator):
        from prompto.declaration.ConcreteCategoryDeclaration import ConcreteCategoryDeclaration
        actual = self.getDeclaration(context)
        if isinstance(actual, ConcreteCategoryDeclaration):
            try:
                method = actual.getOperatorMethod(context, operator, other)
                if method is None:
                    return None
                context = context.newInstanceContext(None, self)
                local = context.newChildContext()
                method.registerArguments(local)
                return method.check(local, False)
            except SyntaxError as e:
                # ok to pass, will try reverse
                pass
        if tryReverse:
            return None
        else:
            raise SyntaxError("Unsupported operation: " + self.typeName + " " + operator.token + " " + other.name)


    def checkExists(self, context):
        self.resolve(context)


    def checkMember(self, context, name):
        if "category" == name:
            return CategoryType("Category")
        decl = context.getRegisteredDeclaration(IDeclaration, self.typeName)
        if decl is None:
            raise SyntaxError("Unknown category:" + self.typeName)
        from prompto.declaration.CategoryDeclaration import CategoryDeclaration
        from prompto.declaration.EnumeratedNativeDeclaration import EnumeratedNativeDeclaration
        if isinstance(decl, EnumeratedNativeDeclaration):
            return decl.typ.checkMember(context, name)
        elif isinstance(decl, CategoryDeclaration):
            return self.checkCategoryMember(context, decl, name)
        else:
            raise SyntaxError("Not a category:" + self.typeName)


    def checkCategoryMember(self, context, decl, name):
        if decl.storable and "dbId" == name:
            return AnyType.instance
        elif decl.hasAttribute(context, name):
            ad = context.getRegisteredDeclaration(AttributeDeclaration, name)
            if ad is None:
                raise SyntaxError("Missing attribute:" + name)
            else:
                return ad.getType(context)
        elif "text" == name:
            return TextType.instance
        elif decl.hasMethod(context, name):
            method = decl.getMemberMethodsMap(context, name).getFirst()
            return MethodType(method)
        else:
            raise SyntaxError("No attribute:" + name + " in category:" + self.typeName)


    def checkStaticMember(self, context, name):
        from prompto.declaration.SingletonCategoryDeclaration import SingletonCategoryDeclaration

        decl = context.getRegisteredDeclaration (IDeclaration, self.typeName)
        if decl is None:
            raise SyntaxError("Unknown category:" + self.typeName)
        if isinstance(decl, IEnumeratedDeclaration):
            return decl.getType(context).checkStaticMember(context, name)
        elif isinstance(decl, SingletonCategoryDeclaration):
            return self.checkCategoryMember(context, decl, name)
        else:
            raise SyntaxError("No attribute:" + name + " in category:" + self.typeName)


    def getStaticMemberMethods(self, context, name):
        from prompto.declaration.SingletonCategoryDeclaration import SingletonCategoryDeclaration

        decl = self.getDeclaration(context)
        if isinstance(decl, IEnumeratedDeclaration):
            return decl.getType(context).getStaticMemberMethods(context, name)
        elif isinstance(decl, SingletonCategoryDeclaration):
            return decl.getType(context).getMemberMethods(context, name)
        else:
            return super().getStaticMemberMethods(context, name)


    def getStaticMemberValue(self, context, name):
        from prompto.declaration.SingletonCategoryDeclaration import SingletonCategoryDeclaration

        decl = self.getDeclaration(context)
        if isinstance(decl, IEnumeratedDeclaration):
            return decl.getType(context).getStaticMemberValue(context, name)
        elif isinstance(decl, SingletonCategoryDeclaration):
            singleton = context.loadSingleton(self)
            return singleton.getMemberValue(context, name, False)
        else:
            return super().getStaticMemberValue(context, name)


    def isDerivedFrom(self, context, other:IType):
        from prompto.declaration.CategoryDeclaration import CategoryDeclaration
        if not isinstance(other, CategoryType):
            return False
        try:
            thisDecl = self.getDeclaration(context)
            if isinstance(thisDecl, CategoryDeclaration):
                if thisDecl.derivedFrom is None:
                    return False
                for derived in thisDecl.derivedFrom:
                    cat = CategoryType(derived)
                    if cat==other or cat.isDerivedFrom(context, other):
                        return True
        except:
            return False
        return False



    def isAssignableFrom(self, context, other:IType):
        actual = self.resolve(context, None)
        other = other.resolve(context, None)
        if actual is self:
            return super().isAssignableFrom(context, other) or \
                (isinstance(other, CategoryType) and self.isAssignableFromCategory(context, other))
        else:
            return actual.isAssignableFrom(context, other)


    def isAssignableFromCategory(self, context, other: IType):
        return "Any" == self.typeName or \
               other.isDerivedFrom(context, self) or \
               other.isDerivedFromAnonymous(context, self)


    def isAnonymous(self):
        return self.typeName[0:1].islower()  # since it's the name of the argument


    def isDerivedFromAnonymous(self, context, other:IType):
        if not other.isAnonymous():
            return False
        try:
            from prompto.declaration.CategoryDeclaration import CategoryDeclaration
            thisDecl = self.getDeclaration(context)
            if isinstance(thisDecl, CategoryDeclaration):
                otherDecl = other.getDeclaration(context)
                if isinstance(otherDecl, CategoryDeclaration):
                    # an anonymous category extends 1 and only 1 category
                    baseName = otherDecl.derivedFrom[0]
                    # check we derive from root category ( if not extending 'any')
                    if not "any" == baseName and not thisDecl.isDerivedFrom(context, CategoryType(baseName)):
                        return False
                    for attribute in otherDecl.getAllAttributes(context):
                        if not thisDecl.hasAttribute(context, attribute):
                            return False
                    return True
        except:
            return False



    def isMoreSpecificThan(self, context, other):
        if isinstance(other, (NullType, AnyType, MissingType)):
            return True
        if not isinstance(other, CategoryType):
            return False
        if other.isAnonymous():
            return True
        from prompto.declaration.CategoryDeclaration import CategoryDeclaration
        selfDecl = context.getRegisteredDeclaration(CategoryDeclaration, self.typeName)
        if selfDecl.isDerivedFrom(context, other):
            return True
        return False



    def scoreMostSpecific(self, context, t1, t2):
        if t1 == t2:
            return Score.SIMILAR
        if self == t1:
            return Score.BETTER
        if self == t2:
            return Score.WORSE
        # since self derives from both t1 and t2, return the most specific of t1 and t2
        if t1.isMoreSpecificThan(context, t2):
            return Score.BETTER
        if t2.isMoreSpecificThan(context, t1):
            return Score.WORSE
        return Score.SIMILAR  # should never happen


    def newInstance(self, context):
        from prompto.declaration.CategoryDeclaration import CategoryDeclaration
        decl = context.getRegisteredDeclaration(CategoryDeclaration, self.typeName)
        return decl.newInstance(context)


    def getSortKeyReader(self, context, key):
        if key is None:
            key = UnresolvedIdentifier("key", Dialect.M)
        decl = self.getDeclaration(context)
        if decl.hasAttribute(context, str(key)):
            return self.getAttributeSortKeyReader(context, str(key))
        elif decl.hasMethod(context, str(key)):
            return self.getMemberMethodSortKeyReader(context, str(key))
        elif self.globalMethodExists(context, str(key)):
            return self.getGlobalMethodSortKeyReader(context, str(key))
        elif isinstance(key, ArrowExpression):
            return key.getSortKeyReader(context, self)
        else:
            return self.getExpressionSortKeyReader(context, key)


    def getAttributeSortKeyReader(self, context, name):
        return lambda o: o.getMemberValue(context, name)


    def getMemberMethodSortKeyReader(self, context, name):
        return None # TODO


    def getGlobalMethodSortKeyReader(self, context, name):
        from prompto.statement.MethodCall import MethodCall
        exp = ValueExpression(self, self.newInstance(context))
        arg = Argument(None, exp)
        args = ArgumentList(items=[arg])
        call = MethodCall(MethodSelector(name), args)

        def keyGetter(o):
            argument = call.arguments[0]
            argument.setExpression(ValueExpression(self, o))
            return call.interpret(context)

        return keyGetter


    def getExpressionSortKeyReader(self, context, exp):

        def keyGetter(o):
            co = context.newInstanceContext(o, None)
            return exp.interpret(co)

        return keyGetter


    def globalMethodExists(self, context, name):
        from prompto.statement.MethodCall import MethodCall
        from prompto.runtime.MethodFinder import MethodFinder
        try:
            exp = ValueExpression(self, self.newInstance(context))
            arg = Argument(None, exp)
            args = ArgumentList(items=[arg])
            proto = MethodCall(MethodSelector(name), args)
            finder = MethodFinder(context, proto)
            return finder.findMethod(True) is not None
        except PromptoError:
            return False


    def convertPythonValueToPromptoValue(self, context, value, returnType):
        decl = self.getDeclaration(context)
        if decl is None:
            return super(CategoryType, self).convertPythonValueToPromptoValue(context, value, returnType)
        if isinstance(decl, IEnumeratedDeclaration):
            return self.loadEnumValue(context, decl, value)
        if DataStore.instance.isDbIdType(type(value)):
            value = DataStore.instance.fetchUnique(value)
        if isinstance(value, IStored):
            return decl.newInstanceFromStored(context, value)
        else:
            return super(CategoryType, self).convertPythonValueToPromptoValue(context, value, returnType)


    def loadEnumValue(self, context, decl, name):
        return context.getRegisteredValue( Symbol, name)


    def getMemberMethods(self, context, name):
        from prompto.declaration.ConcreteCategoryDeclaration import ConcreteCategoryDeclaration
        cd = self.getDeclaration(context)
        if not isinstance(cd, ConcreteCategoryDeclaration):
            raise SyntaxError("Unknown category:" + self.typeName)
        else:
            return cd.getMemberMethodsMap(context, name).values()

