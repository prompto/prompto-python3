import xml.dom.minidom as minidom
from prompto.type.AnyType import AnyType
from prompto.value.TextValue import TextValue
from prompto.value.ListValue import ListValue
from prompto.value.DocumentValue import DocumentValue

def xmlRead(text: str, keepNamespaces: bool, keepAttributes: bool):
    return XMLReader(keepNamespaces, keepAttributes).read(text)


# noinspection PyUnresolvedReferences
class XMLReader(object):

    def __init__(self, keepNamespaces: bool, keepAttributes: bool):
        self.keepNamespaces = keepNamespaces
        self.keepAttributes = keepAttributes

    def read(self, text: str):
        doc = minidom.parseString(text)
        return self.convertDocument(doc)

    def convertDocument(self, doc: minidom.Document):
        result = DocumentValue()
        self.convertElement(result, doc.documentElement)
        return result

    def convertElement(self, parent: DocumentValue, element: minidom.Element):
        tagName = element.tagName
        # cater for repeated elements
        if parent.hasMember(tagName):
            self.convertListElement(parent, tagName, element)
        else:
            parent.setMember(None, tagName, self.convertElementValue(element))

    def convertListElement(self, parent: DocumentValue, tagName: str, element: minidom.Element):
        list = None
        current = parent.getMemberValue(None, tagName, False)
        if isinstance(current, ListValue):
            list = current
        else:
            list = ListValue(AnyType.instance)
            list.add(current)
            parent.setMember(None, tagName, list)
        list.add(self.convertElementValue(element))

    def convertElementValue(self, element: minidom.Element):
        hasAttributes = self.keepAttributes and element.hasAttributes()
        hasChildren = self.elementHasChildren(element)
        if hasAttributes or hasChildren:
            result = DocumentValue()
            if self.keepAttributes:
                for attr in element.attributes:
                    result.setMember(None, "@" + attr.name, TextValue(attr.value))
            if hasChildren:
                for node in element.childNodes:
                    if isinstance(node, minidom.Element):
                        self.convertElement(result, node)
            else:
                result.setMember(None, "$value", element.firstChild.nodeValue)
            return result
        else:
            return TextValue(element.firstChild.nodeValue)

    def elementHasChildren(self, element: minidom.Element):
        return any(isinstance(node, minidom.Element) for node in element.childNodes)
