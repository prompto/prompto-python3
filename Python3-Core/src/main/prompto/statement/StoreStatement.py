from prompto.statement.SimpleStatement import SimpleStatement
from prompto.type.VoidType import VoidType
from prompto.store.Store import Store
from prompto.store.MemStore import MemStore
from prompto.value.IInstance import IInstance
from prompto.parser.Dialect import Dialect

class StoreStatement(SimpleStatement):

    def __init__(self, to_del, to_add):
        self.to_del = to_del
        self.to_add = to_add



    def toDialect(self, writer):
        if self.to_del is not None:
            writer.append("delete ")
            self.itemsToDialect(self.to_del, writer)
            if self.to_add is not None:
                writer.append(" and ")
        if self.to_add is not None:
            writer.append("store ")
            self.itemsToDialect(self.to_add, writer)



    def itemsToDialect(self, items, writer):
        if writer.dialect is not Dialect.E:
            writer.append('(')
        for item in items:
            item.toDialect(writer)
            writer.append(",")
        writer.trimLast(1)
        if writer.dialect is not Dialect.E:
            writer.append(')')



    def __str__(self):
        return "store " + str(self.to_add)

    def __eq__(self, other):
        if other is self:
            return True
        if other is None:
            return False
        if not isinstance(obj, StoreStatement):
            return False
        return self.to_add == other.expressions


    def check (self, context):
        # TODO check expression
        return VoidType.instance

    def interpret (self,  context):
        store = Store.instance
        if store is None:
            store = MemStore.instance
        for exp in self.to_add:
            value = exp.interpret (context)
            storable = None
            if isinstance(value, IInstance):
                storable = value.storable
            if storable is None:
                raise NotStorableError ()
            if not storable.dirty:
                continue
            document = storable.asDocument ()
            store.store (document)
        return None