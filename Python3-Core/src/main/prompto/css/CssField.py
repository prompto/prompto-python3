class CssField(object):

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def toDialect(self, writer):
        writer.append(self.name).append(":")
        self.value.toDialect(writer)
        writer.append(";")
