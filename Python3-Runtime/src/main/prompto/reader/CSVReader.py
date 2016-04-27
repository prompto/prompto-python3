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

def csvIterate(text, delimiter, encloser):
    dialect = csvDialect()
    dialect.delimiter = delimiter
    dialect.quotechar = encloser
    file = StringIO(text)
    return csv.DictReader(file, dialect=dialect)
