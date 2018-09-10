class JsxClosing(object):

    def __init__(self, name, suite):
        self.name = name
        self.suite = suite

    def toDialect(self, writer):
        writer.append("</").append(self.name).append(">")
        if self.suite is not None:
            writer.appendRaw(self.suite)
