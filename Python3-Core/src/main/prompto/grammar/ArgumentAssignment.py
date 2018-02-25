from prompto.grammar.IDialectElement import IDialectElement
from prompto.runtime.Variable import *
from prompto.type.VoidType import *
from prompto.value.ContextualExpression import *
from prompto.value.IInstance import *
from prompto.error.SyntaxError import SyntaxError

class ArgumentAssignment(IDialectElement):

    def __init__(self, argument, expression):
        super(ArgumentAssignment, self).__init__()
        self.argument = argument
        self.expression = expression

    def getArgument(self):
        return self.argument

    def getName(self):
        return self.argument.getName()

    def getExpression(self):
        from prompto.expression.InstanceExpression import InstanceExpression
        return self.expression if self.expression is not None else InstanceExpression(self.argument.name)

    def setExpression(self, expression):
        self.expression = expression

    def __str__(self):
        if self.argument is None:
            return str(self.expression)
        else:
            return str(self.expression) + " as " + self.argument.getName()

    def toODialect(self, writer):
        if self.expression is None:
            writer.append(self.argument.getName())
        else:
            if self.argument is not None:
                writer.append(self.argument.getName())
                writer.append(" = ")
            self.expression.toDialect(writer)


    def toMDialect(self, writer):
        if self.expression is None:
            writer.append(self.argument.getName())
        else:
            if self.argument is not None:
                writer.append(self.argument.getName())
                writer.append(" = ")
            self.expression.toDialect(writer)

    def toEDialect(self, writer):
        if self.expression is None:
            writer.append(self.argument.getName())
        else:
            self.expression.toDialect(writer)
            if self.argument is not None:
                writer.append(" as ")
                writer.append(self.argument.getName())

    def __eq__(self, obj):
        if id(obj) == id(self):
            return True
        if obj is None:
            return False
        if not isinstance(obj, ArgumentAssignment):
            return False
        return self.getArgument() == obj.getArgument() and self.getExpression() == obj.getExpression()

    def check(self, context):
        actual = context.getRegisteredValue(INamedValue, self.argument.getName())
        if actual is None:
            actualType = self.getExpression().check(context)
            context.registerValue(Variable(self.argument.getName(), actualType))
        else:
            # need to check type compatibility
            actualType = actual.getType(context)
            newType = self.getExpression().check(context)
            actualType.checkAssignableFrom(context, newType)
        return VoidType.instance

    def interpret(self, context):
        if context.getRegisteredValue(INamedValue, self.argument.getName()) is None:
            context.registerValue(Variable(self.argument.getName(), self.getExpression()))
        context.setValue(self.argument.getName(), self.getExpression().interpret(context))
        return None

    def resolve(self, context, methodDeclaration, checkInstance):
        from prompto.type.CategoryType import CategoryType
        # since we support implicit members, it's time to resolve them
        name = self.argument.getName()
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

    def makeAssignment(self, context, declaration):
        argument = self.argument
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
        return ArgumentAssignment(argument, expression)
