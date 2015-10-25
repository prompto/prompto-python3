from prompto.expression.IExpression import IExpression
from prompto.declaration.CategoryDeclaration import CategoryDeclaration
from prompto.parser.Section import Section
from prompto.error.SyntaxError import SyntaxError
from prompto.type.BooleanType import BooleanType
from prompto.store.Store import Store
from prompto.store.MemStore import MemStore

class FetchOneExpression(Section, IExpression):

    def __init__(self, typ, filter):
        self.typ = typ
        self.filter = filter

    def toEDialect (self, writer):
        writer.append ("fetch one ")
        writer.append (self.typ.name)
        writer.append (" where ")
        self.filter.toDialect (writer)

    def toODialect (self, writer):
        writer.append ("fetch one (")
        writer.append (self.typ.name)
        writer.append (") where (")
        self.filter.toDialect (writer)
        writer.append (")")

    def toSDialect (self, writer):
        writer.append ("fetch one ")
        writer.append (self.typ.name)
        writer.append (" where ")
        self.filter.toDialect (writer)

    def check (self, context):
        decl = context.getRegisteredDeclaration (CategoryDeclaration, self.typ.name)
        if decl is None:
            raise SyntaxError ("Unknown category: " + self.typ.name)
        local = context.newLocalContext ()
        filterType = self.filter.check (local)
        if filterType is not BooleanType.instance:
            raise  SyntaxError ("Filtering expression must return a boolean !")
        return self.typ

    def interpret (self, context):
        doc = Store.instance.fetchOne (context, self.filter)
        if doc is None:
            return NullValue.instance
        else:
            return self.typ.newInstanceFromDocument (context, doc)
