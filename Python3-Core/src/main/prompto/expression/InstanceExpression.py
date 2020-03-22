from prompto.param.IParameter import IParameter
from prompto.declaration.AttributeDeclaration import AttributeDeclaration
from prompto.declaration.IDeclaration import IDeclaration
from prompto.expression.IExpression import IExpression
from prompto.parser.Dialect import Dialect
from prompto.runtime.Context import MethodDeclarationMap
from prompto.runtime.LinkedVariable import LinkedVariable
from prompto.runtime.Variable import Variable
from prompto.type.BooleanType import BooleanType
from prompto.type.MethodType import MethodType
from prompto.value.ClosureValue import ClosureValue
from prompto.error.SyntaxError import SyntaxError

class InstanceExpression(IExpression):

    def __init__(self, name):
        super(InstanceExpression, self).__init__()
        self.name = name


    def getName(self):
        return self.name


    def __str__(self):
        return self.name


    def toDialect(self, writer, requireMethod = True):
        if requireMethod and self.requiresMethod(writer):
            writer.append("Method: ")
        writer.append(self.name)


    def requiresMethod(self, writer):
        if writer.dialect is not Dialect.E:
            return False
        o = writer.context.getRegistered(self.name)
        if isinstance(o, MethodDeclarationMap):
            return True
        return False


    def check(self, context):
        from prompto.declaration.CategoryDeclaration import CategoryDeclaration
        named = context.getRegistered(self.name)
        if named is None:
            named = context.getRegisteredDeclaration(IDeclaration, self.name)
        if named is None:
            raise SyntaxError("Unknown identifier:" + self.name)
        elif isinstance(named, Variable):  # local variable
            return named.getType(context)
        elif isinstance(named, LinkedVariable):  # linked variable
            return named.getType(context)
        elif isinstance(named, IParameter):  # named argument
            return named.getType(context)
        elif isinstance(named, CategoryDeclaration):  # any p with x
            return named.getType(context)
        elif isinstance(named, AttributeDeclaration):  # in category method
            return named.getType(context)
        elif isinstance(named, MethodDeclarationMap):  # global method or closure
            method = named.getFirst()
            return MethodType(method)
        else:
            raise SyntaxError(self.name + "  is not a value or method:" + type(named).__name__)


    def interpret(self, context):
        if context.hasValue(self.name):
            v = context.getValue(self.name)
            # TODO not sure why interpret is needed in Python only
            if isinstance(v, IExpression):
                v = v.interpret(context)
            return v
        else:
            named = context.getRegistered(self.name)
            if isinstance(named, MethodDeclarationMap):
                decl = named.getFirst()
                return ClosureValue(context, MethodType(decl))
            else:
                raise SyntaxError("No value or method with name:" + self.name)


    def toPredicate(self, context):
        decl = context.findAttribute(self.name)
        if decl is None:
            raise SyntaxError("Unknown identifier:" + self.name)
        elif decl.getType(context)!=BooleanType.instance:
            raise SyntaxError("Expected a Boolean, got: " + decl.getType(context).typeName)
        else:
            from prompto.expression.EqualsExpression import EqualsExpression
            from prompto.grammar.EqOp import EqOp
            from prompto.literal.BooleanLiteral import BooleanLiteral
            return EqualsExpression(self, EqOp.EQUALS, BooleanLiteral("true"))


    def interpretQuery(self, context, builder):
        predicate = self.toPredicate(context)
        predicate.interpretQuery(context, builder)