class IStorable(object):
    pass


class IStored(object):
    pass


class IStore(object):

    def newQueryBuilder(self):
        raise Exception("Must be implemented by Store instance!")


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
