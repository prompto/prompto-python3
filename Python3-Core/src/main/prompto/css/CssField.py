class CssField(object):

    def __init__(self, name, values):
        self.name = name
        self.values = values


    def toDialect(self, writer):
        writer.append(self.name).append(":")
        [val.toDialect(writer) for val in self.values]
        writer.append(";")


    def __str__(self):
        return self.name + ": " + self.valuesToString()


    def valuesToString(self):
        return "".join([str(val) for val in self.values])