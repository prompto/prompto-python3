import xml.dom.minidom as minidom

def xmlWrite(doc: dict):
    dom = XMLWriter().convertToDocument(doc)
    return dom.toxml()

class XMLWriter(object):

    def convertToDocument(self, doc: dict) -> minidom.Document:
        keys = list(filter(lambda key: key[0] != "@", doc.keys()))
        if len(keys) != 1:
            raise Exception("Document must have a single root element")
        self.document = minidom.Document()
        root = self.convertRootDocument(keys[0], doc)
        self.document.appendChild(root)
        return self.document

    def convertRootDocument(self, tagName: str, doc: dict):
        element = self.document.createElement(tagName)
        self.setElementAttributes(element, doc)
        self.convertValue(element, doc[tagName])
        return element

    def setElementAttributes(self, element: minidom.Element, doc: dict):
        for key in doc.keys():
            if key[0] == "@":
                element.setAttribute(key[1:], str(doc[key]))

    def convertValue(self, parent: minidom.Element, value):
        if value is None:
            return
        elif isinstance(value, (list, set)):
            for item in value:
                self.convertValue(parent, item)
        elif isinstance(value, dict):
            self.convertDictOrDocument(parent, value)
        else:
            parent.appendChild(self.document.createTextNode(str(value)))

    def convertDictOrDocument(self, parent: minidom.Element, value: dict):
        self.setElementAttributes(parent, value)
        children = list(filter(lambda key: key[0] != "@" and key != "$value", value.keys()))
        if len(children) > 0:
            for key in children:
                element = self.document.createElement(key)
                self.convertValue(element, value[key])
                parent.appendChild(element)
        else:
             parent.appendChild(self.document.createTextNode(str(value["$value"])))
