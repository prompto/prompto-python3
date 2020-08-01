from prompto.param.CategoryParameter import CategoryParameter
from prompto.error.SyntaxError import SyntaxError



class ExtendedParameter(CategoryParameter):
    def __init__(self, itype, name, attributes):
        super(ExtendedParameter, self).__init__(itype, name)
        self.attributes = attributes



    def setAttributes(self, attributes):
        self.attributes = attributes



    def getProto(self):
        return self.itype.typeName + '(' + str(self.attributes) + ')'



    def hasAttributes(self):
        return self.attributes is not None



    def getAttributes(self):
        return self.attributes



    def __eq__(self, obj):
        if id(obj) == id(self):
            return True
        if obj is None:
            return False
        if not isinstance(obj, ExtendedParameter):
            return False
        return self.getType() == obj.getType() \
               and self.getName() == obj.getName() \
               and self.getAttributes() == obj.getAttributes()



    def register(self, context):
        from prompto.grammar.INamedInstance import INamedInstance
        actual = context.getRegisteredValue(INamedInstance, self.name)
        if actual is not None:
            raise SyntaxError("Duplicate argument: \"" + self.name + "\"")
        from prompto.declaration.ConcreteCategoryDeclaration import ConcreteCategoryDeclaration
        from prompto.grammar.IdentifierList import IdentifierList
        declaration = ConcreteCategoryDeclaration(self.name)
        declaration.setDerivedFrom(IdentifierList(self.itype.typeName))
        declaration.setAttributes(self.attributes)
        context.registerDeclaration(declaration)
        context.registerValue(self)
        if self.defaultExpression is not None:
            value = self.defaultExpression.interpret(context)
            context.setValue(self.name, value)



    def check(self, context):
        self.itype.checkExists(context)
        for attribute in self.attributes:
            from prompto.declaration.AttributeDeclaration import AttributeDeclaration
            actual = context.getRegisteredDeclaration(AttributeDeclaration, attribute)
            if actual is None:
                raise SyntaxError("Unknown attribute: \"" + attribute + "\"")



    def getType(self, context=None):
        from prompto.declaration.IDeclaration import IDeclaration
        return self.itype if context is None else context.getRegisteredDeclaration(IDeclaration, self.name).getType(
            context)



    def toEDialect(self, writer):
        self.itype.toDialect(writer)
        writer.append(' ')
        writer.append(self.name)
        if len(self.attributes) == 1:
            writer.append(" with attribute ")
            self.attributes.toDialect(writer, False)
        elif len(self.attributes) > 1:
            writer.append(" with attributes ")
            self.attributes.toDialect(writer, True)



    def toODialect(self, writer):
        self.itype.toDialect(writer)
        writer.append('(')
        self.attributes.toDialect(writer, False)
        writer.append(')')
        writer.append(' ')
        writer.append(self.name)



    def toMDialect(self, writer):
        writer.append(self.name)
        writer.append(':')
        self.itype.toDialect(writer)
        writer.append('(')
        self.attributes.toDialect(writer, False)
        writer.append(')')
