from ._tokentype import TokenType

class Token:
    WHITE_SPACE = [" ", "\t"]
    ALPHA = {
        "a", "b", "c", "d", "e", "f", "g",
        "h", "i", "j", "k", "l", "m", "n",
        "o", "p", "q", "r", "s", "t", "u",
        "v", "w", "x", "y", "z"}
    NUMERIC = {
        "0", "1", "2", "3", "4", "5", "6",
        "7", "8", "9"}
    KEYWORDS = {
        "var": TokenType.VAR,
        "class": TokenType.CLASS,
    }

    def __init__(self,
            type: TokenType = None,
            lexeme: str = None,
            literal: object = None) -> None:

        if type:
            self.type = type
        else:
            self.type = TokenType.NIL

        self.lexeme = lexeme
        self.literal = literal

    def __repr__(self) -> str:
        _lex = ""
        _lit = ""

        if self.lexeme is not None:
            _lex = f"Lex({self.lexeme}), "
        if self.literal is not None:
            _lit = f", Value({self.literal})"

        return f"Token({_lex}Type({str(self.type).replace('TokenType.', '')}){_lit})"
