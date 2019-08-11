from prompto.grammar.IDialectElement import IDialectElement
from prompto.runtime.Variable import *
from prompto.type.VoidType import *
from prompto.value.ContextualExpression import *
from prompto.value.IInstance import *
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
        actual = context.getRegisteredValue(INamedValue, self.parameter.getName())
        if actual is None:
            actualType = self.getExpression().check(context)
            context.registerValue(Variable(self.parameter.getName(), actualType))
        else:
            # need to check type compatibility
            actualType = actual.getType(context)
            newType = self.getExpression().check(context)
            actualType.checkAssignableFrom(context, newType)
        return VoidType.instance


    def interpret(self, context):
        if context.getRegisteredValue(INamedValue, self.parameter.getName()) is None:
            context.registerValue(Variable(self.parameter.getName(), self.getExpression()))
        context.setValue(self.parameter.getName(), self.getExpression().interpret(context))
        return None


    def resolve(self, context, methodDeclaration, checkInstance):
        from prompto.type.CategoryType import CategoryType
        # since we support implicit members, it's time to resolve them
        name = self.parameter.getName()
        expression = self.getExpression()
        argument = methodDeclaration.getArguments().find(name)
        required = argument.getType(context)
        actual = expression.check(context.getCallingContext())
        if checkInstance and isinstance(actual, CategoryType):
            value = expression.interpret(context.getCallingContext())
            if isinstance(value, IInstance):
                actual = value.getType()
        if not required.isAssignableFrom(context, actual) and isinstance(actual, CategoryType):
            from prompto.expression.MemberSelector import MemberSelector
            expression = MemberSelector(name, expression)
        return expression


    def makeArgument(self, context, declaration):
        argument = self.parameter
        # when 1st argument, can be unnamed
        if argument is None:
            if len(declaration.getArguments()) == 0:
                raise SyntaxError("Method has no argument")
            argument = declaration.getArguments()[0]
        else:
            argument = declaration.getArguments().find(self.getName())
        if argument is None:
            raise SyntaxError("Method has no argument:" + self.getName())
        expression = ContextualExpression(context, self.getExpression())
        return Argument(argument, expression)
