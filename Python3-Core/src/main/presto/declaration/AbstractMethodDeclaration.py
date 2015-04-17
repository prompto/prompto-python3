from presto.declaration.BaseMethodDeclaration import BaseMethodDeclaration
from presto.type.VoidType import VoidType


class AbstractMethodDeclaration(BaseMethodDeclaration):

    def __init__(self, name, arguments, returnType):
        super(AbstractMethodDeclaration, self).__init__(name, arguments)
        self.returnType = returnType if returnType != None else VoidType.instance

    def checkMember(self, category, context):
        pass  # TODO

    def check(self, context):
        if self.arguments != None:
            self.arguments.check(context)
        local = context.newLocalContext()
        self.registerArguments(local)
        return self.returnType

    def interpret(self, context):
        raise SyntaxError("Should never get there !")

    def toPDialect(self, writer):
        writer.append("abstract def ")
        writer.append(self.name)
        writer.append(" (")
        self.arguments.toDialect(writer)
        writer.append(")")
        if self.returnType is not None and self.returnType is not VoidType.instance:
            writer.append("->")
            self.returnType.toDialect(writer)

    def toODialect(self, writer):
        writer.append("abstract ")
        if self.returnType is not None and self.returnType is not VoidType.instance:
            self.returnType.toDialect(writer)
            writer.append(" ")
        writer.append("method ")
        writer.append(self.name)
        writer.append(" (")
        self.arguments.toDialect(writer)
        writer.append(");")

    def toEDialect(self, writer):
        writer.append("define ")
        writer.append(self.name)
        writer.append(" as: abstract method ")
        self.arguments.toDialect(writer)
        if self.returnType is not None and self.returnType is not VoidType.instance:
            writer.append("returning: ")
            self.returnType.toDialect(writer)

