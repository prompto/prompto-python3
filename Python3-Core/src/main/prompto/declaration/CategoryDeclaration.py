from prompto.declaration.BaseDeclaration import BaseDeclaration
from prompto.type.CategoryType import *
from prompto.error.SyntaxError import SyntaxError
from prompto.value.Document import Document

class CategoryDeclaration(BaseDeclaration):

    def __init__(self, name, attributes=None):
        super().__init__(name)
        self.attributes = attributes
        self.storable = False

    def setAttributes(self, attributes):
        self.attributes = attributes

    def getAttributes(self):
        return self.attributes

    def register(self, context):
        context.registerDeclaration(self)

    def check(self, context):
        from prompto.declaration.AttributeDeclaration import AttributeDeclaration
        if self.attributes != None:
            for attribute in self.attributes:
                ad = context.getRegisteredDeclaration(AttributeDeclaration, attribute)
                if ad == None:
                    raise SyntaxError("Unknown attribute: \"" + attribute + "\"")
        return CategoryType(self.getName())


    def getType(self, context):
        return CategoryType(self.getName())


    def hasAttribute(self, context, name):
        return self.attributes != None and name in self.attributes


    def hasMethod(self, context, key, object_):
        return False


    def isDerivedFrom(self, context, categoryType):
        return False


    def getDerivedFrom(self):
        return None


    def checkConstructorContext(self, context):
        # nothing to do
        pass

    def newInstanceFromDocument(self, context, document):
        instance = self.newInstance()
        instance.mutable = True
        try:
            for name in self.attributes:
                decl = context.getRegisteredDeclaration(AttributeDeclaration, name)
                if decl is None:
                    # decl = context.getRegisteredDeclaration(AttributeDeclaration, name)
                    raise "abc"
                if not decl.storable:
                    continue
                value = document.getMember(context, name, False)
                if isinstance(value, Document):
                    typ = decl.GetType(context)
                    if not isinstance(typ, CategoryType):
                        raise InternalError("How did we get there?")
                    value = typ.newInstanceFromDocument(context, document)
                instance.setMember(context, name, value)
        finally:
            instance.mutable = False
        return instance


    def toDialect(self, writer):
        writer = writer.newInstanceWriter(self.getType(writer.context))
        super().toDialect(writer)

    def protoToEDialect(self, writer, hasMethods, hasBindings):
        hasAttributes = self.attributes is not None and len(self.attributes)>0
        writer.append("define ")
        writer.append(self.name)
        writer.append(" as ")
        if self.storable:
            writer.append("storable ")
        self.categoryTypeToEDialect(writer)
        if hasAttributes:
            if len(self.attributes)==1:
                writer.append(" with attribute ")
            else:
                writer.append(" with attributes ")
            self.attributes.toDialect(writer, True)
        if hasMethods:
            if hasAttributes:
                writer.append(", and methods:")
            else:
                writer.append(" with methods:")
        elif hasBindings:
            if hasAttributes:
                writer.append(", and bindings:")
            else:
                writer.append(" with bindings:")
        writer.newLine()

    def methodsToEDialect(self, writer, methods):
        writer.indent()
        for decl in methods:
            writer.newLine()
            w = writer.newMemberWriter()
            decl.toDialect(w)
        writer.dedent()

    def methodsToODialect(self, writer, methods):
        for decl in methods:
            w = writer.newMemberWriter()
            decl.toDialect(w)
            writer.newLine()

    def allToODialect(self, writer, hasBody):
        if self.storable:
            writer.append("storable ")
        self.categoryTypeToODialect(writer)
        writer.append(" ")
        writer.append(self.name)
        if self.attributes is not None:
            writer.append('(')
            self.attributes.toDialect(writer, True)
            writer.append(')')
        self.categoryExtensionToODialect(writer)
        if hasBody:
            writer.append(" {\n")
            writer.newLine()
            writer.indent()
            self.bodyToODialect(writer)
            writer.dedent()
            writer.append('}')
            writer.newLine()
        else:
            writer.append(';')

    def categoryExtensionToODialect(self, writer):
        # by default no extension
        pass

    def protoToSDialect(self, writer,  derivedFrom):
        if self.storable:
            writer.append("storable ")
        self.categoryTypeToSDialect(writer)
        writer.append(" ")
        writer.append(self.name)
        writer.append("(")
        if derivedFrom is not None:
            derivedFrom.toDialect(writer, False)
            if self.attributes is not None:
                writer.append(", ")
        if self.attributes is not None:
            self.attributes.toDialect(writer, False)
        writer.append("):\n")
        writer.newLine()
