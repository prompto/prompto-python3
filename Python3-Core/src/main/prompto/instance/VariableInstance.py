from prompto.error.SyntaxError import SyntaxError
from prompto.grammar.INamedValue import INamedValue
from prompto.instance.IAssignableInstance import IAssignableInstance
from prompto.runtime.Variable import Variable
from prompto.value.NullValue import NullValue



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

    def checkAssignValue(self, context, valueType):
        actual = context.getRegisteredValue(INamedValue, self.name)
        if actual == None:
            context.registerValue(Variable(self.name, valueType))
            return valueType
        else:
            # need to check type compatibility
            actualType = actual.getType(context)
            valueType.checkAssignableTo(context, actualType)
            return actualType



    def checkAssignMember(self, context, name, valueType):
        actual = context.getRegisteredValue(INamedValue, self.name)
        if actual == None:
            raise SyntaxError("Unknown variable:" + self.name)
        return valueType



    def checkAssignItem(self, context, itemType, valueType):
        actual = context.getRegisteredValue(INamedValue, self.name)
        if actual == None:
            raise SyntaxError("Unknown variable:" + self.name)
        parentType = actual.getType(context)
        return parentType.checkItem(context, itemType)



    def assign(self, context, expression):
        value = expression.interpret(context)
        if context.getRegisteredValue(INamedValue, self.name) == None:
            typ = value.type if value is not NullValue.instance else expression.check(context)
            context.registerValue(Variable(self.name, typ))
        context.setValue(self.name, value)

    def interpret(self, context):
        return context.getValue(self.name)
