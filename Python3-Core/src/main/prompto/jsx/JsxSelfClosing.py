from prompto.jsx.JsxElementBase import JsxElementBase


class JsxSelfClosing(JsxElementBase):

    def __init__(self, name, nameSuite, properties, openingSuite):
        super(JsxSelfClosing, self).__init__(name, properties)
        self.nameSuite = nameSuite
        self.openingSuite = openingSuite


    def toDialect(self, writer):
        writer.append("<").append(self.name)
        if self.nameSuite is not None:
            writer.append(self.nameSuite)
        elif(len(self.properties) > 0):
            writer.append(" ")
        for prop in self.properties:
           prop.toDialect(writer)
        writer.append("/>")
        if self.openingSuite is not None:
            writer.append(self.openingSuite)
