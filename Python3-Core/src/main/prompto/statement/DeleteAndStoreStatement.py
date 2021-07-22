from prompto.statement.BaseStatement import BaseStatement
from prompto.type.VoidType import VoidType
from prompto.store.DataStore import DataStore
from prompto.value.DocumentValue import DocumentValue
from prompto.value.IContainer import IContainer
from prompto.value.IInstance import IInstance
from prompto.parser.Dialect import Dialect
from prompto.value.NullValue import NullValue


class DeleteAndStoreStatement(BaseStatement):

    def __init__(self, to_del, to_add, with_meta, andThen):
        super().__init__()
        self.to_del = to_del
        self.to_add = to_add
        self.with_meta = with_meta
        self.andThen = andThen


    def isSimple(self):
        return self.andThen is None


    def toDialect(self, writer):
        if self.to_del is not None:
            writer.append("delete ")
            self.itemsToDialect(self.to_del, writer)
            if self.to_add is not None:
                writer.append(" and ")
        if self.to_add is not None:
            writer.append ("store ")
            self.itemsToDialect(self.to_add, writer)
        if self.with_meta is not None:
            if writer.dialect is Dialect.E:
                writer.append(" with ")
                self.with_meta.toDialect(writer)
                writer.append(" as metadata")
            else:
                writer.append(" with metadata(")
                self.with_meta.toDialect(writer)
                writer.append(')')
        if self.andThen is not None:
            if writer.dialect is Dialect.O:
                writer.append(" then {").newLine().indent()
                self.andThen.toDialect(writer)
                writer.dedent().append("}")
            else:
                writer.append(" then:").newLine().indent()
                self.andThen.toDialect(writer)
                writer.dedent()


    def itemsToDialect (self, items, writer):
        if writer.dialect is not Dialect.E:
            writer.append('(')
        for item in items:
            item.toDialect(writer)
            writer.append(",")
        writer.trimLast(1)
        if writer.dialect is not Dialect.E:
            writer.append(')')


    def __str__(self):
        s = ""
        if self.to_del is not None:
            s += "delete " + ", ".join(self.to_del)
            if self.to_add is not None:
                s += " and "
        if self.to_add is not None:
            s += "store " + ", ".join(self.to_add)
        return s


    def __eq__(self, other):
        if other is self:
            return True
        if other is None:
            return False
        if not isinstance(other, DeleteAndStoreStatement):
            return False
        return self.to_del == other.to_del and self.to_add == other.to_add


    def check (self, context):
        # TODO check expression
        return VoidType.instance


    def interpret (self,  context):
        idsToDel = self.getIdsToDelete(context)
        storablesToAdd = self.getStorablesToAdd(context)
        if idsToDel is not None or storablesToAdd is not None:
            with_meta = None
            if self.with_meta is not None:
                meta = self.with_meta.interpret(context)
                if isinstance(meta, DocumentValue):
                    with_meta = DataStore.instance.newAuditMetadata()
                    for key, value in meta.values.items():
                        with_meta[key] = value.getStorableData()
            DataStore.instance.deleteAndStore(idsToDel, storablesToAdd, with_meta)
        if self.andThen is not None:
            self.andThen.interpret(context)


    def getIdsToDelete(self, context):
        if self.to_del is None:
            return None
        idsToDel = []
        for exp in self.to_del:
            value = exp.interpret (context)
            if value is NullValue.instance:
                continue
            elif isinstance(value, IInstance):
                dbId = value.getMemberValue(context, "dbId")
                if dbId is not None and dbId is not NullValue.instance:
                    idsToDel.append(dbId.getStorableData())
            elif value is IContainer:
                for item in value:
                    if item is NullValue.instance:
                        continue
                    elif isinstance(item, IInstance):
                        dbId = item.getMemberValue(context, "dbId")
                        if dbId is not None and dbId is not NullValue.instance:
                            idsToDel.append(dbId.getStorableData())
        if len(idsToDel) == 0:
            return None
        else:
            return idsToDel


    def getStorablesToAdd(self, context):
        if self.to_add is None:
            return None
        storablesToAdd = []
        for exp in self.to_add:
            value = exp.interpret(context)
            value.collectStorables(storablesToAdd)
        if len(storablesToAdd) == 0:
            return None
        else:
            return storablesToAdd