class Entry(object):

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def getKey(self):
        return self.key

    def getValue(self):
        return self.value

    def __str__(self):
        return str(self.key) + ':' + str(self.value)

    def toDialect(self, writer):
        writer.append(str(self.key)).append(':')
        self.value.toDialect(writer)
