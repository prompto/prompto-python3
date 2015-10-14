from prompto.grammar.IAssignableInstance import IAssignableInstance
from prompto.grammar.INamedValue import INamedValue
from prompto.runtime.Variable import Variable
from prompto.error.SyntaxError import SyntaxError


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
        typ = expression.check(context)
        actual = context.getRegisteredValue(INamedValue, self.name)
        if actual == None:
            context.registerValue(Variable(self.name, typ))
        else:
            # need to check type compatibility
            actualType = actual.getType(context)
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
