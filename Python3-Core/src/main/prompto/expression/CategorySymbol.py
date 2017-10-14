from io import StringIO

from prompto.error.SyntaxError import SyntaxError
from prompto.expression.IExpression import IExpression
from prompto.expression.Symbol import Symbol


class CategorySymbol(Symbol, IExpression):

    def __init__(self, symbol, assignments):
        super(CategorySymbol, self).__init__(symbol)
        self.assignments = assignments
        self.instance = None
        self.itype = None

    def toDialect(self, writer):
        writer.append(self.symbol)
        writer.append(" ")
        self.assignments.toDialect(writer)


    def setType(self, itype):
        self.itype = itype

    def getType(self, context=None):
        return self.itype

    def setAssignments(self, assignments):
        self.assignments = assignments

    def getAssignments(self):
        return self.assignments

    def __str__(self):
        with StringIO() as sb:
            if len(self.assignments)>0:
                sb.write(str(self.assignments))
            else:
                sb.write(self.itype.typeName)
            return sb.getvalue()

    def check(self, context):
        from prompto.declaration.EnumeratedCategoryDeclaration import EnumeratedCategoryDeclaration
        cd = context.getRegisteredDeclaration(EnumeratedCategoryDeclaration, self.itype.typeName)
        if cd is None:
            raise SyntaxError("Unknown category " + self.itype.typeName)
        if self.assignments is not None:
            context = context.newLocalContext()
            for assignment in self.assignments:
                if not cd.hasAttribute(context, assignment.getName()):
                    raise SyntaxError("\"" + assignment.getName() + \
                                      "\" is not an attribute of " + self.itype.typeName)
                assignment.check(context)
        return self.itype


    def interpret(self, context):
        return self.makeInstance(context)


    def makeInstance(self, context):
        if self.instance is None:
            from prompto.value.Text import Text
            instance = self.itype.newInstance(context)
            instance.mutable = True
            if self.assignments != None:
                context = context.newLocalContext()
                for assignment in self.assignments:
                    value = assignment.getExpression().interpret(context)
                    instance.setMember(context, assignment.getName(), value)
            instance.setMember(context, "name", Text(self.symbol))
            instance.mutable = False
            self.instance = instance
        return self.instance


    def getMemberValue(self, context, name, autoCreate):
        instance = self.makeInstance(context)
        return instance.getMemberValue(context, name, autoCreate)