from ._tokentype import TokenType

class Token:
    WHITE_SPACE = [" ", "\t"]

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
        _lex = "NIL"
        _lit = ""

        if self.lexeme is not None:
            _lex = f"'{self.lexeme}'"
        if self.literal is not None:
            _lit = f" [{self.literal}]"

        return f"{_lex} = {self.type}{_lit}"
