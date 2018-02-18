from enum import Enum

class MatchOp(Enum):
    EQUALS = "EQUALS"
    ROUGHLY = "ROUGHLY"
    CONTAINS = "CONTAINS"
    HAS = "HAS"
    IN = "IN"
    GREATER = "GREATER"
    LESSER = "LESSER"