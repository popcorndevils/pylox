from enum import Enum, auto

class TokenType(Enum):
    # single character
    LEFT_PAREN = auto()
    RIGHT_PAREN = auto()
    LEFT_BRACKET = auto()
    RIGHT_BRACKET = auto()
    DOT = auto()
    BANG = auto()
    SEMICOLON = auto()
    EQUAL = auto()
    # multicharacter
    LESS_EQUAL = auto()
    GREATER_EQUAL = auto()
    BANG_EQUAL = auto()
    EQUAL_EQUAL = auto()
    IDENTIFIER = auto()
    # literals
    STRING = auto()
    NUMBER = auto()
    NIL = auto()
    # keywords
    VAR = auto()
    # MISC
    ERROR = auto()
    EOF = auto()
