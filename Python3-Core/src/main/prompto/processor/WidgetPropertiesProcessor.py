from prompto.processor.AnnotationProcessor import AnnotationProcessor


class WidgetPropertiesProcessor(AnnotationProcessor):

    def processCategory(self, annotation, context, declaration):
        if declaration.isAWidget(context):
            self.doProcessCategory(annotation, context, declaration)
        else:
            raise SyntaxError("WidgetProperties is only applicable to widgets")

    def doProcessCategory(self, annotation, context, declaration):
        pass

