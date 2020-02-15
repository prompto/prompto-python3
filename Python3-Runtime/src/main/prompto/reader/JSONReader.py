import json
from prompto.type.AnyType import AnyType
from prompto.value.NullValue import NullValue
from prompto.value.BooleanValue import BooleanValue
from prompto.value.IntegerValue import IntegerValue
from prompto.value.DecimalValue import DecimalValue
from prompto.value.TextValue import TextValue
from prompto.value.ListValue import ListValue
from prompto.value.DocumentValue import DocumentValue

def jsonRead(text:str):
    node = json.loads(text)
    return toValue(node)

def toValue(node: object):
    if node is None:
        return NullValue.instance
    conv = converters[type(node)]
    return conv(node)

def toBoolean(node):
    return BooleanValue.ValueOf(node)

def toInteger(node):
    return IntegerValue(node)

def toDecimal(node):
    return DecimalValue(node)

def toText(node):
    return TextValue(node)

def toList(node):
    items = [toValue(item) for item in node]
    return ListValue(AnyType.instance, items=items)

def toDocument(node):
    values = {}
    for k, v in node.items():
        values[k] = toValue(v)
    return DocumentValue(values=values)

converters =  {
    bool : toBoolean,
    int : toInteger,
    float : toDecimal,
    str : toText,
    list : toList,
    dict : toDocument
}
