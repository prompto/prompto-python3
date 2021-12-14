from prompto.store.Store import IStorable, IStored

class StorableDocument(IStorable, IStored):

    def __init__(self, categories, dbIdFactory):
        self.document = None
        self.categories = categories
        self.dbIdFactory = dbIdFactory

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
            dbId = self.dbIdFactory["provider"]()
            self.setData("dbId", dbId)
        return dbId

    def hasData(self, name):
        return self.document is not None and name in self.document

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
        doc["dbId"] = dbId if dbId is not None else self.dbIdFactory["provider"]()
        return doc

    def matches(self, predicate):
        if predicate is None:
            return True
        else:
            return predicate.matches(self.document)

    def project(self, projection):
        remaining = dict()
        for name in projection:
            remaining[name] = self.getData(name)
        remaining["category"] = self.getData("category")
        remaining["dbId"] = self.getData("dbId")
        doc = StorableDocument(self.categories, self.dbIdFactory)
        doc.document = remaining
        return doc

    def names(self):
        return self.document.keys()