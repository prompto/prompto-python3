from prompto.statement.SimpleStatement import SimpleStatement
from prompto.type.VoidType import VoidType
from prompto.store.Store import Store
from prompto.store.MemStore import MemStore
from prompto.value.IInstance import IInstance
from prompto.parser.Dialect import Dialect

class StoreStatement(SimpleStatement):

    def __init__(self, expressions):
        self.expressions = expressions


    def toDialect (self, writer):
        writer.append ("store ")
        if writer.dialect is Dialect.E:
            for exp in self.expressions:
                exp.toDialect (writer)
                writer.append(",")
            writer.trimLast(1)
        else:
            writer.append ('(')
            for exp in self.expressions:
                exp.toDialect (writer)
                writer.append(",")
            writer.trimLast(1)
            writer.append (')')

    def __str__(self):
        return "store " + str(self.expressions)

    def __eq__(self, other):
        if other is self:
            return True
        if other is None:
            return False
        if not isinstance(obj, StoreStatement):
            return False
        return self.expressions == other.expressions


    def check (self, context):
        # TODO check expression
        return VoidType.instance

    def interpret (self,  context):
        store = Store.instance
        if store is None:
            store = MemStore.instance
        for exp in self.expressions:
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