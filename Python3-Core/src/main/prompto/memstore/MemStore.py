from prompto.memstore.Query import Query
from prompto.store.Store import IStorable, IStored, IStore, IQueryBuilder

# a utility class for running unit tests only
class MemStore(IStore):

    lastDbId = 0

    @staticmethod
    def nextDbId():
        MemStore.lastDbId += 1
        return MemStore.lastDbId

    def __init__(self):
        self.documents = dict()


    def isDbIdType(self, typ):
        return typ is int


    def getDbIdType(self):
        return int


    def flush (self):
        pass # nothing to do


    def store (self, dbIdsToDel, docsToStore):
        if dbIdsToDel is not None:
            for dbId in dbIdsToDel:
                del self.documents[dbId]
        if docsToStore is not None:
            for doc in docsToStore:
                self.documents[doc.getData("dbId")] = doc

    def newStorable(self, categories):
        return StorableDocument(categories)



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
        return DocumentIterator(docs, totalCount)


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



class DocumentIterator(object):

    def __init__(self, docs, totalCount):
        self.docs = docs
        self.totalCount = totalCount

    def __len__(self):
        return len(self.docs)

    def totalLength(self):
        return self.totalCount

    def __iter__(self):
        for doc in self.docs:
            yield doc


class StorableDocument(IStorable, IStored):

    def __init__(self, categories):
        self.document = None
        self.categories = categories

    def __getattribute__(self, key):
        if key=="dirty":
            return self.document is not None
        else:
            return object.__getattribute__(self, key)

    def __setattr__(self, key, value):
        if key=="dirty":
            if value==False:
                self.document = None
            else:
                self.document = self.newDocument(None)
        else:
            self.__dict__[key] = value


    def getOrCreateDbId(self):
        dbId = self.getData("dbId")
        if dbId is None:
            dbId = MemStore.nextDbId()
            self.setData("dbId", dbId)
        return dbId



    def getData(self, name):
        if self.document is None:
            return None
        else:
            return self.document.get(name, None)

    def setData (self, name, data):
        if self.document is None:
            self.document = self.newDocument(None)
        self.document[name] = data


    def newDocument(self, dbId):
        doc = dict()
        if self.categories is not None:
            doc["category"] = self.categories
        doc["dbId"] = dbId if dbId is not None else MemStore.nextDbId()
        return doc

    def matches(self, predicate):
        if predicate is None:
            return True
        else:
            return predicate.matches(self.document)

class QueryBuilder(IQueryBuilder):

    def __init__(self):
        self.query = Query()

    def build(self):
        return self.query

    def setFirst(self, first):
        self.query.first = first

    def setLast(self, last):
        self.query.last = last

    def verify(self, info, match, value):
        self.query.verify(info, match, value)

    def And(self):
        self.query.And()

    def Or(self):
        self.query.Or()

    def Not(self):
        self.query.Not()

    def addOrderByClause(self, info, descending):
        self.query.addOrderByClause(info, descending)
