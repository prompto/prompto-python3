from io import StringIO

from prompto.error.SyntaxError import SyntaxError
from prompto.expression.IExpression import IExpression
from prompto.expression.Symbol import Symbol

class CategorySymbol(Symbol, IExpression):

    def __init__(self, symbol, assignments):
        super(CategorySymbol, self).__init__(symbol)
        self.assignments = assignments
        self.type_ = None

    def toDialect(self, writer):
        writer.append(self.symbol)
        writer.append(" ")
        self.assignments.toDialect(writer)


    def setType(self, type_):
        self.type = type_

    def getType(self, context=None):
        return self.type

    def setAssignments(self, assignments):
        self.assignments = assignments

    def getAssignments(self):
        return self.assignments

    def __str__(self):
        with StringIO() as sb:
            if len(self.assignments)>0:
                sb.write(str(self.assignments))
            else:
                sb.write(self.type_.getName())
            return sb.getvalue()

    def check(self, context):
        from prompto.declaration.EnumeratedCategoryDeclaration import EnumeratedCategoryDeclaration
        cd = context.getRegisteredDeclaration(EnumeratedCategoryDeclaration, self.type.getName())
        if cd == None:
            raise SyntaxError("Unknown category " + self.type.getName())
        if self.assignments != None:
            context = context.newLocalContext()
            for assignment in self.assignments:
                if not cd.hasAttribute(context, assignment.getName()):
                    raise SyntaxError("\"" + assignment.getName() + \
                                      "\" is not an attribute of " + self.type.getName())
                assignment.check(context)
        return self.type


    def interpret(self, context):
        instance = self.type.newInstance(context)
        instance.mutable = True
        if self.assignments != None:
            context = context.newLocalContext()
            for assignment in self.assignments:
                value = assignment.getExpression().interpret(context)
                instance.setMember(context, assignment.getName(), value)
        instance.setMember(context, "name", self.symbol)
        instance.mutable = False
        return instance
