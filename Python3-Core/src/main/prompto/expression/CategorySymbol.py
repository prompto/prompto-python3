from io import StringIO

from prompto.error.SyntaxError import SyntaxError
from prompto.expression.IExpression import IExpression
from prompto.expression.Symbol import Symbol


class CategorySymbol(Symbol, IExpression):

    def __init__(self, symbol, arguments):
        super(CategorySymbol, self).__init__(symbol)
        self.arguments = arguments
        self.instance = None
        self.itype = None

    def toDialect(self, writer):
        writer.append(self.symbol)
        writer.append(" ")
        self.arguments.toDialect(writer)


    def setType(self, itype):
        self.itype = itype

    def getType(self, context=None):
        return self.itype

    def setArguments(self, arguments):
        self.arguments = arguments

    def getArguments(self):
        return self.arguments

    def __str__(self):
        with StringIO() as sb:
            if len(self.arguments)>0:
                sb.write(str(self.arguments))
            else:
                sb.write(self.itype.typeName)
            return sb.getvalue()

    def check(self, context):
        from prompto.declaration.EnumeratedCategoryDeclaration import EnumeratedCategoryDeclaration
        cd = context.getRegisteredDeclaration(EnumeratedCategoryDeclaration, self.itype.typeName)
        if cd is None:
            raise SyntaxError("Unknown category " + self.itype.typeName)
        if self.arguments is not None:
            context = context.newLocalContext()
            for argument in self.arguments:
                if not cd.hasAttribute(context, argument.getName()):
                    raise SyntaxError("\"" + argument.getName() + \
                                      "\" is not an attribute of " + self.itype.typeName)
                argument.check(context)
        return self.itype


    def interpret(self, context):
        return self.makeInstance(context)


    def makeInstance(self, context):
        if self.instance is None:
            from prompto.value.TextValue import TextValue
            instance = self.itype.newInstance(context)
            instance.mutable = True
            if self.arguments != None:
                context = context.newLocalContext()
                for argument in self.arguments:
                    value = argument.getExpression().interpret(context)
                    instance.setMember(context, argument.getName(), value)
            instance.setMember(context, "name", TextValue(self.symbol))
            instance.mutable = False
            self.instance = instance
        return self.instance


    def getMemberValue(self, context, name, autoCreate):
        instance = self.makeInstance(context)
        return instance.getMemberValue(context, name, autoCreate)