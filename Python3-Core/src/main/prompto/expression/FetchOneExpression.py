from prompto.expression.IExpression import IExpression
from prompto.declaration.CategoryDeclaration import CategoryDeclaration
from prompto.parser.Section import Section
from prompto.error.SyntaxError import SyntaxError
from prompto.store.AttributeInfo import AttributeInfo
from prompto.store.MatchOp import MatchOp
from prompto.store.TypeFamily import TypeFamily
from prompto.type.AnyType import AnyType
from prompto.store.DataStore import DataStore
from prompto.type.CategoryType import CategoryType
from prompto.value.NullValue import NullValue

class FetchOneExpression(Section, IExpression):

    def __init__(self, typ, predicate, include):
        super()
        self.typ = typ
        self.predicate = predicate
        self.include = include


    def toEDialect (self, writer):
        writer.append ("fetch one ")
        if self.typ:
            if self.typ.mutable:
                writer.append("mutable ")
            writer.append (self.typ.typeName)
            writer.append(" ")
        writer.append ("where ")
        self.predicate.toDialect (writer)
        if self.include is not None:
            writer.append(" include ")
            if len(self.include) == 1:
                writer.append(self.include[0])
            else:
                for i in range(0, len(self.include) - 1):
                    writer.append(self.include[i]).append(", ")
                writer.trimLast(len(", "))
                writer.append(" and ")
                writer.append(self.include[-1])

    def toODialect (self, writer):
        writer.append ("fetch one ")
        if self.typ:
            writer.append("(")
            if self.typ.mutable:
                writer.append("mutable ")
            writer.append (self.typ.typeName)
            writer.append(") ")
        writer.append ("where (")
        self.predicate.toDialect (writer)
        writer.append (")")
        if self.include is not None:
            writer.append(" include (")
            for name in self.include:
                writer.append(name).append(", ")
            writer.trimLast(len(", "))
            writer.append(")")

    def toMDialect (self, writer):
        writer.append ("fetch one ")
        if self.typ:
            if self.typ.mutable:
                writer.append("mutable ")
            writer.append (self.typ.typeName)
            writer.append(" ")
        writer.append ("where ")
        self.predicate.toDialect (writer)
        if self.include is not None:
            writer.append(" include ")
            for name in self.include:
                writer.append(name).append(", ")
            writer.trimLast(len(", "))

    def check (self, context):
        if self.typ is not None:
            decl = context.getRegisteredDeclaration (CategoryDeclaration, self.typ.typeName)
            if decl is None:
                raise SyntaxError ("Unknown category: " + self.typ.typeName)
            context = context.newInstanceContext(None, decl.getType(context), True)
        self.predicate.checkQuery (context)
        if self.typ is None:
            return AnyType.instance
        else:
            return self.typ


    def interpret (self, context):
        store = DataStore.instance
        query = self.buildFetchOneQuery(context, store)
        stored = store.fetchOne (query)
        if stored is None:
            return NullValue.instance
        else:
            typeName = stored.getData("category")[-1]
            typ = CategoryType(typeName)
            if self.typ is not None:
                typ.mutable = self.typ.mutable
            return typ.newInstanceFromStored (context, stored)


    def buildFetchOneQuery(self, context, store):
        builder = store.newQueryBuilder()
        if self.typ is not None:
            info = AttributeInfo("category", TypeFamily.TEXT, True, None)
            builder.verify(info, MatchOp.CONTAINS, self.typ.typeName)
        if self.predicate is not None:
            self.predicate.interpretQuery(context, builder)
        if self.typ is not None and self.predicate is not None:
            builder.And()
        if self.include is not None:
            builder.project(self.include)
        return builder.build()
