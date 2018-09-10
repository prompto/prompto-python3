from prompto.jsx.JsxElementBase import JsxElementBase


class JsxSelfClosing(JsxElementBase):

    def __init__(self, name, nameSuite, attributes, openingSuite):
        super(JsxSelfClosing, self).__init__(name, attributes)
        self.nameSuite = nameSuite
        self.openingSuite = openingSuite


    def toDialect(self, writer):
        writer.append("<").append(self.name)
        if self.nameSuite is not None:
            writer.append(self.nameSuite)
        elif(len(self.attributes)>0):
            writer.append(" ")
        for attribute in self.attributes:
           attribute.toDialect(writer)
        writer.append("/>")
        if self.openingSuite is not None:
            writer.append(self.openingSuite)
