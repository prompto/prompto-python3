from io import BytesIO
from zipfile import ZipFile, ZIP_DEFLATED

from prompto.error.ReadWriteError import ReadWriteError
from prompto.expression.IExpression import IExpression
from prompto.type.BlobType import BlobType
from prompto.utils.JSONGenerator import JSONGenerator
from prompto.value.Blob import Blob


class BlobExpression ( IExpression ):

    def __init__(self, source):
        self.source = source

    def check(self, context):
        self.source.check(context)
        return BlobType.instance

    def interpret(self, context):
        value = self.source.interpret(context)
        try:
            datas = BlobExpression.collectDatas(context, value)
            zipped = BlobExpression.zipDatas(datas)
            return Blob("application/zip", zipped)
        except Exception as e:
            print(e)
            raise ReadWriteError(e.message)

    @classmethod
    def collectDatas(cls, context, value):
        binaries = dict()
        # create textual data
        output = BytesIO()
        generator = JSONGenerator(output)
        value.toJson(context, generator, None, None, binaries)
        # add it
        binaries["value"] = output.getvalue()
        return binaries

    @classmethod
    def zipDatas(cls, datas):
        output = BytesIO()
        zip = ZipFile(output, mode='w', compression=ZIP_DEFLATED)
        for key, value in datas.items():
            zip.writestr(key, value)
        zip.close()
        return output.getvalue()

    def toEDialect(self, writer):
        writer.append("Blob from ")
        self.source.toDialect(writer)

    def toODialect(self, writer):
        writer.append("Blob(")
        self.source.toDialect(writer)
        writer.append(')')

    def toSDialect(self, writer):
        writer.append("Blob(")
        self.source.toDialect(writer)
        writer.append(')')