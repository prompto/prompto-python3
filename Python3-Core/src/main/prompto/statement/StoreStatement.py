from prompto.statement.SimpleStatement import SimpleStatement
from prompto.type.VoidType import VoidType
from prompto.store.DataStore import DataStore
from prompto.value.IContainer import IContainer
from prompto.value.IInstance import IInstance
from prompto.parser.Dialect import Dialect
from prompto.value.NullValue import NullValue



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
        if not isinstance(other, StoreStatement):
            return False
        return self.to_del == other.to_del and self.to_add == other.to_add


    def check (self, context):
        # TODO check expression
        return VoidType.instance

    def interpret (self,  context):
        idsToDel = self.getIdsToDelete(context)
        storablesToAdd = self.getStorablesToAdd(context)
        if idsToDel is not None or storablesToAdd is not None:
            DataStore.instance.store(idsToDel, storablesToAdd)


    def getIdsToDelete(self, context):
        if self.to_del is None:
            return None
        idsToDel = []
        for exp in self.to_del:
            value = exp.interpret (context)
            if value is NullValue.instance:
                continue
            elif value is IInstance:
                dbId = value.getMember("dbId")
                if dbId is not None and dbId is not NullValue.instance:
                    idsToDel.append(dbId.getStorableData())
            elif value is IContainer:
                for item in value:
                    if item is NullValue.instance:
                        continue
                    elif item is IInstance:
                        dbId = item.getMember("dbId")
                        if dbId is not None and dbId is not NullValue.instance:
                            idsToDel.append(dbId.getStorableData())
        return idsToDel



    def getStorablesToAdd(self, context):
        if self.to_add is None:
            return None
        storablesToAdd = []
        for exp in self.to_add:
            value = exp.interpret(context)
            value.collectStorables(storablesToAdd)
        return storablesToAdd