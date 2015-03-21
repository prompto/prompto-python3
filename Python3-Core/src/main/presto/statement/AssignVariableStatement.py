from presto.expression.MemberSelector import MemberSelector
from presto.grammar.INamedValue import INamedValue
from presto.runtime.Variable import Variable
from presto.statement.SimpleStatement import SimpleStatement
from presto.type.CategoryType import CategoryType
from presto.type.ResourceType import ResourceType
from presto.type.VoidType import VoidType
from presto.value.IInstance import IInstance


class AssignVariableStatement ( SimpleStatement ):

    def __init__(self, name, expression):
        super(AssignVariableStatement, self).__init__()
        self.name = name
        self.expression = expression

    def getName(self):
        return self.name

    def getExpression(self):
        return self.expression

    def setExpression(self, expression):
        self.expression = expression

    def __str__(self):
        return self.name + " = " + str(self.expression)

    def checkResource(self, context):
        expressionType = self.expression.check(context)
        if not isinstance(expressionType, ResourceType):
            raise SyntaxError("Not a resource!")
        actual = context.getRegisteredValue(INamedValue,self.name)
        if actual is None:
            context.registerValue(Variable(self.name, expressionType))
        else:
            # need to check type compatibility
            actualType = actual.getType(context)
            expressionType.checkAssignableTo(context,actualType)
        return VoidType.instance

    def __eq__(self, obj):
        if id(obj)==id(self):
            return True
        if obj is None:
            return False
        if not isinstance(obj, AssignVariableStatement):
            return False
        return self.name==obj.name and self.getExpression()==obj.getExpression()

    def check(self, context):
        actual = context.getRegisteredValue(INamedValue,self.name)
        if actual is None:
            actualType = self.expression.check(context)
            context.registerValue(Variable(self.name, actualType))
        else:
            # need to check type compatibility
            actualType = actual.getType(context)
            newType = self.expression.check(context)
            newType.checkAssignableTo(context,actualType)
        return VoidType.instance

    def interpret(self, context):
        if context.getRegisteredValue(INamedValue,self.name)is None:
            actualType = self.expression.check(context)
            context.registerValue(Variable(self.name, actualType))
        context.setValue(self.name, self.expression.interpret(context))
        return None

    def resolve(self, context, methodDeclaration,checkInstance):
        # since we support implicit members, it's time to resolve them
        expression = self.getExpression()
        argument = methodDeclaration.getArguments().find(self.name)
        required = argument.getType(context)
        actual = expression.check(context.getCallingContext())
        if checkInstance and isinstance(actual, CategoryType):
            value = expression.interpret(context.getCallingContext())
            if isinstance(value, IInstance):
                actual = value.getType()
        if not actual.isAssignableTo(context, required) and isinstance(actual, CategoryType):
            expression = MemberSelector(expression,self.name)
        return expression

    def toDialect(self, writer):
        writer.append(self.name)
        writer.append(" = ")
        self.expression.toDialect(writer)
