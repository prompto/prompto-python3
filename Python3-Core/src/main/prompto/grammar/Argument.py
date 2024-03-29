from prompto.grammar.IDialectElement import IDialectElement
from prompto.grammar.INamedInstance import INamedInstance
from prompto.runtime.Variable import Variable
from prompto.type.MethodType import MethodType
from prompto.type.VoidType import VoidType
from prompto.value.ContextualExpression import ContextualExpression
from prompto.value.IInstance import IInstance
from prompto.error.SyntaxError import SyntaxError

class Argument(IDialectElement):

    def __init__(self, parameter, expression):
        super(Argument, self).__init__()
        self.parameter = parameter
        self.expression = expression


    def getParameter(self):
        return self.parameter


    def getName(self):
        return self.parameter.getName()


    def getExpression(self):
        from prompto.expression.InstanceExpression import InstanceExpression
        return self.expression if self.expression is not None else InstanceExpression(self.parameter.name)


    def setExpression(self, expression):
        self.expression = expression


    def __str__(self):
        if self.parameter is None:
            return str(self.expression)
        else:
            return str(self.expression) + " as " + self.parameter.getName()


    def toODialect(self, writer):
        if self.expression is None:
            writer.append(self.parameter.getName())
        else:
            if self.parameter is not None:
                writer.append(self.parameter.getName())
                writer.append(" = ")
            self.expression.toDialect(writer)


    def toMDialect(self, writer):
        if self.expression is None:
            writer.append(self.parameter.getName())
        else:
            if self.parameter is not None:
                writer.append(self.parameter.getName())
                writer.append(" = ")
            self.expression.toDialect(writer)


    def toEDialect(self, writer):
        if self.expression is None:
            writer.append(self.parameter.getName())
        else:
            self.expression.toDialect(writer)
            if self.parameter is not None:
                writer.append(" as ")
                writer.append(self.parameter.getName())


    def __eq__(self, obj):
        if id(obj) == id(self):
            return True
        if obj is None:
            return False
        if not isinstance(obj, Argument):
            return False
        return self.getParameter() == obj.getParameter() and self.getExpression() == obj.getExpression()


    def check(self, context):
        if self.expression is None:
            self.checkParameterOnly(context)
        else:
            self.checkParameterAndExpression(context)

    def checkParameterOnly(self, context):
        registered = context.getRegisteredValue(INamedInstance, self.parameter.getName())
        if registered is None:
            raise SyntaxError("Unknown attribute: " + self.parameter.getName())
        requiredType = self.parameter.check(context)
        actualType = registered.getType(context)
        requiredType.checkAssignableFrom(context, actualType)

    def checkParameterAndExpression(self, context):
        requiredType = self.parameter.check(context)
        actualType = self.getExpression().check(context)
        requiredType.checkAssignableFrom(context, actualType)

    def checkActualType(self, context, requiredType, expression, checkInstance):
        from prompto.type.CategoryType import CategoryType
        actualType = None
        isArrow = self.isArrowExpression(requiredType, expression)
        if isArrow:
            if isinstance(requiredType, MethodType):
                actualType = self.checkArrowExpression(context, requiredType, expression)
            else:
                actualType = VoidType.instance
        elif isinstance(requiredType, MethodType):
            actualType = expression.checkReference(context.calling)
        else:
            actualType = expression.check(context)
        # retrieve actual runtime type
        if checkInstance and isinstance(actualType, CategoryType):
            value = expression.interpret(context.calling)
            if isinstance(value, IInstance):
                actualType = value.getType()
        return actualType


    def checkArrowExpression(self, context, requiredType, expression):
        from prompto.expression.ArrowExpression import ArrowExpression
        context = expression.calling if isinstance(expression, ContextualExpression) else context.calling
        arrow = expression if isinstance(expression, ArrowExpression) else expression.expression
        return requiredType.checkArrowExpression(context, arrow)


    def isArrowExpression(self, requiredType, expression):
        from prompto.expression.ArrowExpression import ArrowExpression
        if isinstance(expression, ContextualExpression):
            expression = expression.expression
        return isinstance(expression, ArrowExpression)


    def interpret(self, context):
        if context.getRegisteredValue(INamedInstance, self.parameter.getName()) is None:
            context.registerValue(Variable(self.parameter.getName(), self.getExpression()))
        context.setValue(self.parameter.getName(), self.getExpression().interpret(context))
        return None


    def resolve(self, context, methodDeclaration, checkInstance):
        parameter = self.findParameter(methodDeclaration)
        return self.doResolve(context, parameter, checkInstance)

    def findParameter(self, methodDeclaration):
        return methodDeclaration.parameters.find(self.parameter.name)

    def doResolve(self, context, parameter, checkInstance):
        # since we support implicit members, it's time to resolve them
        expression = self.getExpression()
        requiredType = parameter.getType(context)
        actualType = self.checkActualType(context, requiredType, expression, checkInstance)
        assignable = requiredType.isAssignableFrom(context, actualType)
        # try passing category member
        from prompto.type.CategoryType import CategoryType
        if not assignable and isinstance(actualType, CategoryType):
            from prompto.expression.MemberSelector import MemberSelector
            expression = MemberSelector(expression, parameter.name)
        return expression

    def makeArgument(self, context, declaration):
        parameter = self.parameter
        # when 1st argument, can be unnamed
        if parameter is None:
            if len(declaration.parameters) == 0:
                raise SyntaxError("Method has no parameter")
            parameter = declaration.parameters[0]
        else:
            parameter = declaration.parameters.find(self.getName())
        if parameter is None:
            raise SyntaxError("Method has no such parameter:" + self.getName())
        expression = ContextualExpression(context, self.getExpression())
        return Argument(parameter, expression)
