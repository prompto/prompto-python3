from prompto.declaration.BaseDeclaration import BaseDeclaration
from prompto.error.SyntaxError import SyntaxError
from prompto.utils.TypeUtils import fieldToValue
from prompto.type.CategoryType import CategoryType

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
        self.registerMethods(context)


    def check(self, context):
        from prompto.declaration.AttributeDeclaration import AttributeDeclaration
        if self.attributes is not None:
            for attribute in self.attributes:
                ad = context.getRegisteredDeclaration(AttributeDeclaration, attribute)
                if ad is None and attribute != "text":
                    raise SyntaxError("Unknown attribute: \"" + attribute + "\"")
        return CategoryType(self.getName())


    def getType(self, context):
        return CategoryType(self.getName())


    def hasAttribute(self, context, name):
        if name == "dbId":
            return self.storable
        else:
            return self.attributes is not None and name in self.attributes


    def getAllAttributes(self, context):
        return None if self.attributes is None else set(self.attributes)


    def hasMethod(self, context, key):
        return False


    def isDerivedFrom(self, context, categoryType):
        return False


    def getDerivedFrom(self):
        return None


    def isAWidget(self, context):
        return False


    def checkConstructorContext(self, context):
        # nothing to do
        pass


    def newInstanceFromStored(self, context, stored):
        instance = self.newInstance(context)
        instance.mutable = True
        try:
            self.populateInstance(context, stored, instance)
        finally:
            instance.mutable = False
        return instance


    def populateInstance(self, context, stored, instance):
        dbId = stored.getData("dbId")
        value = fieldToValue(context, "dbId", dbId)
        instance.setMember(context, "dbId", value)
        for name in self.getAllAttributes(context):
            self.populateMember(context, stored, instance, name)
        if instance.storable is not None:
            instance.storable.dirty = False


    def populateMember(self, context, stored, instance, name):
        from prompto.declaration.AttributeDeclaration import AttributeDeclaration
        decl = context.getRegisteredDeclaration(AttributeDeclaration, name)
        if not decl.storable:
            return
        data = stored.getData(name)
        if data is not None:
            value = decl.itype.convertPythonValueToPromptoValue(context, data, None)
            if value is not None:
                instance.setMember(context, name, value)


    def toDialect(self, writer):
        writer = writer.newInstanceWriter(self.getType(writer.context))
        super().toDialect(writer)


    def processAnnotations(self, context, processDerivedFrom):
        if processDerivedFrom:
            derivedFrom = self.getDerivedFrom()
            if derivedFrom is not None:
                for name in derivedFrom:
                    decl = context.getRegisteredDeclaration(CategoryDeclaration, name)
                    if decl is not None:
                        decl.processAnnotations(context, True)
        if self.annotations is not None:
            [ann.processCategory(context, self) for ann  in self.annotations]


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
            if decl.comments is not None:
                for comment in decl.comments:
                    comment.toDialect(writer)
            if decl.annotations is not None:
                for annotation in decl.annotations:
                    annotation.toDialect(writer)
            w = writer.newMemberWriter()
            decl.toDialect(w)
        writer.dedent()


    def methodsToODialect(self, writer, methods):
        for decl in methods:
            if decl.comments is not None:
                for comment in decl.comments:
                    comment.toDialect(writer)
            if decl.annotations is not None:
                for annotation in decl.annotations:
                    annotation.toDialect(writer)
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


    def protoToMDialect(self, writer,  derivedFrom):
        if self.storable:
            writer.append("storable ")
        self.categoryTypeToMDialect(writer)
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
