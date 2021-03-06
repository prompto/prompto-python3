from prompto.param.UnresolvedParameter import UnresolvedParameter
from prompto.error.ExecutionError import ExecutionError
from prompto.expression.ConstructorExpression import ConstructorExpression
from prompto.expression.IExpression import IExpression
from prompto.grammar.Argument import Argument
from prompto.grammar.ArgumentList import ArgumentList
from prompto.grammar.INamedInstance import INamedInstance
from prompto.literal.TextLiteral import TextLiteral
from prompto.runtime.ErrorVariable import ErrorVariable
from prompto.statement.BaseSwitchStatement import BaseSwitchStatement
from prompto.type.CategoryType import CategoryType
from prompto.type.VoidType import VoidType


class SwitchErrorStatement(BaseSwitchStatement):

    def __init__(self, errorName, instructions):
        super(SwitchErrorStatement, self).__init__()
        self.errorName = errorName
        self.instructions = instructions
        self.alwaysInstructions = None

    def setAlwaysInstructions(self, list_):
        self.alwaysInstructions = list_

    def __str__(self):
        return ""  # TODO

    def checkSwitchCasesType(self, context):
        local = context.newLocalContext()
        local.registerValue(ErrorVariable(self.errorName))
        super().checkSwitchCasesType(local)

    def checkSwitchType(self, context):
        from prompto.type.EnumeratedCategoryType import EnumeratedCategoryType
        return EnumeratedCategoryType("Error")

    def collectReturnTypes(self, context, types):
        itype = self.instructions.check(context, None)
        if itype != VoidType.instance:
            types[itype.getName()] = itype
        local = context.newLocalContext()
        local.registerValue(ErrorVariable(self.errorName))
        super().collectReturnTypes(local, types)
        if self.alwaysInstructions != None:
            itype = self.alwaysInstructions.check(context, None)
            if itype != VoidType.instance:
                types[itype.getName()] = itype


    def interpret(self, context):
        result = None
        try:
            result = self.instructions.interpret(context)
        except ExecutionError as e:
            switchValue = self.populateError(e, context)
            result = self.interpretSwitch(context, switchValue, e)
        finally:
            if self.alwaysInstructions != None:
                self.alwaysInstructions.interpret(context)
        return result


    def populateError(self, e, context):
        error = e.getExpression(context)
        if error == None:
            exp = ConstructorExpression(CategoryType("Error"), None, None)
            args = ArgumentList()
            args.append(Argument(UnresolvedParameter("name"), TextLiteral(type(e).__name__)))
            args.append(Argument(UnresolvedParameter("text"), TextLiteral(e.getMessage())))
            exp.setArguments(args)
            error = exp
        if context.getRegisteredValue(INamedInstance, self.errorName) == None:
            context.registerValue(ErrorVariable(self.errorName))
        if isinstance(error, IExpression):
            error = error.interpret(context)
        context.setValue(self.errorName, error)
        return error


    def toDialect(self, writer):
        writer = writer.newLocalWriter()
        writer.context.registerValue(ErrorVariable(self.errorName))
        super().toDialect(writer)


    def toODialect(self, writer):
        writer.append("try (")
        writer.append(self.errorName)
        writer.append(") {\n")
        writer.indent()
        self.instructions.toDialect(writer)
        writer.dedent()
        writer.append("} ")
        if self.switchCases is not None:
            for sc in self.switchCases:
                sc.catchToODialect(writer)
        if self.defaultCase is not None:
            writer.append("catch(any) {\n")
            writer.indent()
            self.defaultCase.toDialect(writer)
            writer.dedent()
            writer.append("}")
        if self.alwaysInstructions is not None:
            writer.append("finally {\n")
            writer.indent()
            self.alwaysInstructions.toDialect(writer)
            writer.dedent()
            writer.append("}")
        writer.newLine()



    def toMDialect(self, writer):
        writer.append("try ")
        writer.append(self.errorName)
        writer.append(":\n")
        writer.indent()
        self.instructions.toDialect(writer)
        writer.dedent()
        if self.switchCases is not None:
            for sc in self.switchCases:
                sc.catchToMDialect(writer)
        if self.defaultCase is not None:
            writer.append("except:\n")
            writer.indent()
            self.defaultCase.toDialect(writer)
            writer.dedent()
        if self.alwaysInstructions is not None:
            writer.append("finally:\n")
            writer.indent()
            self.alwaysInstructions.toDialect(writer)
            writer.dedent()
        writer.newLine()

    def toEDialect(self, writer):
        writer.append("switch on ")
        writer.append(self.errorName)
        writer.append(" doing:\n")
        writer.indent()
        self.instructions.toDialect(writer)
        writer.dedent()
        if self.switchCases is not None:
            for sc in self.switchCases:
                sc.catchToEDialect(writer)
        if self.defaultCase is not None:
            writer.append("when any:\n")
            writer.indent()
            self.defaultCase.toDialect(writer)
            writer.dedent()
        if self.alwaysInstructions is not None:
            writer.append("always:\n")
            writer.indent()
            self.alwaysInstructions.toDialect(writer)
            writer.dedent()
