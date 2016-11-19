from prompto.statement.BaseStatement import BaseStatement
from prompto.parser.Dialect import Dialect
from prompto.type.VoidType import VoidType


class CommentStatement(BaseStatement):

    def __init__(self, text):
        super(CommentStatement, self).__init__()
        self.text = text

    def check(self, context):
        return VoidType.instance

    def interpret(self, context):
        return None

    def toDialect(self, writer):
        lines = self.text.split("\n")
        lines = [self.uncomment(line) for line in lines]
        if writer.dialect in [ Dialect.E, Dialect.O ]:
            if len(lines)>1:
                writer.append("/*")
                for line in lines:
                    writer.append(line)
                    writer.newLine()
                writer.trimLast(1)
                writer.append("*/")
                writer.newLine()
            else:
                writer.append("//")
                writer.append(lines[0])
                writer.newLine()
        elif writer.dialect is Dialect.M:
            for line in lines:
                writer.append("#")
                writer.append(line)
                writer.newLine()

    def uncomment(self, line):
        if line.startswith("#"):
            return line[1:]
        elif line.startswith("//"):
            return line[2:]
        else:
            return line
