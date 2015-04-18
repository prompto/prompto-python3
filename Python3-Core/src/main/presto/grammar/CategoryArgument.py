from presto.declaration.AttributeDeclaration import *
from presto.declaration.ConcreteCategoryDeclaration import *
from presto.declaration.IDeclaration import *
from presto.grammar.BaseArgument import *
from presto.grammar.INamedValue import *
from presto.grammar.ITypedArgument import *
from presto.grammar.IdentifierList import *


class CategoryArgument(BaseArgument, ITypedArgument):

    def __init__(self, type_, name, attributes=None):
        super(CategoryArgument, self).__init__(name)
        self.type_ = type_
        self.attributes = attributes

    def setAttributes(self, attributes):
        self.attributes = attributes

    def getSignature(self, dialect):
        return self.getProto()

    def getProto(self, context):
        if self.attributes == None:
            return self.type_.getName()
        else:
            return self.type_.getName() + '(' + str(self.attributes) + ')';

    def __str__(self):
        return self.name + ':' + self.getProto()

    def hasAttributes(self):
        return self.attributes != None

    def getAttributes(self):
        return self.attributes

    def __eq__(self, obj):
        if id(obj) == id(self):
            return True
        if obj == None:
            return False
        if not isinstance(obj, CategoryArgument):
            return False
        return self.getType() == obj.getType() \
                   and self.getName() == obj.getName() \
            and self.getAttributes() == obj.getAttributes()

    def register(self, context):
        actual = context.getRegisteredValue(INamedValue, self.name)
        if actual != None:
            raise SyntaxError("Duplicate argument: \"" + self.name + "\"")
        if self.attributes != None:
            declaration = ConcreteCategoryDeclaration(self.name)
            declaration.setDerivedFrom(IdentifierList(self.type_.getName()))
            declaration.setAttributes(self.attributes)
            context.registerDeclaration(declaration)
        context.registerValue(self)
        if self.defaultExpression is not None:
            context.setValue(self.name, self.defaultExpression)

    def check(self, context):
        self.type_.checkExists(context)
        if self.attributes != None:
            for attribute in self.attributes:
                actual = context.getRegisteredDeclaration(AttributeDeclaration, attribute)
                if actual == None:
                    raise SyntaxError("Unknown attribute: \"" + attribute + "\"")

    def getType(self, context=None):
        if self.attributes is None or context is None:
            return self.type_
        else:
            return context.getRegisteredDeclaration(IDeclaration, self.name).getType(context)

    def toDialect(self, writer):
        if self.mutable:
            writer.append("mutable ")
        super(CategoryArgument, self).toDialect(writer)
        if self.defaultExpression is not None:
            writer.append(" = ")
            self.defaultExpression.toDialect(writer)


    def toEDialect(self, writer):
        anonymous = "any"==self.type_.name
        self.type_.toDialect(writer)
        if anonymous:
            writer.append(' ')
            writer.append(self.name)
        if self.attributes is not None:
            if len(self.attributes)==1:
                writer.append(" with attribute: ")
                self.attributes.toDialect(writer, False)
            elif len(self.attributes)>1:
                writer.append(" with attributes: ")
                self.attributes.toDialect(writer, True)
        if not anonymous:
            writer.append(' ')
            writer.append(self.name)


    def toODialect(self, writer):
        self.type_.toDialect(writer)
        if self.attributes is not None:
            writer.append('(')
            self.attributes.toDialect(writer, False)
            writer.append(')')
        writer.append(' ')
        writer.append(self.name)

    def toPDialect(self, writer):
        writer.append(self.name)
        writer.append(':')
        self.type_.toDialect(writer)
        if self.attributes is not None:
            writer.append('(')
            self.attributes.toDialect(writer, False)
            writer.append(')')
