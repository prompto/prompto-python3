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
        actual = context.getRegisteredValue(INamedInstance, self.parameter.getName())
        if actual is None:
            actualType = self.getExpression().check(context)
            context.registerValue(Variable(self.parameter.getName(), actualType))
        else:
            # need to check type compatibility
            actualType = actual.getType(context)
            newType = self.getExpression().check(context)
            actualType.checkAssignableFrom(context, newType)
        return VoidType.instance


    def checkActualType(self, context, requiredType, expression, checkInstance):
        from prompto.type.CategoryType import CategoryType
        actualType = None
        isArrow = self.isArrowExpression(requiredType, expression)
        if isArrow:
            actualType = self.checkArrowExpression(context, requiredType, expression)
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
        if not isinstance(requiredType, MethodType):
            return False
        if isinstance(expression, ContextualExpression):
            expression = expression.expression
        return isinstance(expression, ArrowExpression)


    def interpret(self, context):
        if context.getRegisteredValue(INamedInstance, self.parameter.getName()) is None:
            context.registerValue(Variable(self.parameter.getName(), self.getExpression()))
        context.setValue(self.parameter.getName(), self.getExpression().interpret(context))
        return None


    def resolve(self, context, methodDeclaration, checkInstance):
        from prompto.type.CategoryType import CategoryType
        from prompto.expression.ArrowExpression import ArrowExpression
        # since we support implicit members, it's time to resolve them
        name = self.parameter.getName()
        expression = self.getExpression()
        argument = methodDeclaration.getArguments().find(name)
        requiredType = argument.getType(context)
        checkArrow = isinstance(requiredType, MethodType) and isinstance(expression, ContextualExpression) and isinstance(expression.expression, ArrowExpression)
        actualType = requiredType.checkArrowExpression(context, expression) if checkArrow else expression.check(context.getCallingContext())
        if checkInstance and isinstance(actualType, CategoryType):
            value = expression.interpret(context.getCallingContext())
            if isinstance(value, IInstance):
                actualType = value.getType()
        if not requiredType.isAssignableFrom(context, actualType) and isinstance(actualType, CategoryType):
            from prompto.expression.MemberSelector import MemberSelector
            expression = MemberSelector(name, expression)
        return expression


    def makeArgument(self, context, declaration):
        parameter = self.parameter
        # when 1st argument, can be unnamed
        if parameter is None:
            if len(declaration.getArguments()) == 0:
                raise SyntaxError("Method has no argument")
            parameter = declaration.getArguments()[0]
        else:
            parameter = declaration.getArguments().find(self.getName())
        if parameter is None:
            raise SyntaxError("Method has no argument:" + self.getName())
        expression = ContextualExpression(context, self.getExpression())
        return Argument(parameter, expression)
