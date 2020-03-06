from prompto.error.SyntaxError import SyntaxError
from prompto.grammar.INamedValue import INamedValue
from prompto.instance.IAssignableInstance import IAssignableInstance
from prompto.runtime.Variable import Variable
from prompto.type.CategoryType import CategoryType
from prompto.type.DocumentType import DocumentType



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
                if actual is None:
                    typ = expression.check(writer.context)
                    writer.context.registerValue(Variable(self.name, typ))
            except:
                pass
        writer.append(self.name)

    def checkAssignValue(self, context, valueType):
        actual = context.getRegisteredValue(INamedValue, self.name)
        if actual is None:
            context.registerValue(Variable(self.name, valueType))
            return valueType
        else:
            # need to check type compatibility
            actualType = actual.getType(context)
            actualType.checkAssignableFrom(context, valueType)
            return actualType



    def checkAssignMember(self, context, name, valueType):
        actual = context.getRegisteredValue(INamedValue, self.name)
        if actual is None:
            raise SyntaxError("Unknown variable:" + self.name)
        thisType = actual.getType(context)
        if thisType is DocumentType.instance:
            return valueType
        else:
            if isinstance(thisType, CategoryType) and not thisType.mutable:
                raise SyntaxError("Not mutable:" + self.name)
            requiredType = thisType.checkMember(context, name)
            if requiredType is not None and not requiredType.isAssignableFrom(context, valueType):
                raise SyntaxError("Incompatible types:" + requiredType.typename + " and " + valueType.typename)
            return valueType



    def checkAssignItem(self, context, itemType, valueType):
        actual = context.getRegisteredValue(INamedValue, self.name)
        if actual is None:
            raise SyntaxError("Unknown variable:" + self.name)
        parentType = actual.getType(context)
        return parentType.checkItem(context, itemType)



    def assign(self, context, expression):
        value = expression.interpret(context)
        if context.getRegisteredValue(INamedValue, self.name) is None:
            itype = expression.check(context)
            context.registerValue(Variable(self.name, itype))
        context.setValue(self.name, value)

    def interpret(self, context):
        return context.getValue(self.name)
