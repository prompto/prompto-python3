from prompto.error.NotMutableError import NotMutableError
from prompto.instance.IAssignableInstance import IAssignableInstance


class MemberInstance ( IAssignableInstance ):

    def __init__(self, parent, name):
        self.parent = parent
        self.name = name

    def setParent(self, parent):
        self.parent = parent

    def getName(self):
        return self.name



    def __str__(self):
        return str(self.parent) + "." + self.name



    def toDialect(self, writer, expression):
        self.parent.toDialect(writer, None)
        writer.append(".")
        writer.append(self.name)



    def checkAssignValue(self, context, valueType):
        return self.parent.checkAssignMember(context, self.name, valueType)



    def checkAssignMember(self, context, name, valueType):
        self.parent.checkAssignMember(context, self.name, None)
        return valueType # TODO



    def checkAssignItem(self, context, itemType, valueType):
        return valueType # TODO



    def assign(self, context, expression):
        root = self.parent.interpret(context)
        if not root.mutable:
            raise NotMutableError()
        value = expression.interpret(context)
        root.SetMember(context, self.name, value)

    def interpret(self, context):
        root = self.parent.interpret(context)
        return root.GetMember(context, self.name, True)
