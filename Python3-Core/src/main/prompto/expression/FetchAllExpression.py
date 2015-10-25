from prompto.expression.IExpression import IExpression
from prompto.declaration.CategoryDeclaration import CategoryDeclaration
from prompto.parser.Section import Section
from prompto.error.SyntaxError import SyntaxError
from prompto.type.BooleanType import BooleanType
from prompto.type.CursorType import CursorType
from prompto.store.Store import Store
from prompto.value.Cursor import Cursor

class FetchAllExpression(Section, IExpression):

    def __init__(self, typ, filter, start, stop, orderBy):
        self.typ = typ
        self.xstart = start
        self.xstop = stop
        self.filter = filter
        self.orderBy = orderBy

    def toEDialect (self, writer):
        writer.append("fetch ")
        if self.xstart is None:
            writer.append("all ")
        writer.append(self.typ.name)
        if self.xstart is not None:
            self.xstart.toDialect(writer)
            writer.append(" to ")
            self.xstop.toDialect(writer)
        if self.filter is not None:
            writer.append(" where ")
            self.filter.toDialect(writer)
        if self.orderBy is not None:
            self.orderBy.toDialect(writer)

    def toODialect (self, writer):
        writer.append("fetch ")
        if self.xstart is None:
            writer.append("all ")
        writer.append("( ")
        writer.append(self.typ.name)
        writer.append(" ) ")
        if self.xstart is not None:
            writer.append("rows ( ")
            self.xstart.toDialect(writer)
            writer.append(" to ")
            self.xstop.toDialect(writer)
            writer.append(") ")
        if self.filter is not None:
            writer.append(" where ( ")
            self.filter.toDialect(writer)
            writer.append(") ")
        if self.orderBy is not None:
            self.orderBy.toDialect(writer)


    def toSDialect (self, writer):
        writer.append("fetch ")
        if self.xstart is not None:
            writer.append("rows ")
            self.xstart.toDialect(writer)
            writer.append(" to ")
            self.xstop.toDialect(writer)
        else:
            writer.append("all ")
        writer.append(" ( ")
        writer.append(self.typ.name)
        writer.append(" ) ")
        if self.filter is not None:
            writer.append(" where ")
            self.filter.toDialect(writer)
        if self.orderBy is not None:
            self.orderBy.toDialect(writer)

    def check (self, context):
        decl = context.getRegisteredDeclaration (CategoryDeclaration, self.typ.name)
        if decl is None:
            raise SyntaxError ("Unknown category: " + self.typ.name)
        self.checkFilter(context)
        self.checkOrderBy(context)
        self.checkLimits(context)
        return CursorType (self.typ)

    def checkOrderBy (self, context):
        pass # TODO

    def checkLimits (self, context):
        pass # TODO

    def checkFilter (self, context):
        if self.filter is None:
            return
        local = context.newLocalContext ()
        filterType = self.filter.check (local)
        if filterType is not BooleanType.instance:
            raise SyntaxError ("Filtering expression must return a boolean !")

    def interpret (self, context):
        docs = Store.instance.fetchMany (context, self.xstart, self.xstop, self.filter, self.orderBy)
        return Cursor(context, self.typ, docs)
