from prompto.param.CategoryParameter import CategoryParameter
from prompto.param.CodeParameter import CodeParameter
from prompto.declaration.BaseMethodDeclaration import BaseMethodDeclaration
from prompto.statement.StatementList import StatementList
from prompto.type.DictType import DictType
from prompto.type.IType import IType
from prompto.type.TextType import TextType
from prompto.type.VoidType import VoidType
from prompto.error.SyntaxError import SyntaxError

class ConcreteMethodDeclaration ( BaseMethodDeclaration ):

    def __init__(self, name, arguments, returnType, statements):
        super(ConcreteMethodDeclaration, self).__init__(name, arguments, returnType)
        if statements is None:
            statements = StatementList()
        self.statements = statements
        self.declarationOf = None
        self.beingChecked = False
        from prompto.statement.DeclarationStatement import DeclarationStatement
        for statement in statements:
            if isinstance(statement, DeclarationStatement):
                statement.declaration.closureOf = self

    def getStatements(self):
        return self.statements

    def checkStart(self, context):
        if self.canBeChecked(context):
            return self.recursiveCheck(context, True)
        else:
            return VoidType.instance

    def check(self, context):
        if self.canBeChecked(context):
            return self.recursiveCheck(context, False)
        else:
            return VoidType.instance

    def canBeChecked(self, context):
        if context.isGlobalContext():
            return not self.mustBeBeCheckedInCallContext(context)
        else:
            return True

    def mustBeBeCheckedInCallContext(self, context):
        # if at least one argument is 'Code'
        if self.parameters is None:
            return False
        for arg in self.parameters:
            if isinstance(arg, CodeParameter):
                return True
        return False

    def recursiveCheck(self, context, isStart:bool):
        if self.beingChecked:
            if self.returnType is None:
                raise SyntaxError("Cannot check recursive method " + self.name + " without a return type!")
            else:
                return self.returnType
        else:
            self.beingChecked = True
            try:
                return self.fullCheck(context, isStart)
            finally:
                self.beingChecked = False

    def fullCheck(self, context, isStart:bool):
        if isStart:
            context = context.newLocalContext()
            self.registerParameters(context)
        if self.parameters is not None:
            self.parameters.check(context)
        return self.checkStatements(context, self.returnType)


    def checkChild(self, context):
        if self.parameters is not None:
            self.parameters.check(context)
        context = context.newChildContext()
        self.registerParameters(context)
        return self.checkStatements(context, self.returnType)


    def checkStatements(self, context, returnType: IType):
        try:
            return self.statements.check(context, returnType)
        except SyntaxError as e:
            e.suffix = " in method '" + self.name + "'"
            raise e


    def interpret(self, context):
        context.enterMethod(self)
        try:
            return self.statements.interpret(context)
        except SyntaxError as e:
            e.suffix = " in method '" + self.name + "'"
            raise e
        finally:
            context.leaveMethod(self)


    def isEligibleAsMain(self):
        if self.parameters is None or self.parameters.isEmpty():
            return True
        if self.parameters.size()==1:
            arg = self.parameters[0]
            if isinstance(arg, CategoryParameter):
                itype = arg.getType()
                if isinstance(itype, DictType):
                    return itype.itemType is TextType.instance
        return super(ConcreteMethodDeclaration, self).isEligibleAsMain()


    def toDialect(self, writer):
        if writer.isGlobalContext():
            writer = writer.newLocalWriter()
        self.registerParameters(writer.context)
        super(ConcreteMethodDeclaration, self).toDialect(writer)


    def toMDialect(self, writer):
        writer.append("def ")
        writer.append(self.name)
        writer.append(" (")
        self.parameters.toDialect(writer)
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
        self.parameters.toDialect(writer)
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
        self.parameters.toDialect(writer)
        writer.append(") {\n")
        writer.indent()
        self.statements.toDialect(writer)
        writer.dedent()
        writer.append("}\n")
