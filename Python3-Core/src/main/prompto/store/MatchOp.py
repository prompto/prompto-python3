from enum import Enum

class MatchOp(Enum):
    EQUALS = "EQUALS"
    ROUGHLY = "ROUGHLY"
    CONTAINS = "CONTAINS"
    CONTAINED = "CONTAINED"
    GREATER = "GREATER"
    LESSER = "LESSER"