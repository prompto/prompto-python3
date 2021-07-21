class StorableDocumentIterator(object):

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