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

    def toDialect(self, writer, expression):
        if expression is not None:
            try:
                actual = writer.context.getRegisteredValue(INamedValue, self.name)
                if actual == None:
                    typ = expression.check(writer.context)
                    writer.context.registerValue(Variable(self.name, typ))
            except:
                pass
        writer.append(self.name)

    def checkAssignValue(self, context, expression):
        actual = context.getRegisteredValue(INamedValue, self.name)
        if actual == None:
            actualType = expression.check(context)
            context.registerValue(Variable(self.name, actualType))
        else:
            # need to check type compatibility
            actualType = actual.getType(context)
            typ = expression.check(context)
            typ.checkAssignableTo(context, actualType)

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
