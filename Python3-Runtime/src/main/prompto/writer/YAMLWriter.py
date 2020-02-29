import yaml
from io import StringIO

from prompto.error.ReadWriteError import ReadWriteError

def yamlWrite(docs):
    stream = StringIO()
    try:
        yaml.safe_dump_all(docs, stream)
        return stream.getvalue()
    except Exception as e:
        raise ReadWriteError(e.message)


