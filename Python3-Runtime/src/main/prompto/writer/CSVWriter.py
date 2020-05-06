import csv
from io import StringIO

class csvDialect(csv.Dialect):
    delimiter = ','
    quotechar = '"'
    escapechar = '\\'
    doublequote = True
    lineterminator = '\n'
    quoting = csv.QUOTE_MINIMAL


def csvWrite(docs:list, columns:list, mappings:dict, delimiter:str, encloser:str):
    dialect = csvDialect()
    dialect.delimiter = delimiter
    dialect.quotechar = encloser
    with StringIO() as file:
        writer = csv.DictWriter(file, fieldnames=columns, dialect=dialect)
        if mappings is None:
            writer.writeheader()
        else:
            zipped = zip( columns, [ mappings.get(column, column) for column in columns] )
            headers = dict(zipped)
            writer.writerow(headers)
        writer.writerows(docs)
        file.flush()
        return file.getvalue()
