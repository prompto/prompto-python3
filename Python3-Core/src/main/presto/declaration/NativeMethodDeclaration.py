from presto.declaration.ConcreteMethodDeclaration import *


class NativeMethodDeclaration(ConcreteMethodDeclaration):

    def __init__(self, name, arguments, returnType, instructions):
        super(NativeMethodDeclaration, self).__init__(name, arguments, returnType, instructions)

    def interpret(self, context):
        context.enterMethod(self)
        try:
            result = self.statements.interpretNative(context, self.returnType)
            return self.castToReturnType(context, result)
        finally:
            context.leaveMethod(self)

    def castToReturnType(self, context, value):
        # can only cast to specified type, and if required
        if self.returnType is not None and value is not None and not value.type.isAssignableTo(context, self.returnType):
            # only cast if implemented, on a per type basis
            if self.returnType.nativeCast:
                value = self.returnType.nativeCast(context, value)
        return value

    def check(self, context):
        checked = self.fullCheck(context, True)
        return checked if self.returnType is None else self.returnType

    def toPDialect(self, writer):
        writer.append("def native ")
        writer.append(self.name)
        writer.append(" (")
        self.arguments.toDialect(writer)
        writer.append(")")
        if self.returnType is not None and self.returnType is not VoidType.instance:
            writer.append("->")
            self.returnType.toDialect(writer)
        writer.append(":\n")
        writer.indent()
        self.statements.toDialect(writer)
        writer.dedent()

    def toODialect(self, writer):
        if self.returnType is not None and self.returnType is not VoidType.instance:
            self.returnType.toDialect(writer)
            writer.append(" ")
        writer.append("native method ")
        writer.append(self.name)
        writer.append(" (")
        self.arguments.toDialect(writer)
        writer.append(") {\n")
        writer.indent()
        for stmt in self.statements:
            stmt.toDialect(writer)
            writer.newLine()
        writer.dedent()
        writer.append("}\n")

    def toEDialect(self, writer):
        writer.append("define ")
        writer.append(self.name)
        writer.append(" as: native method ")
        self.arguments.toDialect(writer)
        if self.returnType is not None and self.returnType is not VoidType.instance:
            writer.append("returning: ")
            self.returnType.toDialect(writer)
            writer.append(" ")
        writer.append("doing:\n")
        writer.indent()
        self.statements.toDialect(writer)
        writer.dedent()
        writer.append("\n")
