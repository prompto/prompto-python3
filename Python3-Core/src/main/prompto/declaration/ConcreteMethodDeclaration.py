from prompto.argument.CategoryArgument import CategoryArgument
from prompto.argument.CodeArgument import CodeArgument
from prompto.declaration.BaseMethodDeclaration import BaseMethodDeclaration
from prompto.statement.StatementList import StatementList
from prompto.type.DictType import DictType
from prompto.type.TextType import TextType
from prompto.type.VoidType import VoidType


class ConcreteMethodDeclaration ( BaseMethodDeclaration ):

    def __init__(self, name, arguments, returnType, statements):
        super(ConcreteMethodDeclaration, self).__init__(name, arguments, returnType)
        if statements is None:
            statements = StatementList()
        self.statements = statements
        self.declarationOf = None
        from prompto.statement.DeclarationStatement import DeclarationStatement
        for statement in statements:
            if isinstance(statement, DeclarationStatement):
                statement.declaration.closureOf = self


    def getStatements(self):
        return self.statements


    def checkMember(self, category, context):
        context = context.newInstanceContext(None, category.getType(context), False)
        return self.checkChild(context)


    def check(self, context, isStart):
        if self.canBeChecked(context):
            return self.fullCheck(context, isStart)
        else:
            return VoidType.instance


    def canBeChecked(self, context):
        if context.isGlobalContext():
            return not self.mustBeBeCheckedInCallContext(context)
        else:
            return True


    def mustBeBeCheckedInCallContext(self, context):
        # if at least one argument is 'Code'
        if self.arguments is None:
            return False
        for arg in self.arguments:
            if isinstance(arg, CodeArgument):
                return True
        return False


    def fullCheck(self, context, isStart):
        if isStart:
            context = context.newLocalContext()
            self.registerArguments(context)
        if self.arguments is not None:
            self.arguments.check(context)
        return self.statements.check(context, self.returnType)


    def checkChild(self, context):
        if self.arguments is not None:
            self.arguments.check(context)
        child = context.newChildContext()
        self.registerArguments(child)
        return self.statements.check(child, self.returnType)


    def interpret(self, context):
        context.enterMethod(self)
        try:
            return self.statements.interpret(context)
        finally:
            context.leaveMethod(self)


    def isEligibleAsMain(self):
        if self.arguments is None or self.arguments.isEmpty():
            return True
        if self.arguments.size()==1:
            arg = self.arguments[0]
            if isinstance(arg, CategoryArgument):
                itype = arg.getType()
                if isinstance(itype, DictType):
                    return itype.itemType==TextType.instance
        return super(ConcreteMethodDeclaration, self).isEligibleAsMain()


    def toDialect(self, writer):
        if writer.isGlobalContext():
            writer = writer.newLocalWriter()
        self.registerArguments(writer.context)
        super(ConcreteMethodDeclaration, self).toDialect(writer)


    def toMDialect(self, writer):
        writer.append("def ")
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


    def toEDialect(self, writer):
        writer.append("define ")
        writer.append(self.name)
        writer.append(" as method ")
        self.arguments.toDialect(writer)
        if self.returnType is not None and self.returnType is not VoidType.instance:
            writer.append("returning ")
            self.returnType.toDialect(writer)
            writer.append(" ")
        writer.append("doing:\n")
        writer.indent()
        self.statements.toDialect(writer)
        writer.dedent()


    def toODialect(self, writer):
        if self.returnType is not None and self.returnType is not VoidType.instance:
            self.returnType.toDialect(writer)
            writer.append(" ")
        writer.append("method ")
        writer.append(self.name)
        writer.append(" (")
        self.arguments.toDialect(writer)
        writer.append(") {\n")
        writer.indent()
        self.statements.toDialect(writer)
        writer.dedent()
        writer.append("}\n")
