from prompto.expression.TypeExpression import TypeExpression
from prompto.literal.TextLiteral import TextLiteral
from prompto.processor.AnnotationProcessor import AnnotationProcessor
from prompto.error.SyntaxError import SyntaxError
from prompto.runtime.Variable import Variable


class WidgetFieldProcessor(AnnotationProcessor):

    def processCategory(self, annotation, context, declaration):
        if declaration.isAWidget(context):
            self.doProcessCategory(annotation, context, declaration)
        else:
            raise SyntaxError("WidgetField is only applicable to widgets")


    def doProcessCategory(self, annotation, context, declaration):
        fieldName = annotation.getArgument("name")
        fieldType = annotation.getArgument("type")
        if not isinstance(fieldName, TextLiteral):
            raise SyntaxError("WidgetField requires a Text value for argument 'name'")
        elif not isinstance(fieldType, TypeExpression):
            raise SyntaxError("WidgetField requires a Type value for argument 'type'")
        else:
            name = str(fieldName)
            typ = fieldType.typ
            context.registerValue(Variable(name[1:-1], typ), False)
