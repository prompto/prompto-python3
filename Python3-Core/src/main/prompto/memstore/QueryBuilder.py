from prompto.memstore.Query import Query
from prompto.store.Store import IQueryBuilder


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

    def project(self, projection):
        self.query.project(projection)

    def addOrderByClause(self, info, descending):
        self.query.addOrderByClause(info, descending)