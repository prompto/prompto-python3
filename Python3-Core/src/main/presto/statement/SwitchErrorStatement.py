from presto.error.ExecutionError import ExecutionError
from presto.expression.ConstructorExpression import ConstructorExpression
from presto.expression.IExpression import IExpression
from presto.grammar.ArgumentAssignment import ArgumentAssignment
from presto.grammar.ArgumentAssignmentList import ArgumentAssignmentList
from presto.grammar.INamedValue import INamedValue
from presto.grammar.UnresolvedArgument import UnresolvedArgument
from presto.literal.TextLiteral import TextLiteral
from presto.runtime.ErrorVariable import ErrorVariable
from presto.statement.BaseSwitchStatement import BaseSwitchStatement
from presto.type.CategoryType import CategoryType
from presto.type.VoidType import VoidType


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
        from presto.type.EnumeratedCategoryType import EnumeratedCategoryType
        return EnumeratedCategoryType("Error")

    def collectReturnTypes(self, context, types):
        type_ = self.instructions.check(context)
        if type_ != VoidType.instance:
            types[type_.getName()] = type_
        local = context.newLocalContext()
        local.registerValue(ErrorVariable(self.errorName))
        super().collectReturnTypes(local, types)
        if self.alwaysInstructions != None:
            type_ = self.alwaysInstructions.check(context)
            if type_ != VoidType.instance:
                types[type_.getName()] = type_


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
            ctor = ConstructorExpression(CategoryType("Error"), None)
            args = ArgumentAssignmentList()
            args.append(ArgumentAssignment(UnresolvedArgument("name"), TextLiteral(type(e).__name__)))
            args.append(ArgumentAssignment(UnresolvedArgument("text"), TextLiteral(e.getMessage())))
            ctor.setAssignments(args)
            error = ctor
        if context.getRegisteredValue(INamedValue, self.errorName) == None:
            context.registerValue(ErrorVariable(self.errorName))
        if isinstance(error, IExpression):
            error = error.interpret(context)
        context.setValue(self.errorName, error)
        return error

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

    def toPDialect(self, writer):
        writer.append("try ")
        writer.append(self.errorName)
        writer.append(":\n")
        writer.indent()
        self.instructions.toDialect(writer)
        writer.dedent()
        if self.switchCases is not None:
            for sc in self.switchCases:
                sc.catchToPDialect(writer)
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
