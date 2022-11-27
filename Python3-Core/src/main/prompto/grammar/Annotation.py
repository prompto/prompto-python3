from prompto.processor.AnnotationProcessor import AnnotationProcessor


class Annotation(object):

    def __init__(self, name, entries):
        self.name = name
        self.entries = entries


    def toDialect(self, writer):
        writer.append(self.name)
        if self.entries is not None and len(self.entries) > 0:
            writer.append("(")
            for entry in self.entries:
                if entry.key is not None:
                    writer.append(entry.key)
                    writer.append(" = ")
                entry.value.toDialect(writer)
                writer.append(", ")
            writer.trimLast(len(", "))
            writer.append(")")
        writer.newLine()


    def processCategory(self, context, declaration):
        processor = AnnotationProcessor.forName(self.name)
        if processor is not None:
            processor.processCategory(self, context, declaration)


    def getArgument(self, name):
        if self.entries is not None:
            for entry in self.entries:
                if entry.key == name:
                    return entry.value
        return None

    def getDefaultArgument(self):
        if self.entries is not None and len(self.entries) == 1:
            return self.entries[0].value
        else:
            return None