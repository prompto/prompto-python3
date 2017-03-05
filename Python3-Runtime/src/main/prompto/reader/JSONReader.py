import json
from prompto.type.AnyType import AnyType
from prompto.value.NullValue import NullValue
from prompto.value.Boolean import Boolean
from prompto.value.Integer import Integer
from prompto.value.Decimal import Decimal
from prompto.value.Text import Text
from prompto.value.ListValue import ListValue
from prompto.value.Document import Document

def jsonRead(text:str):
    node = json.loads(text)
    return toValue(node)

def toValue(node: object):
    if node is None:
        return NullValue.instance
    conv = converters[type(node)]
    return conv(node)

def toBoolean(node):
    return Boolean.ValueOf(node)

def toInteger(node):
    return Integer(node)

def toDecimal(node):
    return Decimal(node)

def toText(node):
    return Text(node)

def toList(node):
    items = [toValue(item) for item in node]
    return ListValue(AnyType.instance, items=items)

def toDocument(node):
    values = {}
    for k, v in node.items():
        values[k] = toValue(v)
    return Document(values=values)

converters =  {
    bool : toBoolean,
    int : toInteger,
    float : toDecimal,
    str : toText,
    list : toList,
    dict : toDocument
}
