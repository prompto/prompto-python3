from prompto.store.MatchOp import MatchOp



class Query(object):

    def __init__(self):
        self.predicates = []
        self.first = None
        self.last = None
        self.orderBys = None

    def predicate(self):
        return self.predicates[-1] if len(self.predicates)>0 else None


    def verify(self, info, match, value):
        self.predicates.append(MatchesPredicate(info, match, value))


    def Not(self):
        pred = self.predicates.pop()
        self.predicates.append(NotPredicate(pred))


    def And(self):
        right = self.predicates.pop()
        left = self.predicates.pop()
        self.predicates.append(AndPredicate(left, right))


    def Or(self):
        right = self.predicates.pop()
        left = self.predicates.pop()
        self.predicates.append(OrPredicate(left, right))

    def addOrderByClause(self, info, descending):
        if self.orderBys is None:
            self.orderBys = []
        self.orderBys.append(OrderBy(info, descending))


class OrderBy(object):

    def __init__(self, info, descending):
        self.names = [info.name]
        self.descending = descending


class NotPredicate(object):

    def __init__(self, pred):
        self.pred = pred


    def matches(self, doc):
        return not self.pred.matches(doc)


class AndPredicate(object):

    def __init__(self, left, right):
        self.left = left
        self.right = right


    def matches(self, doc):
        return self.left.matches(doc) and self.right.matches(doc)


class OrPredicate(object):

    def __init__(self, left, right):
        self.left = left
        self.right = right


    def matches(self, doc):
        return self.left.matches(doc) or self.right.matches(doc)


class MatchesPredicate(object):

    def __init__(self, info, match, value):
        self.info = info
        self.match = match
        self.value = value
        self.matcher = self.getMatcher()


    def getMatcher(self):
        if self.match is MatchOp.EQUALS:
            return self.matchesEQUALS
        elif self.match is MatchOp.ROUGHLY:
            return self.matchesROUGHLY
        elif self.match is MatchOp.CONTAINS:
            return self.matchesCONTAINS
        elif self.match is MatchOp.CONTAINED:
            return self.matchesCONTAINED
        elif self.match is MatchOp.GREATER:
            return self.matchesGREATER
        elif self.match is MatchOp.LESSER:
            return self.matchesLESSER
        else:
            return None


    def matches(self, doc):
        if self.matcher is None:
            return False
        else:
            data = doc.get(self.info.name, None)
            return self.matcher(data)

    def matchesGREATER(self, data):
        try:
            return data > self.value
        except:
            return False # cmp not supported


    def matchesLESSER(self, data):
        try:
            return data < self.value
        except:
            return False # cmp not supported


    def matchesCONTAINS(self, data):
        if isinstance(data, str) and isinstance(self.value, str):
            return self.value in data
        elif isinstance(data, (list, set, tuple)):
            return self.value in data
        else:
            return False


    def matchesCONTAINED(self, data):
        if isinstance(data, str) and isinstance(self.value, str):
            return data in self.value
        elif isinstance(self.value, (list, set, tuple)):
            return data in self.value
        else:
            return False


    def matchesROUGHLY(self, data):
        if isinstance(data, str) and isinstance(self.value, str):
            return data.lower()==self.value.lower()
        else:
            return self.matchesEQUALS(data)


    def matchesEQUALS(self, data):
        if data is None:
            return self.value is None
        else:
            return data==self.value
