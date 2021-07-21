from prompto.store.IAuditMetadata import IAuditMetadata


class IStorable(object):
    pass


class IStored(object):
    pass


class IStore(object):

    def newQueryBuilder(self):
        raise Exception("newQueryBuilder must be implemented by Store instance!")

    def nextSequenceValue(self, name:str):
        raise Exception("nextSequenceValue must be implemented by Store instance!")

    def fetchLatestAuditMetadataId(self, dbId: object) -> object:
        raise Exception("fetchLatestAuditMetadataId must be implemented by Store instance!")

    def fetchAllAuditMetadataIds(self, dbId: object) -> list:
        raise Exception("fetchAllAuditMetadataIds must be implemented by Store instance!")

    def fetchAuditMetadata(self, dbId: object) -> IAuditMetadata:
        raise Exception("fetchAuditMetadata must be implemented by Store instance!")

    def fetchAuditMetadataAsDocument (self, dbId: object) -> dict:
        return self.fetchAuditMetadata(dbId)


class IQueryBuilder(object):

    def setFirst(self, first):
        raise Exception("Must be implemented by QueryBuilder instance!")

    def setLast(self, first):
        raise Exception("Must be implemented by QueryBuilder instance!")

    def verify(self, info, match, value):
        raise Exception("Must be implemented by QueryBuilder instance!")

    def And(self):
        raise Exception("Must be implemented by QueryBuilder instance!")

    def Or(self):
        raise Exception("Must be implemented by QueryBuilder instance!")

    def Not(self):
        raise Exception("Must be implemented by QueryBuilder instance!")

    def addOrderByClause(self, info, descending):
        raise Exception("Must be implemented by QueryBuilder instance!")

    def build(self):
        raise Exception("Must be implemented by QueryBuilder instance!")
