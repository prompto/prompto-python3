from datetime import datetime

from prompto.memstore.AuditMetadata import AuditMetadata
from prompto.memstore.AuditRecord import AuditRecord
from prompto.memstore.QueryBuilder import QueryBuilder
from prompto.memstore.StorableDocument import StorableDocument
from prompto.memstore.StorableDocumentIterator import StorableDocumentIterator
from prompto.store.Store import AuditOperation
from prompto.store.Store import IStore


# a utility class for running unit tests only
class MemStore(IStore):

    def __init__(self):
        self.lastDbId = 0
        self.sequences = dict()
        self.documents = dict()
        self.lastAuditRecordDbId = 0
        self.auditRecords = dict()
        self.lastAuditMetadataDbId = 0
        self.auditMetadatas = dict()

    def nextDbId(self):
        self.lastDbId += 1
        return self.lastDbId

    def nextSequenceValue(self, name):
        value = self.sequences.get(name, 0) + 1
        self.sequences[name] = value
        return value

    def isDbIdType(self, typ):
        return typ is int

    def getDbIdType(self):
        return int

    def flush (self):
        pass # nothing to do

    def deleteAndStore (self, dbIdsToDel, docsToStore, withMeta):
        withMeta = self.storeMetadata(withMeta)
        if dbIdsToDel is not None:
            for dbId in dbIdsToDel:
                self.doDelete(dbId, withMeta)
        if docsToStore is not None:
            for storable in docsToStore:
                self.doStore(storable, withMeta)

    def doDelete(self, dbId, withMeta):
        del self.documents[dbId]
        audit = self.newAuditRecord(withMeta)
        audit.instanceDbId = dbId
        audit.operation = AuditOperation.DELETE
        self.auditRecords[audit.dbId] = audit

    def doStore(self, storable, withMeta):
        operation = AuditOperation.UPDATE
        # ensure db id
        dbId = storable.getData("dbId")
        if not isinstance(dbId, int):
            dbId = ++self.lastDbId
            storable.setData("dbId", dbId)
        if self.auditRecords.get(dbId, None) is None:
            operation = AuditOperation.INSERT
        self.documents[dbId] = storable
        audit = self.newAuditRecord(withMeta)
        audit.instanceDbId = dbId
        audit.operation = operation
        audit.instance = storable
        self.auditRecords[audit.dbId] =  audit

    def newStorableDocument(self, categories, factory):
        provider = factory.get("provider", None)
        def getDbId():
            dbId = provider() if provider is not None else None
            return dbId if dbId is not None else self.nextDbId()
        factory["provider"] = getDbId
        return StorableDocument(categories, factory)

    def newQueryBuilder(self):
        return QueryBuilder()

    def fetchOne (self, query):
        predicate = query.predicate()
        for doc in self.documents.values():
            if doc.matches(predicate):
                return doc
        return None

    def fetchUnique (self, dbId):
        return self.documents.get(dbId, None)

    def fetchMany(self, query):
        # iter all docs
        docs = self.documents.values()
        # filter with predicate
        if query.predicate() is not None:
            docs = self.filterDocs(docs, query.predicate())
        totalCount = len(docs)
        # sort if required
        if query.orderBys is not None:
            docs = self.sortDocs(docs, query.orderBys)
        # slice it if required
        if query.first is not None or query.last is not None:
            docs = self.sliceDocs(docs, query.first, query.last)
        # done
        return StorableDocumentIterator(docs, totalCount)

    def filterDocs(self, docs, predicate):
        res = []
        for doc in docs:
            if doc.matches(predicate):
                res.append(doc)
        return res

    def sortDocs(self, docs, orderBys):
        # need a closure builder on a per clause basis
        def valueExtractor(clause):
            # build the closure to be returned
            def extractValue(doc):
                source = doc
                value = None
                for name in clause.names:
                    value = source.getData(name)
                    source = value
                return value
            return extractValue
        # sorts are guaranteed to be stable, so go through clauses in reverse order
        for clause in reversed(orderBys):
            docs = sorted(docs, key=valueExtractor(clause), reverse = clause.descending)
        return docs

    def sliceDocs(self, docs, first, last):
        if first is None or first < 1:
            first = 1
        if last is None:
            last = len(docs)
        return docs[first-1:last]

    def isAuditEnabled(self) -> bool:
        return True

    def newAuditMetadata(self):
        meta = AuditMetadata()
        self.lastAuditMetadataDbId += 1
        meta.dbId = self.lastAuditMetadataDbId
        meta.utcTimestamp = datetime.utcnow()
        return meta

    def storeMetadata(self, withMeta):
        if withMeta is None:
            withMeta = self.newAuditMetadata()
        self.auditMetadatas[withMeta.dbId] = withMeta
        return withMeta

    def newAuditRecord(self, auditMetadata):
        audit = AuditRecord()
        self.lastAuditRecordDbId += 1
        audit.dbId = self.lastAuditRecordDbId
        audit.metadataDbId = auditMetadata.dbId
        audit.utcTimestamp = auditMetadata.utcTimestamp
        return audit

    def fetchLatestAuditMetadataId(self, dbId: object) -> object:
        audits = filter(lambda a: a.instanceDbId == dbId, self.auditRecords.values())
        audits = sorted(audits, key = lambda a: a.utcTimestamp, reverse = True)
        return None if len(audits) == 0 else audits[0].metadataDbId

    def fetchAllAuditMetadataIds(self, dbId: object) -> object:
        audits = filter(lambda a: a.instanceDbId == dbId, self.auditRecords.values())
        audits = sorted(audits, key = lambda a: a.utcTimestamp, reverse = True)
        return [a.metadataDbId for a in audits]

    def fetchAuditMetadata(self, dbId: object) -> AuditMetadata:
        return self.auditMetadatas.get(dbId, None)

    def fetchAuditMetadataAsDocument(self, dbId: object) -> dict:
        return self.auditMetadatas.get(dbId, None)

    def fetchLatestAuditRecord(self, dbId: object) -> AuditRecord:
        audits = self.fetchAllAuditRecordsStream(dbId)
        return audits[0] if len(audits) > 0 else None

    def fetchLatestAuditRecordAsDocument(self, dbId: object) -> dict:
        audit = self.fetchLatestAuditRecord(dbId)
        return None if audit is None else audit.asDocument()

    def fetchAllAuditRecords(self, dbId: object) -> list:
        audits = self.fetchAllAuditRecordsStream(dbId)
        return list(audits)

    def fetchAllAuditRecordsAsDocuments(self, dbId: object) -> list:
        audits = self.fetchAllAuditRecordsStream(dbId)
        return list([a.asDocument() for a in audits])

    def fetchAllAuditRecordsStream(self, dbId: object) -> iter:
        audits = filter(lambda a: a.instanceDbId == dbId, self.auditRecords.values())
        return sorted(audits, key=lambda a: a.utcTimestamp, reverse=True)

    def fetchDbIdsAffectedByAuditMetadataId(self, dbId: object) -> list:
        audits = filter(lambda a: a.metadataDbId == dbId, self.auditRecords.values())
        audits = sorted(audits, key=lambda a: a.utcTimestamp, reverse=True)
        return list([a.instanceDbId for a in audits])

    def fetchAuditRecordsMatching(self, auditPredicates: dict, instancePredicates: dict) -> list:
        return list(self.fetchAuditRecordsMatchingStream(auditPredicates, instancePredicates))

    def fetchAuditRecordsMatchingAsDocuments(self, auditPredicates: dict, instancePredicates: dict) -> list:
        audits = self.fetchAuditRecordsMatchingStream(auditPredicates, instancePredicates)
        return list([a.asDocument() for a in audits])

    def fetchAuditRecordsMatchingStream(self, auditPredicates: dict, instancePredicates: dict) -> iter:
        audits = filter(lambda a: a.matches(auditPredicates, instancePredicates), self.auditRecords.values())
        return sorted(audits, key=lambda a: a.utcTimestamp, reverse=True)

    def deleteAuditRecord(self, dbId: object) -> bool:
        return self.auditRecords.pop(dbId, None) is not None

    def deleteAuditMetadata(self, dbId: object) -> bool:
        return self.auditMetadatas.pop(dbId, None) is not None