from prompto.param.BaseParameter import BaseParameter
from prompto.param.ITypedParameter import ITypedParameter
from prompto.error.SyntaxError import SyntaxError
from prompto.type.MethodType import MethodType


class CategoryParameter(BaseParameter, ITypedParameter):

    def __init__(self, itype, name, default=None):
        super(CategoryParameter, self).__init__(name)
        self.itype = itype
        self.resolved = None
        self.defaultExpression = default


    def getSignature(self, dialect):
        return self.getProto()


    def getProto(self):
        return self.itype.typeName


    def __str__(self):
        return self.name + ':' + self.getProto()


    def __eq__(self, obj):
        if id(obj) == id(self):
            return True
        if obj is None:
            return False
        if not isinstance(obj, CategoryParameter):
            return False
        return self.getType() == obj.getType() \
            and self.getName() == obj.getName()


    def setMutable(self, mutable):
        self.itype.mutable = mutable
        self.mutable = mutable


    def register(self, context):
        actual = context.contextForValue(self.name)
        if actual is self:
            raise SyntaxError("Duplicate argument: \"" + self.name + "\"")
        self.resolve(context)
        if self.resolved is self.itype:
            context.registerValue(self)
        else:
            param = CategoryParameter(self.resolved, self.name)
            param.setMutable(self.mutable)
            context.registerValue(param)
        if self.defaultExpression is not None:
            value = self.defaultExpression.interpret(context)
            context.setValue(self.name, value)

    def check(self, context):
        self.resolve(context)
        self.resolved.checkExists(context)
        return self.itype

    def checkValue(self, context, expression):
        from prompto.value.ContextualExpression import ContextualExpression
        from prompto.expression.ArrowExpression import ArrowExpression
        isArrow = isinstance(expression, ContextualExpression) and isinstance(expression.expression, ArrowExpression)
        if isArrow:
            return self.checkArrowValue(context, expression)
        else:
            return self.checkSimpleValue(context, expression)

    def checkArrowValue(self, context, expression):
        decl = self.getAbstractMethodDeclaration(context)
        from prompto.value.ArrowValue import ArrowValue
        return ArrowValue(decl, expression.calling, expression.expression) # TODO check

    def getAbstractMethodDeclaration(self, context):
        from prompto.runtime.Context import MethodDeclarationMap
        methods = context.getRegisteredDeclaration(MethodDeclarationMap, self.itype.typeName)
        if methods is not None:
            return next((m for m in methods.values() if m.isAbstract()), None)
        else:
            return None

    def checkSimpleValue(self, context, expression):
        self.resolve(context)
        if isinstance(self.resolved, MethodType):
            return expression.interpretReference(context)
        else:
            return super(CategoryParameter, self).checkValue(context, expression)


    def resolve(self, context):
        if self.resolved is None:
            self.resolved = self.itype.resolve(context, None).asMutable(context, self.mutable)


    def getType(self, context=None):
        return self.itype


    def toDialect(self, writer):
        if self.mutable:
            writer.append("mutable ")
        super(CategoryParameter, self).toDialect(writer)
        if self.defaultExpression is not None:
            writer.append(" = ")
            self.defaultExpression.toDialect(writer)


    def toEDialect(self, writer):
        self.itype.toDialect(writer, True)
        writer.append(' ')
        writer.append(self.name)


    def toODialect(self, writer):
        self.itype.toDialect(writer, True)
        writer.append(' ')
        writer.append(self.name)

    def toMDialect(self, writer):
        writer.append(self.name)
        writer.append(':')
        self.itype.toDialect(writer, True)
