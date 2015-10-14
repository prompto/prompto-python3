from prompto.expression.IExpression import IExpression
from prompto.parser.Section import Section

class FetchAllExpression(Section, IExpression):

    def __init__(self, typ, filter, start, end):
        self.typ = typ
        self.filter = filter
        self.start = start
        self.end = end

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
        self.toDialect (writer)

    def check (self, context):
        decl = context.getRegisteredDeclaration (self.typ.name)
        if decl is None:
            raise SyntaxError ("Unknown category: " + self.typ.name)
        local = context.newLocalContext ()
        filterType = self.filter.check (local)
        if filterType is not BooleanType.instance:
            raise  SyntaxError ("Filtering expression must return a boolean !")
        return ListType (self.typ)

    def interpret (self, context):
        store = Store.instance
        if store is None:
            store = MemStore.instance
        doc = store.fetchOne (context, self.filter)
        if doc is None:
            return NullValue.instance
        else:
            return self.typ.newInstanceFromDocument (context, doc)
