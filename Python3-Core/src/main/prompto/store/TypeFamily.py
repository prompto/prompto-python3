from enum import Enum

class TypeFamily(Enum):
    
    # storable
    BOOLEAN = "BOOLEAN"
    CHARACTER = "CHARACTER"
    INTEGER = "INTEGER"
    DECIMAL = "DECIMAL"
    TEXT = "TEXT"
    UUID = "UUID"
    DATE = "DATE"
    TIME = "TIME"
    DATETIME = "DATETIME"
    PERIOD = "PERIOD"
    VERSION = "VERSION"
    LIST = "LIST"
    SET = "SET"
    TUPLE = "TUPLE"
    RANGE = "RANGE"
    BLOB = "BLOB"
    IMAGE = "IMAGE"
    DOCUMENT = "DOCUMENT"
    CATEGORY = "CATEGORY"
    RESOURCE = "RESOURCE"
    DICTIONARY = "DICTIONARY"
    ENUMERATED = "ENUMERATED"
    # non storable
    VOID = "VOID"
    NULL = "NULL"
    ANY = "ANY"
    METHOD = "METHOD"
    CURSOR = "CURSOR"
    ITERATOR = "ITERATOR"
    CLASS = "CLASS"
    TYPE = "TYPE"
    CODE = "CODE"
    # volatile
    MISSING = "MISSING"
