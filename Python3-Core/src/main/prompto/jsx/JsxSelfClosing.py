from prompto.jsx.JsxElementBase import JsxElementBase


class JsxSelfClosing(JsxElementBase):

    def __init__(self, name, attributes):
        super().__init__(name, attributes)


    def toDialect(self, writer):
        writer.append("<").append(self.name)
        for attribute in self.attributes:
           attribute.toDialect(writer)
        writer.append("/>")
