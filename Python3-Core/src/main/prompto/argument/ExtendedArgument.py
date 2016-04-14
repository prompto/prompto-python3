from prompto.argument.CategoryArgument import CategoryArgument


class ExtendedArgument(CategoryArgument):

    def __init__(self, type_, name, attributes):
        super(ExtendedArgument, self).__init__(type_, name)
        self.attributes = attributes

    def setAttributes(self, attributes):
        self.attributes = attributes

    def getProto(self, context):
        return self.type_.getName() + '(' + str(self.attributes) + ')';

    def hasAttributes(self):
        return self.attributes != None

    def getAttributes(self):
        return self.attributes

    def __eq__(self, obj):
        if id(obj) == id(self):
            return True
        if obj == None:
            return False
        if not isinstance(obj, ExtendedArgument):
            return False
        return self.getType() == obj.getType() \
                   and self.getName() == obj.getName() \
            and self.getAttributes() == obj.getAttributes()

    def register(self, context):
        from prompto.grammar.INamedValue import INamedValue
        actual = context.getRegisteredValue(INamedValue, self.name)
        if actual != None:
            raise SyntaxError("Duplicate argument: \"" + self.name + "\"")
        from prompto.declaration.ConcreteCategoryDeclaration import ConcreteCategoryDeclaration
        from prompto.grammar.IdentifierList import IdentifierList
        declaration = ConcreteCategoryDeclaration(self.name)
        declaration.setDerivedFrom(IdentifierList(self.type_.getName()))
        declaration.setAttributes(self.attributes)
        context.registerDeclaration(declaration)
        context.registerValue(self)
        if self.defaultExpression is not None:
            context.setValue(self.name, self.defaultExpression)

    def check(self, context):
        self.type_.checkExists(context)
        for attribute in self.attributes:
            from prompto.declaration.AttributeDeclaration import AttributeDeclaration
            actual = context.getRegisteredDeclaration(AttributeDeclaration, attribute)
            if actual == None:
                raise SyntaxError("Unknown attribute: \"" + attribute + "\"")

    def getType(self, context=None):
        from prompto.declaration.IDeclaration import IDeclaration
        return self.type_ if context is None else context.getRegisteredDeclaration(IDeclaration, self.name).getType(context)

    def toEDialect(self, writer):
        anonymous = "any"==self.type_.name
        self.type_.toDialect(writer)
        if anonymous:
            writer.append(' ')
            writer.append(self.name)
        if len(self.attributes)==1:
            writer.append(" with attribute ")
            self.attributes.toDialect(writer, False)
        elif len(self.attributes)>1:
            writer.append(" with attributes ")
            self.attributes.toDialect(writer, True)
        if not anonymous:
            writer.append(' ')
            writer.append(self.name)


    def toODialect(self, writer):
        self.type_.toDialect(writer)
        writer.append('(')
        self.attributes.toDialect(writer, False)
        writer.append(')')
        writer.append(' ')
        writer.append(self.name)

    def toSDialect(self, writer):
        writer.append(self.name)
        writer.append(':')
        self.type_.toDialect(writer)
        writer.append('(')
        self.attributes.toDialect(writer, False)
        writer.append(')')
