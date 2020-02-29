import yaml
import inspect
from io import StringIO
from prompto.type.AnyType import AnyType
from prompto.value.NullValue import NullValue
from prompto.value.BooleanValue import BooleanValue
from prompto.value.IntegerValue import IntegerValue
from prompto.value.DecimalValue import DecimalValue
from prompto.value.TextValue import TextValue
from prompto.value.ListValue import ListValue
from prompto.value.DocumentValue import DocumentValue
from prompto.error.ReadWriteError import ReadWriteError

def yamlRead(value):
    docs = yaml.safe_load_all(StringIO(value))
    return convertList(docs)


def convert(obj):
    if obj is None:
        return NullValue.instance
    elif inspect.isgenerator(obj):
        return convert(list(obj))
    elif isinstance(obj, list):
        return convertList(obj)
    elif isinstance(obj, dict):
        return convertDocument(obj)
    elif isinstance(obj, int):
        return IntegerValue(obj)
    elif isinstance(obj, float):
        return DecimalValue(obj)
    elif isinstance(obj, bool):
        return BooleanValue(obj)
    elif isinstance(obj, str):
        return TextValue(obj)
    else:
        raise ReadWriteError("Cannot convert: " + type(obj).__name__)


def convertList(obj):
    items = [ convert(o) for o in obj ]
    return ListValue(AnyType.instance, items=items)


def convertDocument(obj):
    values = {}
    for k, v in obj.items():
        values[k] = convert(v)
    return DocumentValue(values=values)
