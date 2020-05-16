import csv

from io import StringIO

class csvDialect(csv.Dialect):
    delimiter = ','
    quotechar = '"'
    escapechar = '\\'
    doublequote = True
    skipinitialspace = False
    lineterminator = '\r\n'
    quoting = csv.QUOTE_MINIMAL


def csvIterate(text:str, columns:dict, delimiter:str, encloser:str):
    dialect = csvDialect()
    dialect.delimiter = delimiter
    dialect.quotechar = encloser
    file = StringIO(text)
    return DictReader(file, columns, dialect)


def csvRead(text:str, columns:dict, delimiter:str, encloser:str) -> list:
    reader = csvIterate(text, columns, delimiter, encloser)
    return [doc for doc in reader]


def csvReadHeaders(text:str, delimiter:str, encloser:str) -> list:
    reader = csvIterate(text, None, delimiter, encloser)
    return reader.fieldnames


class DictReader(csv.DictReader):

    def __init__(self, file, columns, dialect):
        csv.DictReader.__init__(self, file, dialect=dialect)
        self.columns = columns

    @property
    def fieldnames(self):
        if self._fieldnames is None:
            try:
                self._fieldnames = self.reader.__next__()
                self.convertFieldNames()
            except StopIteration:
                pass
        self.line_num = self.reader.line_num
        return self._fieldnames

    def convertFieldNames(self):
        if self.columns is not None:
            self._fieldnames = [ self.columns.get(fieldName, fieldName) for fieldName in self._fieldnames]


