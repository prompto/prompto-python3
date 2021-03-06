from io import StringIO


class Indenter(object):

    def __init__(self, file):
        self.file = file
        self.indents = ""
        self.isStartOfLine = False

    def appendTabsIfRequired(self, s):
        if self.isStartOfLine:
            self.file.write(self.indents)
        self.isStartOfLine = len(s) >0  and s[-1] == '\n'

    def indent(self):
        self.indents += '\t'

    def dedent(self):
        if len(self.indents)==0:
            raise Exception("Illegal dedent!")
        self.indents = self.indents[1:]

class CodeWriter(object):

    def __init__(self, dialect, context, file = None, indenter = None):
        self.dialect = dialect
        self.context = context
        self.file = file if file is not None else StringIO()
        self.indenter = indenter if indenter is not None else Indenter(self.file)


    def appendRaw(self, s):
        self.file.write(s)
        return self


    def append(self, s):
        self.indenter.appendTabsIfRequired(s)
        self.file.write(s)
        return self


    def trimLast(self, count):
        len = self.file.tell()
        self.file.seek(len-count)
        self.file.truncate()
        return self


    def indent(self):
        self.indenter.indent()
        return self


    def dedent(self):
        self.indenter.dedent()
        return self


    def newLine(self):
        self.append('\n')
        return self


    def __str__(self):
        return self.file.getvalue()


    def isGlobalContext(self):
        return self.context.isGlobalContext()


    def newLocalWriter(self):
        return CodeWriter(self.dialect, self.context.newLocalContext(), self.file, self.indenter)


    def newChildWriter(self, context = None):
        if context is None:
            context = self.context.newChildContext()
        return CodeWriter(self.dialect, context, self.file, self.indenter)


    def newInstanceWriter(self, typ):
        return CodeWriter(self.dialect, self.context.newInstanceContext(None, typ), self.file, self.indenter)


    def newDocumentWriter(self):
        return CodeWriter(self.dialect, self.context.newDocumentContext(None, False), self.file, self.indenter)


    def newMemberWriter(self):
        return CodeWriter(self.dialect, self.context.newChildContext(), self.file, self.indenter)
