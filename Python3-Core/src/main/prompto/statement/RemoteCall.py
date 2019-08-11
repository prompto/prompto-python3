from prompto.expression.IExpression import IExpression
from prompto.grammar.ArgumentList import ArgumentList
from prompto.parser.Dialect import Dialect
from prompto.runtime.Context import Context
from prompto.runtime.Variable import Variable
from prompto.statement.StatementList import StatementList
from prompto.statement.UnresolvedCall import UnresolvedCall
from prompto.type.VoidType import VoidType


class RemoteCall(UnresolvedCall):

    def __init__(self, caller:IExpression, arguments:ArgumentList, resultName:str, andThen:StatementList):
        super().__init__(caller, arguments)
        self.resultName = resultName
        self.andThen = andThen


    def isSimple(self):
        return False


    def toDialect(self, writer):
        super().toDialect(writer)
        resultType = self.resolveAndCheck(writer.context)
        writer.append(" then")
        writer = writer.newChildWriter()
        if self.resultName is not None:
            writer.append(" with ").append(self.resultName)
            writer.context.registerValue(Variable(self.resultName, resultType))
        if writer.dialect is Dialect.O:
            writer.append(" {")
        else:
            writer.append(":")
        writer = writer.newLine().indent()
        self.andThen.toDialect(writer)
        writer = writer.dedent()
        if writer.dialect is Dialect.O:
            writer.append("}")


    def check(self, context:Context):
        resultType = self.resolveAndCheck(context)
        context = context.newChildContext()
        if self.resultName is not None:
            context.registerValue(Variable(self.resultName, resultType))
        self.andThen.check(context, VoidType.instance)
        return VoidType.instance


    def interpret(self, context:Context):
        resultType = self.resolveAndCheck(context)
        resultValue = super().interpret(context)
        context = context.newChildContext()
        if self.resultName is not None:
            context.registerValue(Variable(self.resultName, resultType))
            context.setValue(self.resultName, resultValue)
        self.andThen.interpret(context)
        return None
