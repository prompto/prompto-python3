from prompto.jsx.JsxElementBase import JsxElementBase


class JsxElement(JsxElementBase):

    def __init__(self, name, attributes):
        super().__init__(name, attributes)
        self.children = None


    def setChildren(self, children):
        self.children = children


    def toDialect(self, writer):
        writer.append("<").append(self.name)
        for attribute in self.attributes:
            attribute.toDialect(writer)
        writer.append(">")
        if self.children is not None:
            for child in self.children:
                child.toDialect(writer)
        writer.append("</").append(self.name).append(">")
