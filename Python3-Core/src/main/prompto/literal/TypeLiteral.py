from prompto.expression.IExpression import IExpression
from prompto.parser.Dialect import Dialect
from prompto.parser.Section import Section
from prompto.runtime.Context import Context, MethodDeclarationMap
from prompto.type.IType import IType
from prompto.type.TypeType import TypeType
from prompto.utils.CodeWriter import CodeWriter
from prompto.value.TypeValue import TypeValue


class TypeLiteral(Section, IExpression):

    def __init__(self, itype:IType):
        super().__init__()
        self.itype = itype


    def check(self, context:Context):
        return TypeType(self.itype)


    def interpret(self, context:Context):
        return TypeValue(self.itype)


    def toDialect(self, writer:CodeWriter):
        if writer.dialect is Dialect.E:
            decl = writer.context.getRegisteredDeclaration(MethodDeclarationMap, self.itype.typeName)
            if isinstance(decl, MethodDeclarationMap):
                writer.append("Method: ")
            else:
                writer.append("Type: ")
        self.itype.toDialect(writer)

    def parentToDialect(self, writer:CodeWriter):
        self.itype.toDialect(writer)


    def __str__(self):
        return str(self.itype)
