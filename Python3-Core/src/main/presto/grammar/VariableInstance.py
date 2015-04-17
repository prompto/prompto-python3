from presto.grammar.IAssignableInstance import IAssignableInstance
from presto.grammar.INamedValue import INamedValue
from presto.runtime.Variable import Variable
from presto.error.SyntaxError import SyntaxError


class VariableInstance(IAssignableInstance):
    def __init__(self, name):
        super(VariableInstance, self).__init__()
        self.name = name

    def getName(self):
        return self.name

    def __str__(self):
        return self.name

    def toDialect(self, writer):
        writer.append(self.name)

    def checkAssignValue(self, context, expression):
        type = expression.check(context)
        actual = context.getRegisteredValue(INamedValue, self.name)
        if actual == None:
            actualType = expression.check(context)
            context.registerValue(Variable(self.name, actualType))
        else:
            # need to check type compatibility
            actualType = actual.getType(context)
            type.checkAssignableTo(context, actualType)

    def checkAssignMember(self, context, memberName):
        actual = context.getRegisteredValue(INamedValue, self.name)
        if actual == None:
            raise SyntaxError("Unknown variable:" + self.name)

    def assign(self, context, expression):
        value = expression.interpret(context)
        if context.getRegisteredValue(INamedValue, self.name) == None:
            context.registerValue(Variable(self.name, value.type))
        context.setValue(self.name, value)

    def interpret(self, context):
        return context.getValue(self.name)
