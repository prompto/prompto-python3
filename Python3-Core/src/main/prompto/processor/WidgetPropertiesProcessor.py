from prompto.declaration.CategoryDeclaration import CategoryDeclaration
from prompto.expression.TypeExpression import TypeExpression
from prompto.grammar.Annotation import Annotation
from prompto.literal.BooleanLiteral import BooleanLiteral
from prompto.literal.DocEntry import DocEntry
from prompto.literal.DocumentLiteral import DocumentLiteral
from prompto.literal.TypeLiteral import TypeLiteral
from prompto.processor.AnnotationProcessor import AnnotationProcessor
from prompto.runtime.Context import Context, MethodDeclarationMap
from prompto.type.IType import IType
from prompto.type.MethodType import MethodType
from prompto.type.PropertiesType import PropertiesType


class WidgetPropertiesProcessor(AnnotationProcessor):

    def processCategory(self, annotation: Annotation, context: Context, declaration: CategoryDeclaration):
        if declaration.isAWidget(context):
            self.doProcessCategory(annotation, context, declaration)
        else:
            raise SyntaxError("WidgetProperties is only applicable to widgets")

    def doProcessCategory(self, annotation: Annotation, context: Context, declaration: CategoryDeclaration):
        widget = declaration.asWidget(context)
        value = annotation.getDefaultArgument()
        properties = self.checkProperties(annotation, context, value)
        if properties is not None and len(properties) > 0:
            widget.properties = properties
        widgetField = self.findWidgetPropertiesFieldAnnotation(context, declaration)
        if widgetField is not None:
            self.overrideWidgetFieldType(context, widgetField, PropertiesType(properties))

    def checkProperties(self, annotation: Annotation, context: Context, value: DocumentLiteral):
        # implement bare minimum for tests since there is use case for python widgets
        properties = dict()
        for entry in value.entries:
            property = self.loadProperty(context, entry)
            if property is not None:
                properties[property.name] = property
        return properties

    def loadProperty(self, context: Context, entry: DocEntry):
        name = str(entry.key)
        validator = None
        value = entry.value
        if isinstance(value, TypeExpression):
            value = value.itype
        if isinstance(value, TypeLiteral):
            itype = value.itype.resolve(context)
            if itype is not None:
                validator = TypeValidator(itype)
        if validator is None:
            return None
        else:
            return Property(name, validator)

    def findWidgetPropertiesFieldAnnotation(self, context: Context, declaration: CategoryDeclaration):

        def isWidgetPropertiesField(ann: Annotation):
            if ann.name != "@WidgetField":
                return False
            for entry in ann.entries:
                if str(entry.key) == "isProperties" and isinstance(entry.value, BooleanLiteral) and entry.value.value:
                    return True
            return False

        return declaration.findAnnotation(context, isWidgetPropertiesField)

    def overrideWidgetFieldType(self, context: Context, widgetField: Annotation, itype: IType ):
        name = str(widgetField.getArgument("name"))[1:-1]
        context = context.getClosestInstanceContext()
        context.overrideWidgetFieldType(name, itype)

class Property:

    def __init__(self, name: str, validator):
        self.name = name
        self.validator = validator

class TypeValidator:

    def __init__(self, itype: IType):
        self.itype = itype

    def getMethodDeclarations(self, context: Context):
        if isinstance(self.itype, MethodType):
            decls: MethodDeclarationMap = context.getRegisteredDeclaration(MethodDeclarationMap, self.itype.typeName)
            if decls is not None:
                return [decl.asReference() for decl in decls.values()]
        return []