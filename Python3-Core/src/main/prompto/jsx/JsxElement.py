from prompto.jsx.JsxElementBase import JsxElementBase


class JsxElement(JsxElementBase):

    def __init__(self, name, nameSuite, attributes, openingSuite):
        super(JsxElement, self).__init__(name, attributes)
        self.nameSuite = nameSuite
        self.openingSuite = openingSuite
        self.children = None
        self.closing = None

    def setChildren(self, children):
        self.children = children

    def setClosing(self, closing):
        self.closing = closing

    def toDialect(self, writer):
        writer.append("<").append(self.name)
        if self.nameSuite is not None:
            writer.appendRaw(self.nameSuite)
        elif(len(self.properties) > 0):
            writer.append(" ")
        for attribute in self.properties:
            attribute.toDialect(writer)
        writer.append(">")
        if self.openingSuite is not None:
            writer.appendRaw(self.openingSuite)
        if self.children is not None:
            for child in self.children:
                child.toDialect(writer)
        self.closing.toDialect(writer)
